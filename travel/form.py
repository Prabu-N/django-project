from django.forms import ModelForm 
from .models import feed

class feed_back(ModelForm):
	class Meta:
		model=feed
		fields=[
		    'name',
		    'email',
		    'message',
	    ]