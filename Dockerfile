FROM python:2.7-alpine

ADD DriverProgram.py  /
ADD ConfigFile.properties  /

#RUN pip install pystrich
RUN pip install boto3

CMD [ "python", "./DriverProgram.py" ]
