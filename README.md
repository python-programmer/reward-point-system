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

## API
For every operation, you need a token

first of all you must register a user


### SSO API

**SignUp**

http://127.0.0.1:8000/sign-up

Method: POST

data: {

  'username': 'any-name',
  
  'password': 'password'
  
}

-------

**SignIn**

get a token

http://127.0.0.1:8000/api-token-auth

Method: POST

data: {

  'username': 'any-name',
  
  'password': 'password'
  
}

-------

**Get All Valid Clients**

uber or mcdonald

http://127.0.0.1:8000/clients/

Method: GET

Authorization: JWT _token_

-------

**Add or Update order items attributes(Admin panel)**

add or update order items attribute in other services(uber or mcdonald)

http://127.0.0.1:8000/clients/

Method: POST

Authorization: JWT _token_
  
data: {

  client: uber|mcdonald,
  
  key1: value1,
  
  key2: value2,
  
  ...
  
}

-------
  
### Other services

**Post data to a service**

http://127.0.0.1:8002/api/orders/

Method: POST

Authorization: JWT _token_
  
data:{

  key1: value1,
  
  key2: value2,
  
  key3: value3,
  
  ...
  
}

-------

**Update a record**

http://127.0.0.1:8002/api/orders/

Method: PUT

Authorization: JWT _token_
  
data:{

  key1: value1,
  
  key2: value2,
  
  key3: value3,
  
  ...
  
}
  
-------
  
**Delete a record**

http://127.0.0.1:8002/api/orders/id

Method: DELETE

Authorization: JWT _token_

-------
 
**Get a record**

http://127.0.0.1:8002/api/orders/id

Method: GET

Authorization: JWT _token_

-------
  
## Throttling

Each user can only do 5 unsafe method operation(Add, Edit, Delete)  per minute

## Logging all transactions

All transactions are logged
