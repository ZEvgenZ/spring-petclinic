FROM maven:3.5.3 as mvn
RUN mvn package -Dmaven.test.skip=true



