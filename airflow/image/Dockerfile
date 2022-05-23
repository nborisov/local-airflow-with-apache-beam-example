FROM apache/airflow:2.3.0

USER root

# Install OpenJDK-11
RUN apt update && \
    apt install -y openjdk-11-jdk && \
    apt install -y ant && \
    apt clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

USER airflow