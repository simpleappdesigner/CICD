# Use an official Python runtime as a parent image
# FROM python:3.13.0a4-alpine3.19 error: Segmentation fault, so switched to 3.10
FROM python:3.10.13-alpine3.19

# set up workspace directory , create folder app
WORKDIR /app

# copy the requirements.txt which will be used to build the python enviroment
COPY ./requirements.txt /app/

# copy main.py with flask app
COPY ./main.py /app/

# run pip command to install dependencies
RUN pip install -r requirements.txt

# run flask on localhost with port 5001
CMD ["flask" ,"--app" ,"main" ,"run", "--host","0.0.0.0", "--port","5001"]

#CMD ["python","main.py"]


