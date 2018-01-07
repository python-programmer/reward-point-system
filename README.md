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

## Projects Setup

### SSOServer

A Simple SSO server that handles Authentication and Authorization (JWT)

we need to create our tables in the database, to do that, run the following command:

```
$ python manage.py migrate
```

start the development server:

```
$ python manage.py runserver
```

finally running the Celery worker server(adding dynamic data to the order items in other services):
```
$ celery -A admin_tasks worker --loglevel=info
```

### Other Projects

The McDonald and the Uber Project is the same project with different name (for demonstration purposes only):

#### McDonald
postgres requirement: 

> user=python_user

> password=^uCd*r7-M$

> database=mcdonald_db

create the tables with:

```
$ python manage.py migrate
```

start the development server(port=8001):

```
$ python manage.py runserver 8001
```

finally running the Celery worker server(adding dynamic data to the order items in other services):
the celery worker just handles tasks in the **mcdonald queue**
```
$ celery -A mcdonald_tasks worker --loglevel=info -Q mcdonald
```

#### Uber
postgres requirement: 

> user=python_user

> password=^uCd*r7-M$

> database=uber_db

create the tables with:

```
$ python manage.py migrate
```

start the development server(port=8002):

```
$ python manage.py runserver 8002
```

finally running the Celery worker server(adding dynamic data to the order items in other services):
the celery worker just handles tasks in the **uber queue**
```
$ celery -A uber_tasks worker --loglevel=info -Q uber
```

