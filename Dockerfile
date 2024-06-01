FROM python:3.12
RUN mkdir -p /opt/termooo/
COPY . /opt/termooo/
RUN pip install django unittest coverage termcolor unidecode python-decouple dj-database-url psycopg2-binary Pillow
WORKDIR /opt/termooo/
RUN chmod +x /opt/termooo/entrypoint.sh
EXPOSE 5200
ENTRYPOINT [ "/opt/termooo/entrypoint.sh" ]
CMD ["python", "manage.py", "runserver", "--noreload", "0.0.0.0:5200"]