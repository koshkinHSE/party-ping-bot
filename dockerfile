#Docker stuff here

FROM python:3.10-slim
WORKDIR /opt/party-ping-bot
COPY bot.py bot.db config.py sqlighter.py utilities.py requirements.txt README.md ./
RUN pip3 install -r requirements.txt

CMD ["python", "./bot.py"]