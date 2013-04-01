from django.db import models
from django_extensions.db.models import TimeStampedModel
from CourseData.models import universityCourses
from django.contrib.auth.models import User

class beacons(TimeStampedModel):
	#auto generated primary id field
	courseNum = models.ForeignKey(universityCourses)
	startTime = models.DateTimeField()
	endTime = models.DateTimeField(null=True)
	adminID = models.ForeignKey(User)
	location = models.CharField(max_length = 100)
	comments = models.CharField(max_length = 2000)
	visible = models.BooleanField()
	maxSize = models.IntegerField()

class signups(TimeStampedModel):
	userID = models.ForeignKey(User)
	beaconID = models.ForeignKey(beacons)
