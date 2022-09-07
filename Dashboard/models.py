from django.db import models
from django.contrib.auth.models import User


class Domain(models.Model):
    domain_name = models.CharField('Domain Name', max_length=30)

    def __str__(self):
        return self.domain_name
    
class Questions(models.Model):
    que_id = models.CharField('Question Id', max_length=5)
    que_title = models.CharField('Title Name', max_length=150)
    que_link = models.URLField('Question Link')
    que_domain = models.ManyToManyField(Domain, blank = True)
    que_difficulty = models.CharField('Difficulty Level', max_length=10)
    dsa_sheet = models.CharField('DSA Sheet', max_length=2) #L - Love Babbar; F - Fraz; S - Striver; A - Apna College

    def __str__(self):
        return self.que_title


class Student(models.Model):
    user = models.ForeignKey(User, blank = True, null = True, on_delete = models.CASCADE)
    que_ids = models.ManyToManyField(Questions, blank = True) 
    
    def __str__(self):
        return self.user.first_name+' '+self.user.last_name
