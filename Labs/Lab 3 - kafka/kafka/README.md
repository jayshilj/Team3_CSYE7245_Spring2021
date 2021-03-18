#### Lab 3 - Apache Kafka

1. Google Docs Link : https://docs.google.com/document/d/1Nh6rB67CbmXL5hBK7logKcKF0ra49wNYU59jH5Vln_8/edit# 

2. CLAT Document Link : https://codelabs-preview.appspot.com/?file_id=1Nh6rB67CbmXL5hBK7logKcKF0ra49wNYU59jH5Vln_8#4 

## Apache Kafka


#### What is Kafka?
Apache Kafka is an event streaming platform used to collect, process, store, and integrate data at scale. It has numerous use cases including distributed logging, stream processing, data integration, and pub/sub messaging.

#### Events? What are they?
An event is any type of action, incident, or change that's identified or recorded by software or applications. For example, a payment, a website click, or a temperature reading, along with a description of what happened.

#### Where do I use Kafka?
Assume you have multiple source systems that generate data and this data has to be consumed by one or more target system(s). As the number of source and target systems increase, there is an increased complexity to map all source systems to their respective targets.

![kafka1](https://github.com/jayshilj/Team4_CSYE7245_Spring2021/blob/main/Labs/Lab%203/kafka/img/kafka1.jpeg)

Therefore, maintaining the infrastructure and ensuring system resilience and reliability and data consistency is also a huge challenge. This is where Kafka can help.

![kafka2](https://github.com/jayshilj/Team4_CSYE7245_Spring2021/blob/main/Labs/Lab%203/kafka/img/kafka2.jpeg)

### Getting Started

#### Download & Configure Kafka
- Download Apache Kafka from [here](https://kafka.apache.org/downloads)
- Unzip contents of the downloaded file

#### Python Libraries 

- kafka-python - Install the Python client for the Apache Kafka by running `pip3 install kafka-python`. This library is designed to function much like the official java client & can help publish and receive messages from Python. Alternatively, you may use `confluent-kafka-python` as well, but for this exercise, we would be using `kafka-python`.

#### Starting Zookeeper & Kafka Broker

Navigate to the directory where the downloaded files are unzipped and start the Zookeeper service:
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```
Additionally, start the Kafka broker by running:
```
bin/kafka-server-start.sh config/server.properties
```

### Usage

Once the Zookeeper and Kafka broker services are started, we can use the Python scripts on this repo.

#### Using `producer.py`
Run the script to publish events to the newly created topic `sample`

#### Using `consumer.py`
Run the script to consume the events published by the producer. This script should write messages to the console.

## Level UP! :arrow_up:

Let's work with a use-case that collects real-time sampled tweets from [Twitter](twitter.com) and publishes these to a Kafka Broker.

### Requirements

This requires the use of a Twitter Developer account. Apply for one [here](https://developer.twitter.com/en/apply-for-access). Once you have access to your developer account:

- Create a new Project on the dev console
- Generate your API keys and bearer tokens

:warning: Never share your tokens or push them to GitHub

### Usage

Use the `twitter-stream.py` script to fetch tweets using Twitter's API in real-time. Ensure that you enter your bearer token in the script under the `BEARER_TOKEN` param. This script:
- Fetches sampled tweets in real-time.
  
- Publishes these tweets to the Kafka Broker

On running `consumer.py` - you should see all the published events, that are collected by the consumer. 

ß