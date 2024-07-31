from celery import shared_task
import time
from mail_service import send_email
from models import StudyResource
from flask_excel import make_response_from_query_sets

@shared_task()
def add(x,y):
    time.sleep(15)
    return x+y

@shared_task(ignore_result = False)
def export_job():
    resource = StudyResource.query.with_entities(StudyResource.topic, StudyResource.content).all()

    csv_out = make_response_from_query_sets(resource, ['topic','content'], 'csv', filename="study.csv")

    with open('./user-downloads/file.csv', 'wb') as file:
        file.write(csv_out.data)
    
    return 'file.csv'

@shared_task()
def daily_reminder(message):
    send_email('harsh.gmail', message, '<h1> content body </h1>')
    return "OK"