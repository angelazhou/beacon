from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'beaconauth.views.login_user'),
     url(r'^login/', 'beaconauth.views.login_user'),
	 url(r'^logout/', 'beaconauth.views.logout_user'),
	 url(r'^register/', 'beaconauth.views.register_user'),
	 url(r'^home/', 'beaconauth.views.homepage'),
	 url(r'^beaconInfo.html/', 'BeaconData.views.getBeaconInfo'),
     url(r'^initInfo.html/', 'CourseData.views.getinitInfo'), 
	 url(r'^courseInfo.html/', 'CourseData.views.getInfo'), 
	 url(r'^beaconIDListInfo.html/', 'BeaconData.views.getIDListInfo'),
	 url(r'^beaconStore.html', 'BeaconData.views.beaconStore'),
	 url(r'^courseStore.html', 'CourseData.views.courseStore'),
	 url(r'^admin/', include(admin.site.urls)),
)
