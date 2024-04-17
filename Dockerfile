FROM python:3.12
RUN mkdir -p /opt/termo
COPY . /opt/termo/
RUN pip install django termcolor unidecode python-decouple dj-database-url psycopg2-binary
WORKDIR /opt/termo/
RUN chmod +x entrypoint.sh
EXPOSE 5200
ENTRYPOINT [ "/opt/termo/entrypoint.sh" ]
CMD ["python", "manage.py", "runserver", "--noreload", "0.0.0.0:5200"]