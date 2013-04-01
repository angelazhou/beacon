from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User

class universityCourses(models.Model):
	courseNum = models.IntegerField(primary_key=True)
	courseName = models.CharField(max_length=300)

class courseNickname(models.Model):
	courseAbbrev = models.CharField(max_length=10, primary_key=True)
	courseNum = models.ForeignKey(universityCourses)

class userCourses(TimeStampedModel):
	#auto generated primary field
	userID = models.ForeignKey(User)
	courseAbbrev = models.ForeignKey(courseNickname)
