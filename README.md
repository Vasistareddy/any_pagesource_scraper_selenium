# docker_selenium_pagesource_flask
Extract pagesource/html through selenium webdriver with get request of Flask API

# guide for the docker installation @digitalocean
	- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

# Build the docker

docker build . -t selenium:pagesource


# Run the docker

docker run -p 5056:5056 --env DISPLAY=:10 -d selenium:pagesource


# endpoint

## - pagesource

# querystrings

## params:
	- url <required>
## response:
	200:
	- status_code: 200
	- pageSource: <response of the url>
	500:
	- status_code: 500
	- erro: error message

Ex: http://localhost:5056/pagesource?url=http://vasistareddy.blogspot.com/