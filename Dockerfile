# For more information, please refer to https://aka.ms/vscode-docker-python
FROM google/cloud-sdk:313.0.0

LABEL Name=$BITBUCKET_REPO_SLUG Version=0.0.1

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD requirements.txt .

RUN python3.8 -m pip install --upgrade pip
RUN python3.8 -m pip install -r requirements.txt

RUN apt-get update

WORKDIR /app
ADD . /app

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 4 app:app
CMD exec gunicorn --bind :$PORT --workers 1 --threads 4 app:app
