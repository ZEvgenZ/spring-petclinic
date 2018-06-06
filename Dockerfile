FROM maven:3.5.3 AS mvn
WORKDIR /app
COPY . . 
RUN mvn package -Dmaven.test.skip=true
