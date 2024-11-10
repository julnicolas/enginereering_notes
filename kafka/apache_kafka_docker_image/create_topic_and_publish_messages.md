# Create topic and publish messages

The following command creates a topic, then publishes a few messages:
``` sh
docker exec -it kafka /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server :9092 --topic demo
```

Press `ctrl + c` to exit, `enter` to send another message.

