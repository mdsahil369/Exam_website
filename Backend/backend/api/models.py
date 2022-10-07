from django.db import models

SUBJECT_CHOICES = (
    ('Pysics 1st','Pysics 1st'),
    ('Chemistry 1st',"Chemistry 1st"),
    ('Higher Math 1st','Higher Math 1st'),
    ('Biology 1st','Biology 1st'),
    ('Pysics 2nd','Pysics 2nd'),
    ('Chemistry 2nd',"Chemistry 2nd"),
    ('Higher Math 2nd','Higher Math 2nd'),
    ('Biology 2nd','Biology 2nd'),
)

CHEPTER_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
)


# Create your models here.
class Subject(models.Model):
  subject = models.CharField(choices=SUBJECT_CHOICES,max_length=50,default='')
  chapter = models.CharField(choices=CHEPTER_CHOICES,max_length=50,default='')
  question = models.CharField(max_length=250,default='')
  option01 = models.CharField(max_length=250,default='none')
  option02 = models.CharField(max_length=250,default='none')
  option03 = models.CharField(max_length=250,default='none')
  option04 = models.CharField(max_length=250,default='none')
  answer = models.CharField(max_length=200,default="none")
  board = models.CharField(max_length=100,default="")
  univercity = models.CharField(max_length=100,default="")
