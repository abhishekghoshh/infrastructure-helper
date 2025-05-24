FROM jenkins/jenkins

USER root

RUN apt-get update && apt-get install -y docker.io

# Add a user 'admin' with password 'password' and add it to the root group
RUN useradd -m -s /bin/bash admin && \
    echo "admin:password" | chpasswd && \
    usermod -aG root admin

USER jenkins