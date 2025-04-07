## Sample Github action files

Github action is pretty easy, if we see some couple of action files most of our confusion will be clear




### Push to Docker-hub action

```yaml
## See this video for refference : https://www.youtube.com/watch?v=x7f9x30W_dI


# This workflow builds and pushes a Docker image to Docker Hub
name: Build and Push Docker Image

# Controls when the action will run. Triggers the workflow on push or pull request
# events but only for the main branch
on:
  push:
    branches: ["main", "master"]
  pull_request:
    branches: ["main", "master"]

jobs:
  publish_images:
    runs-on: ubuntu-latest
    steps:
      - name: checkout
        uses: actions/checkout@v4
      - name: build image
        run: |
          docker build -t '${{ secrets.DOCKER_USERNAME }}/${{ github.event.repository.name }}:latest'
      - name: push image to docker hub
        run: |
          docker login -u ${{ secrets.DOCKER_USERNAME }} -p ${{ secrets.DOCKER_HUB_TOKEN }}
          docker push '${{ secrets.DOCKER_USERNAME }}/${{ github.event.repository.name }}:latest'
```


### Push to Docker-hub action but in different way

```yaml
# This workflow builds and pushes a Docker image to Docker Hub
name: Build and Push Docker Image

# Controls when the action will run. Triggers the workflow on push or pull request
# events but only for the main branch
on:
  push:
    branches: ["main", "master"]
  pull_request:
    branches: ["main", "master"]


jobs:
  publish_images:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: '${{ secrets.DOCKER_USERNAME }}'
          password: '${{ secrets.DOCKER_PASSWORD }}'
      - name: Set up QEMU
        uses: docker/setup-qemu-action@v3
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      - name: Build and push Docker image
        uses: docker/build-push-action@v6
        with: 
        # We could also use Docker CLI token here so that we don't have store the dockerhub password in secrets
        # We could skip the docker login option, directly use docker 
          context: .
          tags: '${{ secrets.DOCKER_USERNAME }}/${{ github.event.repository.name }}:latest'
          push: true
```


### Java Maven Build


```yaml
name: project cicd flow

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
    - name: Set up JDK 1.8
      uses: actions/setup-java@v1
      with:
        java-version: '1.8'
        distribution: 'adopt'
        cache: maven
    - name: Build with Maven
      run: mvn clean install
```

### Java Maven Build & Publish Artifact


```yaml
name: Java Maven Build & Publish Artifact

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build_and_publish:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
    - name: Set up JDK 17
      uses: actions/setup-java@v3
      with:
        java-version: '17'
        distribution: 'temurin'
        cache: maven
    - name: Build with Maven
      run: mvn -B package --file pom.xml
    - name: Verify and publish
      run: |
        mvn --batch-mode --update-snapshots verify
        mkdir staging && cp target/*.jar staging
    - uses: actions/upload-artifact@v3
      with:
        name: Package
        path: staging
```