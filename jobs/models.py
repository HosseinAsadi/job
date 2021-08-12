from django.db import models

# Create your models here.

class Jobs(models.Model):

    title = models.CharField(unique=False, max_length=300,null=False,blank=False)

    paymentType=models.CharField(unique=False, max_length=300,null=False,blank=False) # =>type of payment

    paymentValue=models.CharField(unique=False, max_length=300,null=False,blank=False) # =>value depend on payment time

    paymentTime=models.CharField(unique=False, max_length=300,null=False,blank=False) # =>value depend on payment time

    bidsCount=models.IntegerField(null=False,default=0,blank=False,help_text="counter bids  for this job")

    description = models.TextField(default="")
    
    like_counts=models.IntegerField(null=False,default=0,blank=False,help_text="counter likes  for this job")
    
    # TODO employer=models.ForeignKey()

    isOpen=models.BooleanField(default=True)



class Bids(models.Model):

    # TODO  applicant=models.ForeignKey()

    description = models.TextField(default="")

    # TODO  agrementType=models.ChoiceField(blank)   => show type of aggrement:unseen,seen,accept,reject


    attachment= models.FileField(null=True, blank=True)




