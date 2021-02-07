from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
	image = models.ImageField(upload_to='news/image/',  height_field=None, width_field=None, max_length=100)
	title = models.CharField(max_length=1000)
	text = models.TextField()
	create_date = models.DateTimeField(default = timezone.now)
	pyblished_date = models.DateTimeField(null = True, blank=True)

	def publish(self):
		self.publish_date = timezone.now()
	