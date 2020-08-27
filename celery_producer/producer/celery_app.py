from celery import Celery
from celery import bootsteps
from kombu import Consumer, Exchange, Queue
# import time

my_queue = Queue('custom', Exchange('custom'), 'routing_key')

app = Celery(broker='amqp://guest:guest@rabbitmq')
app.conf.task_protocol = 1

def send_me_a_message(who, producer=None):
    with app.producer_or_acquire(producer) as producer:
        producer.publish(
            {'hello': who},
            serializer='json',
            exchange=my_queue.exchange,
            routing_key='routing_key',
            declare=[my_queue],
            retry=True,
        )