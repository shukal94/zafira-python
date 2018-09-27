import pika


class RabbitMQService:
    """
    Service that provides a message sending from zafira-client to server
    """
    def __init__(self, host='localhost', port=5672, username='qpsdemo', password='qpsdemo'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.virtual_host = '/'
        self.exchange = 'logs'
        self.type = 'x-recent-history'
        self.routing_key = ''
        self.history = 1000
        self.queue = None
        self.con = None

    def connect(self):
        creds = pika.PlainCredentials(username=self.username, password=self.password)
        params =  pika.ConnectionParameters(host=self.host, port=self.port, credentials=creds)
        if not self.con:
            con = pika.BlockingConnection(params)
            if not con:
                raise Exception
            self.con = con

    def send_message(self, message_body):
        channel = self.con.channel()
        channel.exchange_declare(exchange=self.exchange, exchange_type=self.type)
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange=self.exchange,
                              routing_key='hello',
                              body=message_body)
        return 'Sent ' + message_body

    def close_con(self):
        self.con.close()


if __name__ == '__main__':
    rmqs = RabbitMQService()
    rmqs.connect()
    print(rmqs.send_message('HELLOOOOO'))
    rmqs.close_con()

