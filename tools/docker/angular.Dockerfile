FROM node:20-alpine3.17
ENV home_dir /opt/angular_home/
# Install OS requirements
RUN apk update && apk add bash
# Install npm packages
RUN npm install -g @angular/cli
RUN mkdir -p ${home_dir}
WORKDIR ${home_dir}