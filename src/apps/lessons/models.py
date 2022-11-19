from django.db import models

class Lesson(models.Model):
    start = models.DateTimeField()
    duration = models.IntegerField()
    teacher = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    subject = models.ForeignKey('subjects.Subject', on_delete=models.PROTECT, null=True)
