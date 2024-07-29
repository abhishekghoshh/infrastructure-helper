## Cheetsheet for docker commands

### Images:
- Images are read only templates used to create containers.
- Images are created with the docker build command, either by us or by other docker users.
- Images are composed of layers of other images.
- Images are stored in a Docker registry.

### Containers:
- If an image is a class, then a container is an instance of a class - a runtime object.
- Containers are lightweight and portable encapsulations of an environment in which to run applications.
- Containers are created from images. Inside a container, it has all the binaries and dependencies needed to run the application.

### Registries and Repositories:
- A registry is where we store our images.
- You can host your own registry, or you can use Docker’s public registry which is called DockerHub.
- Inside a registry, images are stored in repositories.
- Docker repository is a collection of different docker images with the same name, that have different tags, each tag usually represents a different version of the image.

### basics commands
```
# Docker CLI + Rest API + Docker Deamon => Docker Engine

# login into remote repository
docker login

# pull either from local repository or remote image repository and run it.
docker run ngnix

# by deafult tag considered as latest 
docker run image_name/tag

# just to download an image, it will not run
docker pull nginx

# Docker run starts the process in the container and attaches the console to the process’s standard input, output, and standard error.
# Containers started in detached mode and exit when the root process used to run the container exits.

# pull either from local or remote and run it in a deattached mode and will return the container_id
docker run -d ngnix

# it will again attach cmd to the docker container
docker attach container_id

# it will run ubuntu image and then run bash in interactive mode in the same command prompt
# here i mean interactive and t means same terminal
docker run -it ubuntu bash

# nginx on port 80 on docker internal network will be connected to externally port 5000
# http://localhost:8080 or http://host-ip:8080 in your browser
docker run -p our_port/docker_internal_port -> docker run -p 5000:80 nginx

# show the current docker running process
docker ps

CONTAINER ID   IMAGE        COMMAND             CREATED         STATUS         PORTS                                       NAMES
2f11c8f2dc81   tomcat:9.0   "catalina.sh run"   2 minutes ago   Up 2 minutes   0.0.0.0:8888->8080/tcp, :::8888->8080/tcp   cool_heisenberg

docker exec 2f11c8f2dc81 ps -eaf
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  1 04:16 pts/0    00:00:03 /usr/local/openjdk-11/bin/java -Djava.util.logging.config.file=/usr/local/tomcat/conf/logging.properties -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -Djdk.tls.ephemeralDHKeySize=2048 -Djava.protocol.handler.pkgs=org.apache.catalina.webresources -Dorg.apache.catalina.security.SecurityListener.UMASK=0027 -Dignore.endorsed.dirs= -classpath /usr/local/tomcat/bin/bootstrap.jar:/usr/local/tomcat/bin/tomcat-juli.jar -Dcatalina.base=/usr/local/tomcat -Dcatalina.home=/usr/local/tomcat -Djava.io.tmpdir=/usr/local/tomcat/temp org.apache.catalina.startup.Bootstrap start
root        40     0  0 04:19 ?        00:00:00 ps -eaf

# show all docker processes
docker ps -a

# To pause a running container
docker pause conainer_id 

# to stop a running a container/process
docker stop container_name/container_id

# Stops all the containers
docker stop $(docker ps -a -q)

# to remove a running container
docker rm container_name/container_id

# to show all available images and its size
docker images

# to delete an available image
docker rmi image_name
```

### About container specifications
```
# container is meant to run a specific task like a server or a process. 
# the container will be running as long as process inside in it will be in a living stage.
# So we can append a command into the process like this

# it will run ubuntu image and sleep for 10 sec. when 10 sec is completed then ubuntu will be stopped as it has no running process
docker run ubuntu sleep 10

# check ubuntu version
docker run ubuntu cat /etc/"os-release"

# Run a command in a running container
docker exec

# This will create a new Bash session in the container ubuntu_bash.
docker exec -it ubuntu_bash bash

# we can specify environment variable using --env
docker run --env MYSQL_ROOT_PASSWORD=100997 mysql

# we can volume mount using the -v flag
# -v means it map docker internal directory to external file storage
docker run -v /opt/tempMysql:/var/lib/mysql --env MYSQL_ROOT_PASSWORD=100997 mysql

# to get more information about the container
# We can see the environment variables using docker inspect container_name/id
# networks and all other things are there
docker inspect container_id/container_name

# to get logs for the container
docker logs container_id/container_name

# to give conatiner a name and port
docker run -p 8080:8080 --name=jenkins-master -d jenkins/jenkins

# to take a snapshot of a running container
docker commit <container_name> <image_name>

```

### About images and volumes
```
# for deleting a single image
docker rmi image-name/tag-name

# for deleting an image forcefully (required when the a running container is still using the image)
docker rmi -f image-name/tag-name

# to show all the layer details of the image
docker history <image_name>

# for deleting all images
docker image prune -a

# docker uses the storage driver to do all volume and storage related things
# docker uses the different type of storge drivers

# to create docker volume
# it will create a data_ volume folder under the volume directory of "var/lib/docker" directory
docker volume create data_volume

# this will mount the data_volume directory inside the docker 
docker run -v data_volume:var/lib/mysql mysql:latest

# if we want to use external directory
docker run -v external_path:var/lib/mysql mysql:latest
docker run --mount type=bind,source=C:/Users/ghosh/OneDrive/Desktop/devops/data/mysql,target=/var/lib/mysql mysql

# for deleting all volumes
docker volume prune -a
```

### Image layers
```
# what is the image layers
1. To build a good image we must divide the docker file into different stages: 1. Base Image, 2. Working directory, 3. Build, 4. Run and Expose
2. In the first line of docker build docker sends the context to the docker daemon. We can reduce the context by adding dockerignore file.

For reference: go to https://github.com/boot-services/metadata-service/tree/with-mongodb
Check docker files in this order ->
1.  Dockerfile
2.  Dockerfie.optimised.d
3.  Dockerfile.multistage.d
4.  Dockerfile.multistage.optimized.d

# CMD and ENTRYPOINT in docker:
# If we see any dockerfile there we can find CMD, it defines the program that will be run when the container starts.
# For nginx image -> CMD[“nginx”]

# Then there is another keyword ENTRYPOINT. Here can specify whatever program we want to start at the start of the container 
# and if we add anything in the command line then it will be appended with the ENTRYPOINT. 
# If we may have any default value, then we can pass that in CMD and if we specify more than one value 
# then we must provide list of string on CMD or ENTRYPOINT.

# If we want to modify the ENTRYPOINT during runtime like sleep to sleep-v2 then we can do like this:
Previous version: docker run ubuntu-sleeper
New version: docker run --entrypoint sleep-v2 ubuntu-sleeper 20

# Ubuntu-sleeper image: it will start a ubuntu os and then start sleep process for 10 seconds
FROM UBUNTU					# Base image
ENTRYPOINT [“sleep”]		# Command on start
CMD [“10”]					# default value

```

### Docker is one of the implementations of the virtualization technology.
Before docker we have hypervisor. 

#### following is the Hypervisor based architecture. Virtualization happens on physical layer.
- Physical layer
- Host operating system
- Hyepervisor (VMware, Virtual Box)
    - Guest OS
    - Binaries/libraries
    - Applications

#### Benefits
- Cost efficient
- Easy to scale

#### Limitations:
- Kernal Resource Duplication
- Application portability issue
- Runtime isolation. (like running JRE 7 and JRE8 in same system)



#### following is the Container based architecture is like. Virtualization happens on operating system layer. Docker client server architecture
- Physical layer
- Host operating system
- Container Engine
    - Binaries/libraries
    - Applications

#### Benefits
- Cost efficient
- Fast time for boot up and deployment.
- Portability 





### Sample docker files
```
# Single stage not optimized dockerfile

FROM openjdk:11-jre-slim
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","-Xms256m", "-Xmx512m","/app.jar"]



# Multi stage optimized dockerfile

# ===========   BUILD STAGE =====================
FROM maven AS build
WORKDIR /workspace/app

# build maven .m2 cache as layer for reuse
COPY pom.xml pom.xml
RUN mvn dependency:go-offline -B

# build application as fat executable JAR
COPY src src
RUN mvn package -DskipTests
# explod fat executable JAR for COPY in RUN stage
RUN mkdir -p target/dependency && (cd target/dependency; jar -xf ../*.jar)


# =========== RUN STAGE =====================
#FROM openjdk:alpine
FROM openjdk:11-jre-slim
VOLUME /tmp
ARG DEPENDENCY=/workspace/app/target/dependency
COPY --from=build ${DEPENDENCY}/BOOT-INF/lib /app/lib
COPY --from=build ${DEPENDENCY}/META-INF /app/META-INF
COPY --from=build ${DEPENDENCY}/BOOT-INF/classes /app
EXPOSE 8080
ENTRYPOINT ["java","-cp","app:app/lib/*","com.github.typicalitguy.DigitalLayerApplication"]


# Maven has a shortcut to build spring boot image 

<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.6.7</version>
		<relativePath /> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.github.typicalitguy</groupId>
	<artifactId>ARC_REACTOR_DIGITAL</artifactId>
	<version>1.0.0</version>
	<name>ARC_REACTOR_DIGITAL</name>
	<description>Digital layer ARC_REACTOR Microservice</description>
	<properties>
		<java.version>11</java.version>
		<spring-cloud.version>2021.0.1</spring-cloud.version>
	</properties>
	...
<build>
	 <plugins>
	  <plugin>
	   <groupId>org.springframework.boot</groupId>
	   <artifactId>spring-boot-maven-plugin</artifactId>
	   <configuration>
	    <image>
	     <name>abhishek1009/${project.artifactId}:${project.version}</name>
	    </image>
	    <pullPolicy>IF_NOT_PRESENT</pullPolicy>
	   </configuration>
	  </plugin>
        </plugins>
	</build>
</project>

# Build image by maven
mvn spring-boot:built-image

# Build image with skip test 
mvn spring-boot:built-image -DskipTests
```

### docker build and docker compose
```
# build a docker image from Dockerfile
docker build -t repo_name/image_name:version dockerfile_location
docker build -t abhishek1009/arc-reactor-digital-test:1.0.0 .

# build a docker image from Dockerfile with different name
docker build -t repo_name/image_name:version -f <Dockerfile_name> dockerfile_location
docker build -t abhishek1009/arc-reactor-digital-test:1.0.1 -f Dockerfile.optimized .

# if we do not use the docker compose then we have to run this following steps for 
# running a set of microservices in local

docker build . -t voting-app
docker build . -t worker-app
docker build . -t result-app

docker run -d --name=redis redis
docker run -d -e POSTGRES_PASSWORD=10091997 --name=db postgres:9.4

docker run -p 5000:80 --link redis:redis voting-app
docker run -p 5001:80 --link db:db result-app
docker run --link redis:redis --link db:db worker-app


# instead we can do this but we need docker-compose.yaml
docker-compose up --build with docker-compose.yml
```
