from celery import shared_task
import time

# igonre_resuls mean you dont store the result, where results don't matter

@shared_task(ignore_result = False)
def celery_task():
    time.sleep(5)
    return "successfully processed"