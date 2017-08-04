#https://code.tutsplus.com/series/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-827
docker-machine create --driver virtualbox myvm1
docker-machine ls
docker-machine ssh myvm1 "docker swarm init --advertise-addr 192.168.99.100:2377"
#build webserver with app
docker build -t python_app_web .
#publish app
#?docker login
docker tag python_app_web orionempire/python_app_web:latest
docker push orionempire/python_app_web:latest
#Build swarm
docker-machine scp docker-compose.yml myvm1:~
docker-machine ssh myvm1 "docker stack deploy -c docker-compose.yml PythonApp"
docker-machine ls
http://192.168.99.100:8080/``
http://192.168.99.100/
