from django.db import models
from career_map.valid import validate
# Create your models here.
class persion_detail(models.Model):
    d = (
        (
            "AI", "AI"
        ),
        (
            "MECHANICAL", "MECHANICAL"

        ),
        (
            "ELECTRICAL", "ELECTRICAL"
        )
    )
    user_name=models.CharField(max_length=40)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    mail_id= models.CharField(max_length=200)
    resume=models.FileField(upload_to='static/cv',validators=[validate])
    domain=models.CharField(max_length=100,choices=d,null=True,default="AI")



class post_job(models.Model):
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    mail_id=models.CharField(max_length=50)
    company_name=models.CharField(max_length=500,default=' ')
class jobs(models.Model):
    job_title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=1000)
    contact=models.CharField(max_length=1000)
    company_name=models.CharField(max_length=500,default=' ')

