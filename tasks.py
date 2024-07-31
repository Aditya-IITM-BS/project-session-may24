from celery import shared_task
import time
from flask_excel import make_response_from_query_sets
from models import StudyResource
from mail_service import send_email

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

@shared_task
def daily_reminder(to,sub, message):
    send_email(to, sub, message)
    return "OK"