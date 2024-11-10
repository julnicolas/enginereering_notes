# Check cluster is running


This is useful for dev purpose. Using `apache/kafka` image:
``` sh
docker exec -it kafka /opt/kafka/bin/kafka-cluster.sh cluster-id --bootstrap-server :9092
```

It must respond with an answer of the like:
`Cluster ID: 5L6g3nShT-eMCtK--X86sw`

