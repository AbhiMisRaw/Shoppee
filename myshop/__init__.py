from .celery import app as celery_app

# we added here so that it loads when we start the server.
__all__ = ['celery_app']

# Now, celery has been added you can use celery now.

# A celery worker is a process, that handles bookkeeping feature 
# like sending/receiving queue messages, registering task killing hung tasks, tracking status and so on.

# A worker instance can consume from any number of messages queues.