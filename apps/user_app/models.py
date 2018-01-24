from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['fname'] = "First name is too short!"
        if len(postData['last_name']) < 2:
            errors['lname'] = "Last name is too short!"
        if len(postData['email']) < 2:
            errors['email'] = "Email is too short!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Not a valid email address!"
        return errors        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()