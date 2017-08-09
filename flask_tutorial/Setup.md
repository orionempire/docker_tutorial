#https://code.tutsplus.com/series/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-827

## Build webserver with app
    docker build -t python_app_web .
      
## Build swarm
    # docker swarm init
    cd flask_tutorial/Docker_Swarm
    docker stack deploy -c docker-compose.yml PythonApp
    http://localhost:8080/
    http://localhost:4000/
    
## Tear down
    docker stack rm PythonApp

### Diagnostic
# mysql 
# python_app_web
docker run -p 80:80 python_app_web
printf "image ->"; read the_image; docker logs `docker ps|grep $the_image|cut -d' ' -f1`;unset the_image
printf "image ->"; read the_image; docker exec -i -t `docker ps|grep $the_image|cut -d' ' -f1` /bin/bash;unset the_image
docker logs `docker ps|grep python_app_web|cut -d' ' -f1`
docker logs `docker ps|grep python_app_web|cut -d' ' -f1`

curl http://localhost:5002/
docker stop <CONTAINER ID >  
 