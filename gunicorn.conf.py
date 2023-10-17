import multiprocessing

workers = 2

# Always use https in production
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-Forwarded-Proto': 'https'}