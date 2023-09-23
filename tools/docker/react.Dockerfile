FROM node:20-alpine3.17
ENV home_dir /opt/react_home/
# Install OS requirements
RUN apk update && apk add bash
# Install npm packages
RUN npm install -g react
RUN mkdir -p ${home_dir}
WORKDIR ${home_dir}