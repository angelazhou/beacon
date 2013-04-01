from django.shortcuts import render, render_to_response
from CourseData.models import universityCourses, courseNickname, userCourses
from BeaconData.models import signups, beacons
import collections

def getInfo(request):
	courseNum = request.GET.get('courseNum', '')
	
	uniCourse = universityCourses.objects.get(courseNum = courseNum)
	courseName = uniCourse.courseName

	courses = courseNickname.objects.filter(courseNum_id = courseNum)
	courseIds = []
	for course in courses:
		courseIds.append(course.courseAbbrev)

	return render_to_response('courseInfo.html', {'courseName': courseName, 'courseIds': courseIds})

def getinitInfo(request):
	this_userID = request.user.id;
	
	this_userCourses = userCourses.objects.filter(userID=this_userID)
	
	userAbbrevs = []
	for course in this_userCourses:
		userAbbrevs.append(course.courseAbbrev_id)
	
	this_userCourseNums = courseNickname.objects.filter(courseAbbrev__in=userAbbrevs)

	userNums = []
	for course in this_userCourseNums:
		userNums.append(course.courseNum_id)

	this_userBeacons = signups.objects.filter(userID = this_userID)

	courseNums = []
	for course in this_userCourseNums:
		courseNums.append(course.courseNum)

	beaconIds = []
	for beacon in this_userBeacons:
		beaconIds.append(beacon.id)

	return render_to_response('initInfo.html', {'userID': this_userID, 'courseSize': len(userAbbrevs), 'courseNums': userNums, 'beaconIds': beaconIds})
