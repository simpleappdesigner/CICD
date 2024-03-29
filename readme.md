 ### <font color=red> Dependencies </font>
dockers installed , reference - https://docs.docker.com/guides/get-started/

### Python env
- `python -m venv venv` # create a virtual environment with name `venv`
- `source venv/bin/activate` # activate the virtual environment(mac), if are in other os [reference](https://docs.python.org/3/library/venv.html) 
-  `pip install Flask`
- `pip freeze > requirements.txt` # write dependencies to a file
### Hello world flask
create a hello world app in flask. refer main.py

### Dockerfile
go to docker hub and find python [docker_hub_python](https://hub.docker.com/_/python/tags)
select the right tag, selected ~~`3.13.0a4-alpine3.19`~~ python:3.10.13-alpine3.19
> before running build, make sure docker desktop is running

- run `docker build -t docker-flask .` # file with name Dockerfile and at current directory
    - or `docker build --no-cache -t docker-flask .  ` # for no cache
- `docker images` # return images , and will show docker-flask
- `docker run -d -p 5002:5001 --name my_name_for_docker_flask docker-flask:latest` # host_port:container_port
> flask is running at 5001 refer Dockerfile  `CMD ["flask" ,"--app" ,"main" ,"run", "--host","0.0.0.0", "--port","5001"]`, and its been mapped to 5002, so in browser access will be at 5002 - http://127.0.0.1:5002/

-----------------
interactive shell
- `docker run -it  -p 5002:5001 --name my_name_for_docker_flask docker-flask:latest sh`
- /app # `flask --app main run --host 0.0.0.0 --port 5001`
- on browser access `http://127.0.0.1:5002/`


### Other most frequent commands
- stop running container --> `docker stop my_name_for_docker_flask`
- remove --> `docker rm my_name_for_docker_flask`
- execute from shell - `docker run -it  -p 5002:5001 --name my_name_for_docker_flask docker-flask:latest sh`
-  list container(active) `docker ps -a`
![Alt text](image-3.png)
- show images `docker images`
![Alt text](image-1.png)

quick snap of executed commands:
![Alt text](image-3.png)

### <font color=red>Note</font>
- when access the end point, for example `http://127.0.0.1:5002/` and page not displayed or gives impression that container site is un accessible, look for the below error - "Segmentation fault", python crashed, most likly the issue is with container image. 
![Alt text](image-2.png)


## Part 2
#### Mapping the "Runlog" folder inside the container to the "Runlog" folder on the host machine.
- build again `docker build -t docker-flask .`
- run interactive `docker run -it -p 5002:5001 --name my_name_for_docker_flask docker-flask:latest sh` and when run ls, see **Runlog** folder
![Alt text](image-4.png)
- run `docker run -d -p 5002:5001 -v $(pwd)/Runlog:/app/Runlog --name my_name_for_docker_flask docker-flask:latest`
![Alt text](image-6.png)
log file from Host:![Alt text](image-7.png)


--------
## flask server - building with custom file
1. build a image on custome dockerfile with name `docker build -f Dockerfile_flaskserver -t image-name:flask-server .` or `docker build -f Dockerfile_flaskserver -t flask_server:v1.0 .` with version
2. 
```
docker image ls                                                    
REPOSITORY     TAG            IMAGE ID       CREATED              SIZE
image-name     flask-server   b397b49e93f1   About a minute ago   61.9MB
docker-flask   latest         4b2e9013b1fa   2 weeks ago          61.8MB
```
```
flask_server   v1.0      b397b49e93f1   7 minutes ago   61.9MB
docker-flask   latest    4b2e9013b1fa   2 weeks ago     61.8MB
```
3. optional: remove image `docker rmi b397b49e93f1`
4. interactive `docker run -it -p 5002:5001 94f0bc38ea60 sh` and then navigate to folder - 
```
docker run -it -p 5002:5001 94f0bc38ea60 sh
/app # ls
Runlog            flask_server      requirements.txt
/app # python flask_server/main.py 
```
or run so flask log can be viewed at screen
```
docker run -it -p 5002:5001  6f7fb359d00b
```

-----
1.create docker-compose yml
2. run `docker-compose up`
3. all down `docker-compose down`


