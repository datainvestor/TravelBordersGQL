# Basic Flask app with Graphql
Flask api template with simple country model and graphql queries.

## Run for local development with docker:

Build the image:

`docker build --tag flask-docker-gql .`

Run it on mapped port 5000:

`docker run --env-file .env -p 5000:5000 flask-docker-gql`

Or pull the image from the dockerhub:

{{TODO}}

Alternatively just run the app locally:

`pip install -r requirements.txt`

`flask run`


## Create databse (*migrate*) as follows:

```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```



## Production
Run with gunicorn (For heroku deployment)

gunicorn api:app --bind 127.0.0.1:5057 -e POSTGRES_DB={{DATABASE LINK}}