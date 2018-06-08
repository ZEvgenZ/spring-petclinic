# FROM maven:3.5.3 AS mvn
# WORKDIR /app
# RUN git clone urla
# COPY . . 
# RUN mvn package -Dmaven.test.skip=true /app/spring-petclinic

FROM java:alpine
# ....
#COPY --from=mvn /app /
WORKDIR /app
RUN  addgroup -g 1000 -S appuser && \
   adduser -u 1000 -S user -G appuser
USER appuser
COPY --chown=appuser:appuser target/*.jar ./petclin.jar
ENV DB_USER=usersql
ENV DB_HOST=db
ENV DB_PASS=123456
ENV DB_NAME=petclinic
ENV DB_PORT=3306
EXPOSE 8080
CMD ["java","-jar","./petclin.jar"]