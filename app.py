from transformers import AutoTokenizer, AutoModelForCausalLM, Conversation, ConversationalPipeline
from flask import Flask, request, render_template, url_for, redirect
import torch, os

# Transformes file path
transformers_path = os.path.join("transformers")

# Model setup
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/DialoGPT-small", 
    cache_dir=transformers_path
)
tokenizer = AutoTokenizer.from_pretrained(
    "microsoft/DialoGPT-small", 
    cache_dir=transformers_path,
    padding='max_length',
    max_length=1024,
    truncation=True,
    padding_side='left'
)
chatbot = ConversationalPipeline(
    model=model, 
    tokenizer=tokenizer,
    max_length=1024
)

# Conversation setup
conversation = Conversation()

# Flask setup
app = Flask(__name__)

##############################################################################################################################
#                                                   Flask Routes                                                             #
##############################################################################################################################

@app.route("/")
def index():
    # Home page
    messages = []
    for is_user, text in conversation.iter_texts():
        messages.append({
            "user": "You" if is_user else "PenPen",
            "text": text
        })
    return render_template("index.html", messages=messages)

@app.route("/add_input", methods=["POST"])
def add_input():
    # Process user input
    global conversation
    text = request.form["user_message"]
    conversation.add_user_input(text)
    conversation = chatbot(conversation)
    messages = []
    for is_user, text in conversation.iter_texts():
        messages.append({
            "is_user": is_user,
            "text": text
        })
    return 'ok', 200

@app.route("/reset", methods=["POST", "GET"])
def reset():
    global conversation
    conversation = Conversation()
    return redirect(url_for("index"))

# Run app in development mode
if __name__ == "__main__":
    app.run(debug=True)