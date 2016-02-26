from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [url(r'^$', views.welcome,name='welcome'),
				url(r'^course(?P<course_id>[0-9]+)/modules/(?P<section_id>[0-9]*)$', views.section_page,name='questions'),
				url(r'^api/(?P<course_id>[0-9]+)/progress$',views.progress_data,name='progress_api'),
				url(r'^(?P<course_id>[0-9]+)/progress$',views.progress_page,name='progress'),
				url(r'^profile$',views.profile_page,name='profile'),
				url(r'^api/completed/(?P<section_id>[0-9]+)$',views.section_completed,name='completed_api'),
				url(r'^(?P<course_id>[0-9]+)/description$',views.course_detail_page,name='course_detail'),
				url(r'^(?P<course_id>[0-9]+)/join$',views.join_page,name='join'),
				url(r'^(?P<course_id>[0-9]+)/withdraw$',views.withdraw_page,name='withdraw'),
				url(r'^login$',views.user_login,name='login'),
				url(r'^logout$',views.user_logout,name='logout'),
				url(r'^register$',views.user_register,name='register'),
				url(r'^course(?P<course_id>[0-9]+)/test$',views.test_yourself,name='test_yourself'),
				url(r'^forumq$',views.forum_qs,name='forumq'),
				url(r'^forump$',views.forum_ps,name='forump'),
				url(r'^testajax$',views.test_ajax,name='testajax'),
				url(r'^testpost$',views.test_ajax_post,name='testpost'),
				url(r'^courses$',views.courses_page,name='all_courses'),
				]
				#url(r'^(?P<course>[\w\.\-\_]+)/(?P<module>[\w\.\-\_]+)/(?P<section_id>[\w\.\-\_]+)$', views.section_page,name='questions')]



#url(r'^(?P<username>[\w\.\+\-\_\@]+)$', views.publicTiles,name='public')
#url(r'^(?P<user_id>[0-9 A-z]+)/(?P<tile_id>[0-9]+)/share$', views.shareTile,name='share')

#questions - modify so that course name  and module no appear in url - considering creating a short name for each course
#