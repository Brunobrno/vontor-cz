# gunicorn_config.py

bind = '0.0.0.0:8000'  # Specify the host and port for Gunicorn to listen on

workers = 4  # Number of worker processes
max_requests = 1000 # Number of requests before worker restarts
timeout = 300  # Timeout for worker processes in seconds
#keepalive = 2  # Number of seconds to keep an idle client connection open
worker_tmp_dir = '/dev/shm' # Worker temporary directory

#errorlog = '-'  # Log to stdout

preload_app = True

module = "vontor_cz.asgi:application"