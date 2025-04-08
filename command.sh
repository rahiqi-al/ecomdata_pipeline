docker exec -it -u airflow airflow bash
pip install -r /project/requirements.txt

Créer_topic
docker exec -it kafka kafka-topics --create --topic test --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

Publier_message_topic
docker exec -it kafka kafka-console-producer --broker-list localhost:9092 --topic test

Consommer_messages_topic
docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic test --from-beginning



docker volume rm ecomdata_pipeline_kafka_data ecomdata_pipeline_zookeeper_data