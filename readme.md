# Running on docker #

## Requirements ##

- docker
- docker-compose

## Steps ##

Run with cli `docker-compose up -d` on the root of the project.

For create the DB run on cli `docker exec -it contact_test_backend-api_1 flask db upgrade`

Open [http://localhost/](http://localhost/)

To see api documentation open [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

To stop the running app run with cli on the root of the project `docker-compose down` to delete the containers or `docker-compose stop` to stop them without deleting them.

## Troubleshooting ##

The ports needed (5000, 80) can be allocated by other app. Stop the other app until you finish test this app
