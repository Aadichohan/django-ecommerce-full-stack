from django.db import models

# Create your models here.

class User(models.Model):
    username   = models.CharField(max_length=30, unique=True)
    email      = models.EmailField(unique=True)
    name       = models.CharField(max_length=30, blank=True)
    password   = models.CharField(max_length=150)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "daraz_login"


class Author(models.Model):
    name  = models.CharField(max_length=50)
