FROM python:3.8
WORKDIR /app-example
COPY src .
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "python", "index.py" ]


