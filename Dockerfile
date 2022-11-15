FROM node:18
USER root

RUN apt update
RUN apt install python3 python3-pip --no-install-recommends -y
RUN pip install moviepy
RUN pip install nltk
RUN pip install unidecode
RUN pip install contractions
RUN pip install SpeechRecognition

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app

COPY package*.json ./

RUN npm install --unsafe-perm
RUN npm install pm2 -g --unsafe-perm

USER node

COPY --chown=node:node . .

ENV HOST 0.0.0.0
ENV PORT 8080
EXPOSE 8080

ENTRYPOINT ["pm2", "start", "--no-daemon", "/home/node/app/server/index.js"]