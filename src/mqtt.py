from umqtt.simple import MQTTClient

class MQTT:
    def __init__(self, client_id, broker):
        self.client = MQTTClient(client_id, broker)
        self.topics = {}
        self.client.set_callback(self._callback)
        self.client.connect()

    def _callback(self, topic, msg):
        topic_str = topic.decode()
        if topic_str in self.topics:
            self.topics[topic_str](msg.decode())

    def subscribe(self, topic, callback):
        self.topics[topic] = callback
        self.client.subscribe(topic)

    def publish(self, topic, message):
        self.client.publish(topic, message)

    def check_messages(self):
        self.client.check_msg()