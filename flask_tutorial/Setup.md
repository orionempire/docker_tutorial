#https://code.tutsplus.com/series/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-827



## Build webserver with app
    docker build -t python_app_web .
      
### Diagnostic
    docker run -p 4000:80 python_app_web
    docker exec -i -t <ID> /bin/bash
    curl http://localhost:4000/
    docker stop <CONTAINER ID >    


## Build swarm
    # docker swarm init
    docker stack deploy -c docker-compose.yml PythonApp
    http://localhost:8080/
    http://localhost:4000/
    
## Tear down
    docker stack rm PythonApp
