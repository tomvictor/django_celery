# Create your tasks here

from celery import shared_task
import time

@shared_task
def do_work(data):
    print(data)
    print("start work")
    time.sleep(10)
    print("work completed")
    return "ret"

#
# @shared_task
# def count_widgets():
#     return Widget.objects.count()
#
#
# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()