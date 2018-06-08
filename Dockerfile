# FROM maven:3.5.3 AS mvn
# WORKDIR /app
# COPY . . 
# RUN mvn package -Dmaven.test.skip=true

FROM java:alpine
# ....
#COPY --from=mvn /app /
WORKDIR /app
RUN useradd -u 1000 -g 1000 appuser
USER appuser
COPY --chown=appuser:appuser target/*.jar ./petclin.jar
# ENV DB_USER=myuser
# ENV DB_HOST=db
# ENV DB_PASS=1234
# ENV DB_NAME=db
# ENV DB_PORT=3306
EXPOSE 8080
CMD ["java","-jar","./petclin.jar"]