from celery import shared_task
from models import StudyResource
from flask_excel import make_response_from_query_sets
import time

# igonre_resuls mean you dont store the result, where results don't matter

@shared_task(ignore_result = False)
def create_csv():
    time.sleep(5)
    studyRes = StudyResource.query.with_entities(StudyResource.topic, StudyResource.content).all()

    csv_out = make_response_from_query_sets(studyRes, ["topic", "content"], 'csv', file_name="study.csv")

    with open('./downloads/file.csv', 'wb') as file:
        file.write(csv_out.data)

    return 'file.csv'