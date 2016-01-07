from kafka import KafkaConsumer
from conf.kafka_app import REPLICA

def main():
    consumer = KafkaConsumer(REPLICA['TOPIC'],
                             group_id=REPLICA['GROUP_ID'],
                             metadata_broker_list=REPLICA['BROKER'])
    for message in consumer:
        # This will wait and print messages as they become available
        print(message)


if __name__ == "__main__":
    main()