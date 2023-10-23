from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration, Conversation, ConversationalPipeline
from flask import Flask, request, jsonify, render_template, url_for, redirect, session
import torch, os

# Transformes file path
transformers_path = "./transformers"

# Model setup
model = BlenderbotForConditionalGeneration.from_pretrained(
    "facebook/blenderbot-400M-distill", 
    cache_dir=transformers_path
)
tokenizer = BlenderbotTokenizer.from_pretrained(
    "facebook/blenderbot-400M-distill", 
    cache_dir=transformers_path
)
chatbot = ConversationalPipeline(
    model=model, 
    tokenizer=tokenizer,
)

# Conversation setup
conversation = Conversation(max_length=10000)

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

@app.route("/add_input", methods=["POST", "GET"])
def add_input():
    # Process user input
    global conversation
    text = request.form["question"]
    conversation.add_user_input(text)
    conversation = chatbot(conversation)
    messages = []
    for is_user, text in conversation.iter_texts():
        messages.append({
            "is_user": is_user,
            "text": text
        })
    return redirect(url_for("index"))

@app.route("/reset", methods=["POST", "GET"])
def reset():
    global conversation
    conversation = Conversation()
    return redirect(url_for("index"))

# Run app in development mode
if __name__ == "__main__":
    app.run(debug=True)