echo "Running Performance Measurement workloads"

python3 performance_measurement/measure_performance.py --workdir testrun-anvil-zk-performance --input-dir testrun-anvil-zk --anvil-config data/anvil-zookeeper-operator/config.json --reference-config data/zookeeper-operator/v0.2.15/config.json --project zookeeper-operator --sample
echo "ZooKeeper operator performance results are stored in testrun-anvil-zk-performance"

python3 performance_measurement/measure_performance.py --workdir testrun-anvil-rabbitmq-performance --input-dir testrun-anvil-rabbitmq --anvil-config data/anvil-rabbitmq-operator/config.json --reference-config data/rabbitmq-operator/v2.5.0/config.json --project rabbitmq-operator --sample
echo "RabbitMQ controller performance results are stored in testrun-anvil-rabbitmq-performance"

python3 performance_measurement/measure_performance.py --workdir testrun-anvil-fluent-performance --input-dir testrun-anvil-fluent --anvil-config data/anvil-fluent-controller/config.json --reference-config data/fluent-operator/config.json --project fluent-operator --sample
echo "Fluent controller performance results are stored in testrun-anvil-fluent-performance"

echo "Parsing performance data"

python3 plugins/performance_measurement/process_ts.py
