# base image
FROM alpine:latest

# Install python 3 and pip
RUN apk add --update python3
#yum install python3-pip
#ln -s /usr/bin/pip3 /usr/local/bin/pip3

# Install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/

RUN which pip3

RUN /usr/bin/pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

# Copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# Tell the port number the container should expose
EXPOSE 5000

# Run the application
CMD ["python3", "/usr/src/app/app.py"]
