# gendermeme-docker
This repository forks [gendermeme-core](https://github.com/poorna-kumar/gendermeme-core) and attempts the following:
- Adds a simple python server which responds to http GET requests on port 5000
  - Given a `text` parameter, will run `annotate_corenlp` and respond with its results
- Dockerize this application so it can be deployed to a Kubernetes cluster

## Pre-requisites
This application expects a Stanford Core NLP v3.8.0 server running on port 9000. 
- Pull a [dockerized Stanford Core NLP server container](https://github.com/joeybones/corenlp-docker) from docker hub
```
docker pull joeybones/stanford_corenlp
```
- Run the container on port 9000
```
docker run -p 9000:9000 joeybones/stanford_corenlp
```
  
## Running this application
Kick off `server.py`. By default this will run a web server on 5000 of your host machine.
```
python server.py
```

Visit `http://localhost:5000?text=[text to run through gendermeme]` in your web browser. 
