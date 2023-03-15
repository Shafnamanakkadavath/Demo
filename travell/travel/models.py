from django.db import models

# Create your models here
class  place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def str  (self):
        return self.name
class people(models.Model):
    p_name=models.CharField(max_length=250)
    p_img=models.ImageField(upload_to='pics')
    p_desc=models.TextField()
    def str  (self):
        return self.p_name