FROM python:3.10-slim-buster

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip3.10 install -r requirements.txt

COPY . /app

# Set environment variables
ENV CLIENT_ID=${CLIENT_ID}
ENV CLIENT_SECRET=${CLIENT_SECRET}
ENV COMPILATION_ERROR_WORKFLOW=${COMPILATION_ERROR_WORKFLOW}
ENV API_URL=${API_URL}
ENV FLASK_ENV="development"

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]