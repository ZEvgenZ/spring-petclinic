# FROM maven:3.5.3 AS mvn
# WORKDIR /app
# COPY . . 
# RUN mvn package -Dmaven.test.skip=true

FROM java:alpine
# ....
#COPY --from=mvn /app /
EXPOSE 8080
CMD ["java","-jar","./*.jar"]