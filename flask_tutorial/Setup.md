#https://code.tutsplus.com/series/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-827
pip install flask
pip install flask-mysql

## Build webserver with app
docker build -t python_app_web ./PythonApp
docker build -t fat_debug ./Fat_Debug
      
## Build swarm
# docker swarm init
docker stack deploy -c Docker_Swarm/docker-compose.yml PythonApp
    
## Tear down
docker stack rm PythonApp

### Diagnostic
docker run -p 80:80 python_app_web
#### Logs
docker ps; printf "image ->"; read the_image; docker logs `docker ps|grep $the_image|cut -d' ' -f1`;unset the_image
#### Shell
docker ps; printf "image ->"; read the_image; docker exec -i -t `docker ps|grep $the_image|cut -d' ' -f1` /bin/bash;unset the_image
http://localhost:8080/
http://localhost:5002/


#Docker build
docker stack rm PythonApp; docker build -t python_app_web ./PythonApp;docker stack deploy -c Docker_Swarm/docker-compose.yml PythonApp
