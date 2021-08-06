import os

import pika


QUEUE_NAME = "scraping.data.log"


def create_connection(url: str) -> str:
    conn_params = pika.URLParameters(url)
    connection = pika.BlockingConnection(conn_params)
    return connection


def create_channel(conn: pika.BlockingConnection):
    channel = conn.channel()
    
    channel.exchange_declare(exchange='scraping.results.fx', exchange_type='fanout', durable=True)


    channel.queue_declare(queue=QUEUE_NAME)

    channel.queue_bind(exchange='scraping.results.fx', queue=QUEUE_NAME)

    return channel

def consume(cb):
    conn = create_connection(os.environ.get("CLOUDAMQP_URL"))
    channel = create_channel(conn)

    channel.basic_consume(
        queue=QUEUE_NAME,
        on_message_callback=cb,
        auto_ack=True
    )
    
    channel.start_consuming()