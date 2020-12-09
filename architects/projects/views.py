from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.base import View, TemplateView

from projects.forms import MoreProjectDetailsForm, CommentForm
from projects.models import Project, MoreProjectDetails, Comment


class ProjectDetailsView(CreateView):
    template_name = 'details.html'
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                details = Comment(comment=form.cleaned_data['comment'])
                details.project = Project.objects.get(pk=self.kwargs['pk'])
                details.save()
            return redirect('details', self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {
            'project': Project.objects.get(pk=self.kwargs['pk']),
            'pk': self.kwargs['pk'],
            'comment': CommentForm(),
        }
        return context


def ProjectCreateFormView(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'GET':
        form = MoreProjectDetailsForm()
        context = {
            'form': form,
            'pk': pk,
            'project': project,
            'title': project.title,
            'count': MoreProjectDetails.objects.filter(project=project).count()
        }
        return render(request, 'add_more_details.html', context=context)
    else:
        form = MoreProjectDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            details = MoreProjectDetails(image=form.cleaned_data['image'], description=form.cleaned_data['description'])
            details.project = project
            details.save()
            return redirect('add_more_details', pk)
        context = {
            'form': form,
            'pk': pk,
            'project': project,
            'title': project.title
        }
        return render(request, 'add_more_details.html', context=context)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = Project.objects.all()
        return {
            'projects': Project.objects.all()
        }


class FullScreenView(TemplateView):
    template_name = 'full_screen.htm'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        return {
            'data': MoreProjectDetails.objects.get(pk=pk)
        }


class ProjectsListView(ListView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = '10'


# class MoreProjectDetailsView(ListView):
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context={
#             'project_id': self.kwargs['pk']
#         }
#         return context
#     template_name = 'all_project_details.html'
#     model = MoreProjectDetails.objects.filter(project_id=context['project_id'])
#     context_object_name = 'more_details'
#     # paginate_by = '10'

class MoreProjectDetailsView(TemplateView):
    template_name = 'all_project_details.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        data = MoreProjectDetails.objects.filter(project_id=pk)
        return {
            'project_name': Project.objects.get(pk=pk).title,
            'pk': pk,
            'more_details': data
        }


# class ProjectDetailsView(TemplateView):
#     template_name = 'details.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment'] = CommentForm
#         context['project'] = Project.objects.get(pk=self.kwargs['pk'])
#         context['pk'] = self.kwargs['pk']
#         return context

class ProjectDetailsView(CreateView):
    template_name = 'details.html'
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                details = Comment(comment=form.cleaned_data['comment'])
                details.project = Project.objects.get(pk=self.kwargs['pk'])
                details.save()
            return redirect('details', self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {
            'project': Project.objects.get(pk=self.kwargs['pk']),
            'pk': self.kwargs['pk'],
            'comment': CommentForm(),
        }
        return context


class ProjectCreateView(CreateView):
    fields = '__all__'
    model = Project
    template_name = 'create.html'
    # success_url = reverse_lazy(f'index')


# class MoreProjectDetailsView(CreateView):
#     def get_context_data(self, **kwargs):
#         context ={
#             'pk': self.kwargs['pk'],
#             'form': MoreProjectDetailsForm()
#         }
#         return context
#     fields = ['image', 'description']
#     model = MoreProjectDetails
#     template_name = 'more_details.html'
#     success_url = reverse_lazy('index')

