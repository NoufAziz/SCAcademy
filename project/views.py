from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from project.models import Subject, Cource, Lecture
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
    context_object_name = "all_cources"
    def get_queryset(self):
        return Cource.objects.all()

class ShowSubjectView(generic.DetailView):
    model = Subject
    template_name = 'project/subject.html'
    subject_id = Subject.pk

class CourceView(generic.ListView):
    template_name = 'project/cource.html'
    context_object_name = "all_lectures"
    def get_queryset(self):
        return Lecture.objects.all()

class ShowCourceView(generic.DetailView):
    model = Cource
    template_name = 'project/cource.html'
    cource_id = Cource.pk

class ShowLectureView(generic.DetailView):
    model = Lecture
    template_name = 'project/show_lecture.html'
    lecture_id = Lecture.pk

class CourceCreate(CreateView):
    model = Cource
    fields = ['subject','title', 'descrbtion', 'pupdate', 'location' ]
class CourceUpdate(UpdateView):
    model = Cource
    fields = ['subject','title', 'descrbtion', 'pupdate', 'location' ]
class CourceDelete(DeleteView):
    model = Cource
    success_url = reverse_lazy('project:index')

class LectureCreate(CreateView):
    model = Lecture
    fields = ['cource','title', 'sources','objectives', 'pupdate', 'link' ]
class LectureUpdate(UpdateView):
    model = Lecture
    fields = ['cource','title', 'sources','objectives', 'pupdate', 'link' ]
class LectureDelete(DeleteView):
    model = Lecture
    success_url = reverse_lazy('project:index')

def favorite(request,lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    try:
        selected_lecture = Cource.lecture_set.get(pk=request.POST['lecture'])
    except(KeyError, Lecture.DoesNotExist):
        return render(request, 'project/show_lecture.html', {
            'lecture': lecture,
            'error_message': 'You did not select a valid lecture',
        })
    else:
        selected_lecture.is_favorite = True
        selected_lecture.save()
        return render(request, 'project/show_lecture.html', {'lecture': lecture})

