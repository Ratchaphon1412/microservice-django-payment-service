# Django Payment Microservice

![Logo](https://github.com/CS211-651/project211-hardcodeexecutable/blob/featureUser/docs/image/Group%202.png)

## Acknowledgements

- Django Rest Framework
- Python OOP
- Django ORM
- Nginx
- Kafka
- Omise Payment
- Docker Compose
- Jenkins

## Roadmap

- Final Week
  - Create User Payment Register To Omise and Store Token in Database
  - Update User Payment When User Change Profile in Django Auth Service
  - Create Kafka Consumer Update Token Payment User (For Auth Service)
  - Create Kafka Producer Create Token Payment User (For Auth Service)
  - Create Credit Card User To Omise
  - Update Credit Card User To Omise
  - Delete Credit Card User To Omise
  - Get Credit Card User To Omise
  - Get Credit Card User To Omise By Id
  - Payment with Credit Card User By Token
  - Generate Invoice From (Laravel Product Service) and Store In Database
  - Get Invoice From Database
  - Get Balance Admin From Omise

## Third-party libraries

[Omise](https://github.com/omise/omise-python)

[kafka-python](https://github.com/dpkp/kafka-python)

[django-cors-headers](https://github.com/adamchainz/django-cors-headers)

[promptpay](https://github.com/jojoee/promptpay)

## Installation Program

## ENV

```bash
OMISE_PUBLIC_KEY= # Omise Public Key
OMISE_SECRETE= # Omise Secrete Key
OMISE_PUBLIC= # Omise Public Key
PROMPTPAY_PHONE= # Promptpay Phone Number
```

## use docker-compose development

```bash
git clone https://github.com/Ratchaphon1412/microservice-django-payment-service.git

cd microservice-django-payment-service

docker-compose up -d

```

### migrate database

```bash
docker-compose exec -it app-auth-server bash

poetry run python3 manage.py migrate
```

### Run Consumer Kafka Django Background

--topic payment --group auth in this project

```bash
docker-compose exec -it app-auth-server bash

poetry run python3 manage.py CommandConsumer --topic <topic_name>
--group <group_name>
```

## use docker-compose production

```bash
git clone https://github.com/Ratchaphon1412/microservice-django-auth-service.git

cd microservice-django-auth-service

docker-compose -f docker-compose.prod.yml up -d


```

# Architecture

```
.
|-- DjangoAuth (Cors Project Directory For Setting about Django)
    |-- __init__.py
    |-- asgi.py
    |-- settings.py
    |-- urls.py
    |-- wsgi.py
|-- Infrastructure (Directory For Contain Service In project )
    |-- __init__.py
    |-- kafka (Contain Kafka Service)
        |-- __init__.py
        |-- consumer.py (Contain Kafka Consumer)
        |-- producer.py (Contain Kafka Producer)
    |-- event (Contain Event Service Listening for Consumer Kafka)
        |-- interface
            |-- topicinterface.py (Contain Topic Interface)
        |-- listener
            |-- topic.py (Contain Topic Listener)
    |-- management
        |-- commands
            |-- __init__.py
            |-- CommandConsumer.py (Contain Command Consumer Thread)
    |-- service
        |-- factory (Contain Factory Design Pattern Service)
            |-- api.py (Contain API Method )
            |-- paymentFactory
                |-- bank.py (Contain Bank Service)
                |-- omisePayment.py (Contain Omise Service)
                |-- promptpay.py (Contain Promptpay Service)
        |-- interface
            |-- payment.py (Contain Payment Interface)
    |-- __init__.py
|-- Nginx
    |-- django.conf (Nginx Proxy Config File)
|-- media
    |-- qrcode (Contain QR Code Image that Generate From Promptpay)
|-- templates (Contain Template HTML)
    |-- auth
        |-- email_verification.html (Email Verification Template HTML)
|-- payment (Contain Payment App)
    |-- __init__.py
    |-- migrations (Contain Migration File Auto Generate By Django)
    |-- apps.py (Contain App Config)
    |-- models.py (Contain Model That Auto Generate Migration File)
    |-- serializers.py (Contain Serializer For Convert Request To JSON Or JSON To Response)
    |-- tests.py
    |-- urls.py (Contain URL Path)
    |-- views.py (Contain View For API)
|-- .env.example
|-- .gitignore
|-- dockerfile
|-- docker-compose.prod.yml
|-- docker-compose.yml
|-- manage.py
|-- poetry.lock
|-- pyproject.toml
|-- README.md
|-- Jenkinsfile
|-- setup.sh
```

# Features

## Authentication

- Register
- Login
- Logout
- Verify Email
- Update User
- Delete User
- Change Password
- Change Email
- Get Information User
- Get All User (For Admin)

## Address User

- Create User Address
- Update User Address
- Delete User Address
- Get User Address
- Get User Address By Id

## Infrastructures

- Kafka Consumer Update Token Payment User (For Payment Service)
- Kafka Producer Create Token Payment User (For Payment Service)
