# Reward/Point system with Microservices in Python
Simple Microservices with django rest framework, Celery and RabbitMQ

## Requirements
* [Python 3.4+](https://www.python.org/downloads/release/python-2712/)
* [Django 1.8+](https://docs.djangoproject.com/en/1.8/)
* [Django-REST-Framework 3.0+](http://www.django-rest-framework.org/)
* [RabbitMQ 3.6+](https://www.rabbitmq.com/)
* [Celery](http://www.celeryproject.org/)
* [Redis](https://redis.io/)
* [Django-REST-Framework-JWT](https://getblimp.github.io/django-rest-framework-jwt/)

## Installation

### RabbitMQ
Install RabbitMQ via the this [link](https://www.rabbitmq.com/download.html)

please refer to the installation instructions for your specific platform

and Get RabbitMQ running in the background with:

```
$ sudo rabbitmq-server
```

### Redis
Install Redis via the this [link](https://redis.io/download)

Run the Redis server from a new terminal window:

```
$ redis-server
```

### Project Requirements

Create a new virtualenv:

```
$ virtualenv reward_env
$ source reward_env/bin/activate
```

In the root directory of the project, run below command in the terminal:

```
pip install -r requirements.txt
```
