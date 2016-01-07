import time

from kafka import SimpleProducer, KafkaClient
from kafka.common import LeaderNotAvailableError

from conf.kafka_app import REPLICA

def print_response(response=None):
    if response:
        print('Error: {0}'.format(response[0].error))
        print('Offset: {0}'.format(response[0].offset))


def main():
    kafka = KafkaClient(REPLICA['BROKER'][0])
    producer = SimpleProducer(kafka)

    # single kafka-server
    # topic = b'test'

    # replica 3 kafka-server
    topic = 'my-replicated-topic'
    msg = "Hello ~~~~~~~~~~!! "

    try:
        print_response(producer.send_messages(topic, msg))
    except LeaderNotAvailableError:
        # https://github.com/mumrah/kafka-python/issues/249
        # time.sleep(1)
        print_response(producer.send_messages(topic, msg))

    # kafka.close()

if __name__ == "__main__":
    main()