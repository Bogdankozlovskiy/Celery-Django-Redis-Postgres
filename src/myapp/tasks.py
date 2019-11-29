from __future__ import absolute_import, unicode_literals
import logging
from mydjango.celery import app

logger = logging.getLogger("celery")

#@app.task(bind=True)
#def debug_task(self):
#    print('Request: {0!r}'.format(self.request))

@app.task
def show_hello_world():
    logger.info("-"*25)
    logger.info("Printing Hello from Celery")
    logger.info("-"*25)

@app.task
def add(x,  y):
	return x + y

@app.task
def say_hello():
	return 'hello my friend'


app.conf.beat_schedule = {
    "hello_world": {
        "task": "myapp.tasks.show_hello_world",
        "schedule": 10.0,
    },
    'my_add':{
    	'task':'myapp.tasks.add',
    	'schedule': 20.0,
    	'args': (5, 7),
    }
}