from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.base import View, TemplateView

from projects.models import Project, ProjectDetail


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = Project.objects.all()
        return {
            'projects': Project.objects.all()
        }


class ProjectsListView(ListView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = '2'


class ProjectDetailsView(DetailView):
    model = Project
    template_name = 'details.html'


class ProjectCreateView(CreateView):
    fields = '__all__'
    model = Project
    template_name = 'create.html'
    success_url = reverse_lazy('add details')


# class AddDetailsView