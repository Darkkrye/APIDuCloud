from django.db import models

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


@python_2_unicode_compatible
class Professor(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

    def __str__(self):
        return f"[{self.firstname} {self.lastname}]"

@python_2_unicode_compatible
class Subject(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor)

    def __str__(self):
        return f"[{self.code} - {self.name} : {self.professor}]"

@python_2_unicode_compatible
class Promotion(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f"[{self.code} - {self.name}]"

@python_2_unicode_compatible
class Class(models.Model):
    date = models.DateTimeField('date')
    duration = models.IntegerField()
    subject = models.ForeignKey(Subject)
    promotion = models.ForeignKey(Promotion)

    def __str__(self):
        return f"[{self.date} - {self.duration} : {self.subject} - {self.promotion}]"

@python_2_unicode_compatible
class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    promotion = models.ForeignKey(Promotion)

    def __str__(self):
        return f"[{self.firstname} - {self.lastname} : {self.promotion}]"
