import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1

# Always use https in production
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-Forwarded-Proto': 'https'}