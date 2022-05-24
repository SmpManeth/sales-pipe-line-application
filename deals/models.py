from django.db import models

# Create your models here.
class Deal(models.Model):
    contact_person = models.CharField(max_length=100, blank=False)
    organization = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    value = models.IntegerField(default=0)
    pipeline = models.CharField(max_length=100)
    pipeline_stage = models.CharField(max_length=100)
    expected_close_date = models.DateField()
    visible_to = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100 ,blank=False)
    work_mobile_no = models.CharField(max_length=100)

    personal_email = models.CharField(max_length=100)
    work_email = models.CharField(max_length=201000)


