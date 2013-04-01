from django.shortcuts import render_to_response, render
from BeaconData.models import beacons, signups
from CourseData.models import universityCourses, courseNickname
from django.contrib.auth.models import User

def getID

def getIDListInfo(request):
	courseNum = request.GET.get('courseID', '')	#should be courseNum
	
	selectedBeacons = beacons.objects.filter(courseNum_id=courseNum)

	beaconIds = []
	for beacon in selectedBeacons:
		beaconIds.append(beacon.id)

	return render_to_response('beaconIDListInfo.html', {'beaconIds': beaconIds})

def getBeaconInfo(request):
	beaconID = int(request.GET.get('beaconID', ''))
	userID = int(request.GET.get('userID', ''))
	
	beacon = beacons.objects.get(id=beaconID)
	course = universityCourses.objects.get(courseNum=beacon.courseNum_id)
		
	courseNum = beacon.courseNum_id
	location = beacon.location
	#change to return time in 13:30 format
	startTime = beacon.startTime
	endTime = beacon.endTime
	comments = beacon.comments
	isAdmin = (userID is beacon.adminID)
	beaconusers = signups.objects.filter(beaconID = beaconID)

	signedUsers = []
	for user in beaconusers:
		signedUsers.append(user.userID_id)

	namedUsers = User.objects.filter(id__in=signedUsers)
	
	names = []
	for user in namedUsers:
		names.append(user.username)
	
	return render_to_response('beaconInfo.html', {'courseNum': courseNum, 'location': location, 'startTime': startTime, 'endTime': endTime, 'comments': comments, 'isAdmin': isAdmin, 'beaconusers': names})
