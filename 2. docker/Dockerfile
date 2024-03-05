FROM node:20-slim as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
#RUN npm test
RUN npm run build

FROM nginx:latest as app_name
COPY --from=build /app /app
COPY --from=build /app/app.conf /etc/nginx/conf.d/


