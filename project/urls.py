from django.conf.urls import url
from project import views

app_name = 'project'
urlpatterns = [
    url(r'^', views.IndexView.as_view(), name='index'),
    #/StudentsClubAcademy
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #/StudentsClubAcademy

    url(r'^subject/$', views.SubjectView.as_view(), name='subject'),
    #/StudentsClubAcademy/Subject/

    url(r'^subject/(?P<pk>\d+)/$', views.ShowSubjectView.as_view(), name='show_subject'),
    #/StudentsClubAcademy/Subject/1/

    url(r'^cource/$', views.CourceView.as_view(), name='cource'),
    #/StudentsClubAcademy/Cource/

    url(r'^cource/(?P<pk>\d+)/$', views.ShowCourceView.as_view(), name='show_cource'),
    #/StudentsClubAcademy/Cource/1/

    url(r'^cource/add/$', views.CourceCreate.as_view(), name='add-cource'),
    #/StudentsClubAcademy/Cource/add/
    url(r'^cource/(?P<pk>\d+)/$', views.CourceUpdate.as_view(), name='update-cource'),
    #/StudentsClubAcademy/Cource/2/
    url(r'^cource/(?P<pk>\d+)/delete/$', views.CourceDelete.as_view(), name='delete-cource'),
    #/StudentsClubAcademy/Cource/2/delete

    url(r'^lecture/(?P<pk>\d+)/$', views.ShowLectureView.as_view(), name='show_lecture'),
    #/StudentsClubAcademy/Lecture/1/

    url(r'^lecture/add/$', views.LectureCreate.as_view(), name='add-lecture'),
    #/StudentsClubAcademy/Lecture/add/
    url(r'^lecture/?P<pk>\d+)/$', views.LectureUpdate.as_view(), name='update-lecture'),
    #/StudentsClubAcademy/Lecture/2/
    url(r'^lecture/?P<pk>\d+)/delete/$', views.LectureDelete.as_view(), name='delete-lecture'),
    #/StudentsClubAcademy/Lecture/2/delete

    url(r'^lecture/(?P<lecture_id>\d+)/favorite/$', views.favorite, name='favorite'),
    #/StudentsClubAcademy/Lecture/1/favorite/

]