## Cheatsheet for Docker Commands

### Images:
- Images are read-only templates used to create containers.
- Images are created with the docker build command, either by us or by other docker users.
- Images are composed of layers of other images.
- Images are stored in a Docker registry.

### Containers:
- If an image is a class, then a container is an instance of a class - a runtime object.
- Containers are lightweight and portable encapsulations of an environment in which to run applications.
- Containers are created from images. Inside a container, it has all the binaries and dependencies needed to run the application.

### Registries and Repositories:
- A registry is where we store our images.
- You can host your own registry, or you can use Docker's public registry which is called DockerHub.
- Inside a registry, images are stored in repositories.
- Docker repository is a collection of different docker images with the same name, that have different tags, each tag usually represents a different version of the image.

### Basic Commands

**Login into remote repository:**
```sh
docker login
```

**Pull either from local repository or remote image repository and run it:**
```sh
docker run ngnix
```

**By default, tag considered as latest:**
```sh
docker run image_name/tag
```

**Just to download an image, it will not run:**
```sh
docker pull nginx
```

**Docker run starts the process in the container and attaches the console to the process's standard input, output, and standard error. Containers started in detached mode and exit when the root process used to run the container exits.**

**Pull either from local or remote and run it in a detached mode and will return the container_id:**
```sh
docker run -d ngnix
```

**It will again attach cmd to the docker container:**
```sh
docker attach container_id
```

**It will run ubuntu image and then run bash in interactive mode in the same command prompt. Here i means interactive and t means same terminal:**
```sh
docker run -it ubuntu bash
```

**Nginx on port 80 on docker internal network will be connected to externally port 5000. http://localhost:8080 or http://host-ip:8080 in your browser:**
```sh
docker run -p our_port/docker_internal_port -> docker run -p 5000:80 nginx
```

**Show the current docker running process:**
```sh
docker ps
```

**Example output:**
```sh
CONTAINER ID   IMAGE        COMMAND             CREATED         STATUS         PORTS                                       NAMES
2f11c8f2dc81   tomcat:9.0   "catalina.sh run"   2 minutes ago   Up 2 minutes   0.0.0.0:8888->8080/tcp, :::8888->8080/tcp   cool_heisenberg
```

**Execute a command in a running container:**
```sh
docker exec 2f11c8f2dc81 ps -eaf
```

**Example output:**
```sh
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  1 04:16 pts/0    00:00:03 /usr/local/openjdk-11/bin/java -Djava.util.logging.config.file=/usr/local/tomcat/conf/logging.properties -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -Djdk.tls.ephemeralDHKeySize=2048 -Djava.protocol.handler.pkgs=org.apache.catalina.webresources -Dorg.apache.catalina.security.SecurityListener.UMASK=0027 -Dignore.endorsed.dirs= -classpath /usr/local/tomcat/bin/bootstrap.jar:/usr/local/tomcat/bin/tomcat-juli.jar -Dcatalina.base=/usr/local/tomcat -Dcatalina.home=/usr/local/tomcat -Djava.io.tmpdir=/usr/local/tomcat/temp org.apache.catalina.startup.Bootstrap start
root        40     0  0 04:19 ?        00:00:00 ps -eaf
```

**Show all docker processes:**
```sh
docker ps -a
```

**To pause a running container:**
```sh
docker pause conainer_id 
```

**To stop a running a container/process:**
```sh
docker stop container_name/container_id
```

**Stops all the containers:**
```sh
docker stop $(docker ps -a -q)
```

**To remove a running container:**
```sh
docker rm container_name/container_id
```

**To show all available images and its size:**
```sh
docker images
```

**To delete an available image:**
```sh
docker rmi image_name
```

### About container specifications
**Container is meant to run a specific task like a server or a process. The container will be running as long as process inside in it will be in a living stage. So we can append a command into the process like this:**

**It will run ubuntu image and sleep for 10 sec. when 10 sec is completed then ubuntu will be stopped as it has no running process:**
```sh
docker run ubuntu sleep 10
```

**Check ubuntu version:**
```sh
docker run ubuntu cat /etc/"os-release"
```

**Run a command in a running container:**
```sh
docker exec
```

**This will create a new Bash session in the container ubuntu_bash:**
```sh
docker exec -it ubuntu_bash bash
```

**We can specify environment variable using --env:**
```sh
docker run --env MYSQL_ROOT_PASSWORD=100997 mysql
```

**We can volume mount using the -v flag. -v means it map docker internal directory to external file storage:**
```sh
docker run -v /opt/tempMysql:/var/lib/mysql --env MYSQL_ROOT_PASSWORD=100997 mysql
```

**To get more information about the container. We can see the environment variables using docker inspect container_name/id. Networks and all other things are there:**
```sh
docker inspect container_id/container_name
```

**To get logs for the container:**
```sh
docker logs container_id/container_name
```

**To give container a name and port:**
```sh
docker run -p 8080:8080 --name=jenkins-master -d jenkins/jenkins
```

**To take a snapshot of a running container:**
```sh
docker commit <container_name> <image_name>
```

### About images and volumes
**For deleting a single image:**
```sh
docker rmi image-name/tag-name
```

**For deleting an image forcefully (required when the a running container is still using the image):**
```sh
docker rmi -f image-name/tag-name
```

**To show all the layer details of the image:**
```sh
docker history <image_name>
```

**For deleting all images:**
```sh
docker image prune -a
```

**Docker uses the storage driver to do all volume and storage related things. Docker uses the different type of storage drivers.**

**To create docker volume. It will create a data_ volume folder under the volume directory of "var/lib/docker" directory:**
```sh
docker volume create data_volume
```

**This will mount the data_volume directory inside the docker:**
```sh
docker run -v data_volume:var/lib/mysql mysql:latest
```

**If we want to use external directory:**
```sh
docker run -v external_path:var/lib/mysql mysql:latest
docker run --mount type=bind,source=C:/Users/ghosh/OneDrive/Desktop/devops/data/mysql,target=/var/lib/mysql mysql
```

**For deleting all volumes:**
```sh
docker volume prune -a
```

### Image layers
**What is the image layers:**
1. To build a good image we must divide the docker file into different stages: 1. Base Image, 2. Working directory, 3. Build, 4. Run and Expose
2. In the first line of docker build docker sends the context to the docker daemon. We can reduce the context by adding dockerignore file.

**For reference: go to https://github.com/boot-services/metadata-service/tree/with-mongodb. Check docker files in this order:**
1.  Dockerfile
2.  Dockerfie.optimised.d
3.  Dockerfile.multistage.d
4.  Dockerfile.multistage.optimized.d

**CMD and ENTRYPOINT in docker:**
- If we see any dockerfile there we can find CMD, it defines the program that will be run when the container starts.
- For nginx image -> CMD["nginx"]

- Then there is another keyword ENTRYPOINT. Here can specify whatever program we want to start at the start of the container and if we add anything in the command line then it will be appended with the ENTRYPOINT. If we may have any default value, then we can pass that in CMD and if we specify more than one value then we must provide list of string on CMD or ENTRYPOINT.

- If we want to modify the ENTRYPOINT during runtime like sleep to sleep-v2 then we can do like this:
  - Previous version: docker run ubuntu-sleeper
  - New version: docker run --entrypoint sleep-v2 ubuntu-sleeper 20

**Ubuntu-sleeper image: it will start a ubuntu os and then start sleep process for 10 seconds:**
```sh
FROM UBUNTU					# Base image
ENTRYPOINT ["sleep"]		# Command on start
CMD ["10"]					# default value
```

### Docker is one of the implementations of the virtualization technology.
Before docker we have hypervisor. 

#### Following is the Hypervisor based architecture. Virtualization happens on physical layer.
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

#### Following is the Container based architecture is like. Virtualization happens on operating system layer. Docker client server architecture
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
**Single stage not optimized dockerfile:**
```sh
FROM openjdk:11-jre-slim
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","-Xms256m", "-Xmx512m","/app.jar"]
```

**Multi stage optimized dockerfile:**
```sh
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
```

**Maven has a shortcut to build spring boot image:**
```xml
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
```

**Build image by maven:**
```sh
mvn spring-boot:built-image
```

**Build image with skip test:**
```sh
mvn spring-boot:built-image -DskipTests
```

### Docker build and docker compose
**Build a docker image from Dockerfile:**
```sh
docker build -t repo_name/image_name:version dockerfile_location
docker build -t abhishek1009/arc-reactor-digital-test:1.0.0 .
```

**Build a docker image from Dockerfile with different name:**
```sh
docker build -t repo_name/image_name:version -f <Dockerfile_name> dockerfile_location
docker build -t abhishek1009/arc-reactor-digital-test:1.0.1 -f Dockerfile.optimized .
```

**If we do not use the docker compose then we have to run this following steps for running a set of microservices in local:**
```sh
docker build . -t voting-app
docker build . -t worker-app
docker build . -t result-app

docker run -d --name=redis redis
docker run -d -e POSTGRES_PASSWORD=10091997 --name=db postgres:9.4

docker run -p 5000:80 --link redis:redis voting-app
docker run -p 5001:80 --link db:db result-app
docker run --link redis:redis --link db:db worker-app
```

**Instead we can do this but we need docker-compose.yaml:**
```sh
docker-compose up --build with docker-compose.yml
```

## Links


### Youtube videos (docker, container runtime, containerd, kubernetes)
- [Using docker in unusual ways](https://www.youtube.com/watch?v=zfNqp85g5JM)
- [100+ Docker Concepts you Need to Know](https://www.youtube.com/watch?v=rIrNIzy6U_g)
- [you need to learn Docker RIGHT NOW!!](https://www.youtube.com/watch?v=eGz9DS-aIeY)
- [Docker networking is CRAZY!!](https://www.youtube.com/watch?v=bKFMS5C4CG0)
- [Understanding Docker Architecture](https://www.youtube.com/watch?v=4Qv1tb1bm1Q)
- [Docker Architecture | Docker components : daemon, containerd, containerd-shim, runc](https://www.youtube.com/watch?v=253o0hxwxm8)
- [Introduction to Docker for CTFs](https://www.youtube.com/watch?v=cPGZMt4cJ0I)
- [How Docker Works - Intro to Namespaces](https://www.youtube.com/watch?v=-YnMr1lj4Z8)
- [Deepdive Containers - Kernel Sources and nsenter](https://www.youtube.com/watch?v=sHp0Q3rvamk)
- [An introduction to cgroups, runc & containerD](https://www.youtube.com/watch?v=u1LeMndEk70)
- [Containers: cgroups, Linux kernel namespaces, ufs, Docker, and intro to Kubernetes pods](https://www.youtube.com/watch?v=el7768BNUPw)
- [What is a Container Runtime?](https://www.youtube.com/watch?v=DB0BH5N-gDY)
- [Containerd - An open and reliable container runtime (CNCFMinutes 18)](https://www.youtube.com/watch?v=AP630LvIs0o)
- [Docker vs Containerd: Understanding the Differences and Choosing the Right Containerization Tool](https://www.youtube.com/watch?v=21onkZfL2yM)
- [Podman vs. Docker](https://www.youtube.com/watch?v=Xx588nbshlM)
- [you should be using PODMAN](https://www.youtube.com/watch?v=0jhdCcAc8nM)
- [Effortless Docker Management with LazyDocker: A Terminal UI for Containers, Images and Networks!](https://www.youtube.com/watch?v=G955-w-BIQQ)

### Blogs
- **Medium blogs**
  - [Dockerfile cheat sheet](https://medium.com/@anjkeesari/dockerfile-cheat-sheet-1cb9e6eb1484)
  - [6 Tips to Optimize Your Dockerfile](https://aws.plainenglish.io/6-tips-to-optimize-your-dockerfile-40359a73ef8c)
  - [4 Docker Options You May Not Know](https://medium.com/syntaxerrorpub/4-docker-options-you-may-not-know-fef301a5ce03)
  - [Docker Basic Interview Questions — How Many Can You Answer?](https://blog.devgenius.io/docker-interview-questions-how-many-can-you-answer-173437bb8d35)
  - [DevOps in K8s — Write Dockerfile Efficiently](https://blog.devgenius.io/devops-in-k8s-write-dockerfile-efficiently-37eaedf87163)