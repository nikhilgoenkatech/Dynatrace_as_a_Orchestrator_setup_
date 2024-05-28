FROM python:3.10-slim-buster

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip3.10 install -r requirements.txt

COPY . /app

# Set environment variables
ENV SSO_AUTH=${SSO_AUTH}
ENV CLIENT_ID=${CLIENT_ID}
ENV CLIENT_SECRET=${CLIENT_SECRET}
ENV WORKFLOW_ENDPOINT=${WORKFLOW_ENDPOINT}
ENV FLASK_ENV="development"

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
