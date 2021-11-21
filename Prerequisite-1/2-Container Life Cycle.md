## Container Life Cycle



#### Pull BusyBox Image
```bash
$ docker search busybox
$ docker pull busybox
$ docker images
$ 
```

#### Run BusyBox
```bash
$ docker run busybox
$ docker run busybox
$ docker ps
$ docker ps -a
$ docker run busybox echo "Hi "
$ docker ps -a
$ docker container prune
$ docker ps -a

```

#### Run Docker - Interactive Terminal Mode
```bash
$ docker run -it busybox
$	ls
$ 	ls -lh /bin
$ 	cd /bin
$	exit
$ docker ps -a 
$ docker rm <CONTAINER_ID_1> <CONTAINER_ID_2> 
$ docker rm $(docker ps -a -q -f status=exited)

```

#### Detach from /Attach to a Running Container
```bash
$ docker run -it busybox
$	cd bin/
$	ctrl+p+q  # detach from a running container
$ docker ps
$ docker ps # Status Updates
$ docker run -it -d busybox
$ docker ps
$ docker attach <CONTAINER_ID_1>   # consider current directory!
$   pwd
$ 	ctrl+p+q
$ docker attach <CONTAINER_ID_2>   # consider current directory!
$   pwd
$ 	ctrl+p+q


```



#### Pause/UnPause Containers

```bash
$ docker pause  <CONTAINER_ID_1>   
$ docker ps
$ docker attach <CONTAINER_ID_1> # Error!
$ docker unpause <CONTAINER_ID_1>
$ docker ps
```



#### Stop/Start/Restart a Container

```bash
$ docker stop  <CONTAINER_ID_1>   
$ docker ps
$ docker start <CONTAINER_ID_1>   
$ docker attach <CONTAINER_NAME_1> 
$	pwd
$	cd /dev
$ 	ctrl+p+q
$ docker unpause <CONTAINER_ID_1>
$ docker ps
```



#### Kill/Remove a Container

```bash
$ docker rm <CONTAINER_ID_1> #Error
#Option #1
$ 	docker stop <CONTAINER_ID_1> 
$	docker rm  <CONTAINER_ID_1>
# Option 2
$ 	docker rm -f <CONTAINER_ID_2>
# Option 3
$ docker kill <CONTAINER_ID_1>
$ docker rm  <CONTAINER_ID_1>
$

```



#### Commit Changes 

```bash
$ docker  run -it busybox 
$ / # mkdir test
$ / # cd test
$/test # touch t1.txt
$/test # touch t2.txt
$/test # ls > t3.txt
$/test # cat t3.txt
$ exit
$ docker commit -a mojtaba -m 'Making Test Directory' test newbusybox:1.0
$ docker images
$ docker history newbusybox:1.0
$ docker run -it newbusybox #Error
$ docker run -it newbusybox:1.0
$ 	cd test
$	ls 
$ 	exit
$ docker push newbusybox:1.0 # Error --> [docker.io/library/newbusybox]
$ docker tag newbusybox:1.0 smbanaie/newbusybox:1.0 # --> Access Denied :  [docker.io/smbanaie/newbusybox]
$ docker login # User name & Password
$ docker push smbanaie/newbusybox:1.0
$ # Visit: https://hub.docker.com/repository/docker/smbanaie/newbusybox
```

#### Volumes 

#####  Option #1 : Using Explicit Mount Points 

```bash 
$ mkdir busybox_volume
$ cd  busybox_volume
$ docker run -it -v  ${PWD}:/data busybox 
$ 	cd  data
$	touch t1.txt
$	touch t2.txt
$   ls > t3.txt
$ exit
$ docker container prune
$ ### Check Current Directory and you can find these files!
$ docker run -it -v  ${PWD}:/data -v d:/data:/data2 busybox
$ 
```

##### Option #2 : Using Named Volumes

```bash 
$ docker volume create data
$ docker volume ls
$ docker run -it --mount source=data,destination=/data  busybox  
$ 	cd  data
$	touch t1.txt
$	touch t2.txt
$   ls > t3.txt
$ exit
$ docker container prune
$ ### Check Current Directory and you can find these files!
$ docker run -it --mount source=data,destination=/data  busybox  
$ cd data
$ ls -lh
$ docker volume inspect data
$ # Check This Address in Windows: \\wsl$\docker-desktop-data\version-pack-data\community\docker\volumes\

```

#### Port Forwarding

```bash
$ docker run -it -d -p 9000:80 busybox 
$ docker ps # 0.0.0.0:9000->80/tcp 
$ # localhost:9000 --> container:80

```



#### Fetching (STDOUT)Logs from the Container

Syntax : docker logs {container_name_or_container_id}

```bash
$ docker run -it -d  busybox 
$   for i in $(seq 1 1000); do
$	> echo $i
$	> sleep 2
$	> done;
$   ctrl+p+q
$ docker logs <Containr_ID> # Ctrl+C to Quit
$ docker logs -f web_1
```



#### Containers’ resource usage statistics

```bash
$ docker stats
$ docker stats --no-stream
$ docker top web_1

```

#### Display Container IP address

```bash
$ docker inspect web_container | grep IPAddress | cut -d '"' -f 4
```

#### Execute a Command in a Container

```bash
$ docekr exec -it -u 0 <ContainerId> sh
```

