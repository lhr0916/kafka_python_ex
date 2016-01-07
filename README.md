# kafka_python_ex

1. run vagrant kafka-server(replica : 3)
2. virtualenv kafka_python_ex ; pip install -r requirements.txt (pip freeze > requirements.txt)
3. python consumer.py
4. python producer.py
5. vagrant@kafka-1:/tmp/kafka-logs-1/my-replicated-topic-0$ tail -f /tmp/kafka-logs/my-replicated-topic-0/00000000000000000000.log /tmp/kafka-logs-1/my-replicated-topic-0/00000000000000000000.log /tmp/kafka-logs-2/my-replicated-topic-0/00000000000000000000.log


