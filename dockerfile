FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install dependency_injector
RUN pip install pika
RUN pip install pymongo
RUN pip install pytz
CMD ["python","-u","/app/Startup.py"]