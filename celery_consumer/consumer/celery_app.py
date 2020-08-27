from celery import Celery
from celery import bootsteps
from kombu import Consumer, Exchange, Queue

my_queue = Queue('custom', Exchange('custom'), 'routing_key')

app = Celery(broker='amqp://guest:guest@rabbitmq')
app.conf.task_protocol = 1


class MyConsumerStep(bootsteps.ConsumerStep):

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[my_queue],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):
        print(' message block started')
        print('Received message: {0!r}'.format(body))
        print('handle message block ended')
        message.ack()
        print('ack message block ended')
app.steps['consumer'].add(MyConsumerStep)