# Contact Management System - Frontend
This is the backend component of the [Contact Management System](https://github.com/contact-mgmt-sys). It exposes a REST API for the [frontend](https://github.com/contact-mgmt-sys/contact-mgmt-sys-fe) to consume.

## Technologies
* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)

## Requirements
### Required
* [Python](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/)
### Optional
* [Git](https://git-scm.com/downloads)

## Setup
1. Download and extract the repository or clone it if [git is present](#optional).
```
git clone https://github.com/contact-mgmt-sys/contact-mgmt-sys-be.git
```
2. Install the dependencies.
```
pip install -r requirements.txt
```
3. Create an `.env` file in the root directory and add the following environment variables. The following values are examples and should be changed to match your environment.
```env
DATABASE_NAME="contact_mgmt_sys"
DATABASE_USER="postgres"
DATABASE_PASSWORD="postgres"
DATABASE_HOST="127.0.0.1"
DATABASE_PORT="5432"
```

## Usage
* Starting the server.
```
python manage.py runserver
```
* The API exposes the following endpoints.

| Method   | Endpoint                          | Description                                          |
|----------|-----------------------------------|------------------------------------------------------|
| `GET`    | `<host>/contacts/`                | Gets all the contacts                                |
| `GET`    | `<host>/contacts/?search=<query>` | Gets all the contacts that match the query           |
| `POST`   | `<host>/contacts/`                | Creates a new contact                                |
| `GET`    | `<host>/contacts/<id>/`           | Gets the details for the contact with matching id    |
| `PUT`    | `<host>/contacts/<id>/`           | Updates the details for the contact with matching id |
| `DELETE` | `<host>/contacts/<id>/`           | Deletes the contact with matching id                 |

## Docker
1. Create a network.
```
docker network create contact-mgmt-sys
```
2. Build the image.
```
docker build -t contact-mgmt-sys-fe .
```
3. Run the container.
```
docker run -p 8080:8080 contact-mgmt-sys-fe
```