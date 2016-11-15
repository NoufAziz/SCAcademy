from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from project.models import Subject, Course, Lecture
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import Userform

class UserFormView(View):
    form_class = Userform
    template_name= 'project/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user= form.save(commit=False)

            username = form.clean_data['username']
            password = form.clean_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('project:index')
        return render(request, self.template_name, {'form':form})

class IndexView(generic.ListView):
    template_name = 'project/index.html'
    context_object_name = 'all_subjects'
    def get_queryset(self):
        return Subject.objects.all()

class SubjectView(generic.ListView):
    template_name = 'project/subject.html'
    context_object_name = "all_courses"
    def get_queryset(self):
        return Course.objects.all()

class ShowSubjectView(generic.DetailView):
    model = Subject
    template_name = 'project/subject.html'
    subject_id = Subject.pk

class CourseView(generic.ListView):
    template_name = 'project/course.html'
    context_object_name = "all_lectures"
    def get_queryset(self):
        return Lecture.objects.all()

class ShowCourseView(generic.DetailView):
    model = Course
    template_name = 'project/course.html'
    course_id = Course.pk

class ShowLectureView(generic.DetailView):
    model = Lecture
    template_name = 'project/show_lecture.html'
    lecture_id = Lecture.pk

class CourseCreate(CreateView):
    model = Course
    fields = ['subject','title', 'description', 'location' ]
    success_url = reverse_lazy('project:index')
class CourseUpdate(UpdateView):
    model = Course
    fields = ['subject','title', 'description', 'location' ]
    success_url = reverse_lazy('project:index')
class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('project:index')

class LectureCreate(CreateView):
    model = Lecture
    fields = ['course','title', 'sources','objectives', 'link' ]
    success_url = reverse_lazy('project:index')
class LectureUpdate(UpdateView):
    model = Lecture
    fields = ['course','title', 'sources','objectives', 'link' ]
    success_url = reverse_lazy('project:index')
class LectureDelete(DeleteView):
    model = Lecture
    success_url = reverse_lazy('project:index')

