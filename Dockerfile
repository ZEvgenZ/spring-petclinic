FROM maven:3.5.3 
RUN mvn package -Dmaven.test.skip=true