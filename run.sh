#!/bin/bash

worker=${WORKER:-1}
port=${PORT:-8080}

gunicorn --worker-tmp-dir /dev/shm --bind 0.0.0.0:${port} -k gevent -w $worker wsgi:app