# FROM node:14.15.0-alpine as builder

# RUN mkdir /Hospital
# WORKDIR /Hospital


# COPY Frontend-app/package.json Frontend-app/package-lock.json /Hospital/Frontend-app/


# RUN npm install --prefix Frontend-app

# COPY . /Hospital/
# RUN npm run build --prefix Frontend-app -- --output-path=./dist/out


FROM node:16.2.0 as builder

RUN mkdir /app
WORKDIR /app


COPY FrontEnd/package.json FrontEnd/package-lock.json /app/FrontEnd/


RUN npm install --prefix FrontEnd

# RUN npm install

COPY . /app/
RUN npm run build --prefix FrontEnd -- --output-path=./dist/out
#RUN npm run build

FROM nginx:1.15.7-alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/FrontEnd/dist/out /usr/share/nginx/html
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
