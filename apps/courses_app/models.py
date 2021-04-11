from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime


# Create your models here.
class CoursesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print(postData)
        if len(postData['course_name']) < 5:
            errors['course_name'] = "needs to be at least 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "needs to be at least 15 characters"

        return errors

class Courses(models.Model):
    course_name = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CoursesManager()

    def __str__(self):
        return (f"{self.course_name}")
