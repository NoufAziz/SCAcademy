from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)
    collage = models.CharField(max_length=100)
    level = models.CharField(max_length=7)
    def get_absolute_url(self):
        return reverse('project:cource', kwargs={'pk':self.pk})
    def __unicode__(self):
        return self.name + '-' + self.collage

class Course(models.Model):
    subject = models.ForeignKey(Subject)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=7)
    description = models.TextField(max_length=1000)
    pupdate = models.DateTimeField(auto_now_add=True)
    location = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.title

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    code = models.CharField(max_length=7)
    title = models.CharField(max_length=100)
    sources = models.TextField(max_length=500)
    objectives = models.TextField(max_length=500)
    pupdate = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    is_favorite = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class Comment_c (models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    auther = models.CharField(max_length=50)
    body = models.TextField()
    pup_date = models.DateTimeField(auto_now_add=True)

class Comment_l (models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    auther = models.CharField(max_length=50)
    body = models.TextField()
    pup_date = models.DateTimeField(auto_now_add=True)
