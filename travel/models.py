from django.db import models


class prabu(models.Model):
	name=models.CharField(max_length=100)
	img=models.ImageField(upload_to='pics')
	desc=models.TextField()
	price=models.IntegerField()
	offer=models.BooleanField(default=False)
	sp1=models.TextField(blank=True)
	sp2=models.TextField(blank=True)
	sp3=models.TextField(blank=True)
	sp4=models.TextField(blank=True)



class feed(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField()
	message=models.TextField()