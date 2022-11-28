from django.db import models

class User(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  email = models.EmailField()
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __repr__(self):
    return "First_name:{}".format(self.first_name)