#!/usr/bin/env python
import pika
import json

"""
config = {'host': '192.168.10.12',
          'port': 5672,
          'username': 'user01',
          'password': '123456',
          'exchange': 'exchang-01',
          'virtual_host': '/host1',
          }
"""


def create_connection(config):
    """
    创建RabbitMQ连接
    :param config:
    :return:
    """
    credentials = pika.PlainCredentials(username=config['username'], password=config['password'])  # mq用户名和密码
    # 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
    param = pika.ConnectionParameters(host=config['host'], port=config['port'],
                                      virtual_host=config['virtual_host'], credentials=credentials)
    return pika.BlockingConnection(param)


class Subscriber():
    """
        消息订阅者
    """
    def __init__(self, queueName, bindingKey, config):
        self.queueName = queueName
        self.bindingKey = bindingKey
        self.config = config
        self.connection = create_connection(self.config)

    def __del__(self):
        self.connection.close()

    def on_message_callback(self,channel, method, properties, body):
        """
        :param channel:
        :param method:
        :param properties:
        :param body:
        """

        message = json.loads(body)
        print(" [received] %r : %r" % (method.routing_key, message))

    def setup(self):
        channel = self.connection.channel()
        # 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。
        # durable = True 代表exchange持久化存储，False 非持久化存储
        channel.exchange_declare(exchange=self.config['exchange'],
                                 exchange_type='topic',durable = True)
        channel.queue_declare(queue=self.queueName)
        channel.queue_bind(queue=self.queueName, exchange=self.config['exchange'], routing_key=self.bindingKey)
        channel.basic_consume(queue=self.queueName,
                              on_message_callback=self.on_message_callback, auto_ack=True)
        try:

            channel.start_consuming()
            print("启动起了了------")
        except KeyboardInterrupt:
            channel.stop_consuming()


class Publisher:
    """
        消息发布者
    """
    def __init__(self, config):
        self.config = config

    def publish(self, routing_key, message):
        """
        :param routing_key:
        :param message:
        """
        connection = create_connection(self.config)
        channel = connection.channel()
        # 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。
        # durable = True 代表exchange持久化存储，False 非持久化存储
        channel.exchange_declare(exchange=self.config['exchange'], exchange_type='topic')
        channel.basic_publish(exchange=self.config['exchange'], routing_key=routing_key, body=message)
        print("[x] Sent message %r for %r" % (message, routing_key))