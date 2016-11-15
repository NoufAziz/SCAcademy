from django.conf.urls import url
from project import views

app_name = 'project'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/StudentsClubAcademy

    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #/StudentsClubAcademy


    url(r'^subject/$', views.SubjectView.as_view(), name='subject'),
    #/StudentsClubAcademy/Subject/

    url(r'^subject/(?P<subject_id>[0-9]+)/$', views.ShowSubjectView.as_view(), name='show_subject'),
    #/StudentsClubAcademy/Subject/1/


    url(r'^course/$', views.CourseView.as_view(), name='course'),
    #/StudentsClubAcademy/Course/

    url(r'^course/(?P<cource_id>[0-9]+)/$', views.ShowCourseView.as_view(), name='show_course'),
    #/StudentsClubAcademy/Course/1/

    url(r'^course/add/$', views.CourseCreate.as_view(), name='add-course'),
    #/StudentsClubAcademy/Course/add/
    url(r'^course/(?P<course_id>[0-9]+)/$', views.CourseUpdate.as_view(), name='update-course'),
    #/StudentsClubAcademy/Course/2/
    url(r'^course/(?P<course_id>[0-9]+)/delete/$', views.CourseDelete.as_view(), name='delete-course'),
    #/StudentsClubAcademy/Course/2/delete


    url(r'^lecture/(?P<lecture_id>[0-9]+)/$', views.ShowLectureView.as_view(), name='show_lecture'),
    #/StudentsClubAcademy/Lecture/1/

    url(r'^lecture/add/$', views.LectureCreate.as_view(), name='add-lecture'),
    #/StudentsClubAcademy/Lecture/add/
    url(r'^lecture/(?P<lecture_id>[0-9]+)/$', views.LectureUpdate.as_view(), name='update-lecture'),
    #/StudentsClubAcademy/Lecture/2/
    url(r'^lecture/(?P<lecture_id>[0-9]+)/delete/$', views.LectureDelete.as_view(), name='delete-lecture'),
    #/StudentsClubAcademy/Lecture/2/delete


]