from django.shortcuts import render, redirect

# Create your views here.
# from django.urls import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.base import TemplateView
from django import views

from authentication.models import Profile, UserModel
from projects.forms import MoreProjectDetailsForm, CommentForm, FilterForm
from projects.models import Project, MoreProjectDetails, Comment


class ProjectDetailsView(CreateView):
    template_name = 'details.html'
    model = Comment
    fields = ['comment', ]

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.project = Project.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

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
    # order_by_asc = True
    order_by = ''
    contains_text = ''

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        # self.order_by_asc = params['order'] == FilterForm.ORDER_ASC
        self.order_by = params['order']
        self.contains_text = params['text']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        order_by = self.order_by
        if order_by == 'title':
            result = self.model.objects.filter(title__icontains=self.contains_text).order_by(order_by)
        else:
            result = self.model.objects.filter(type__icontains=self.contains_text).order_by(order_by)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FilterForm(initial={
            # 'order': self.order_by,
            'text': self.contains_text
        })

        return context

# class ProjectsListView(ListView):
#     template_name = 'index.html'
#     model = Project
#     context_object_name = 'projects'
#     paginate_by = '10'
#     order_by_asc = True
#     search_by = 'title'
#     contains_text = ''
#
#     def dispatch(self, request, *args, **kwargs):
#         params = extract_filter_values(request.GET)
#         self.order_by_asc = params['search_by'] == FilterForm.SEARCH_BY_TITLE
#         self.order_by = params['search_by']
#         self.contains_text = params['text']
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_queryset(self):
#         search_by = 'title' if self.search_by == FilterForm.SEARCH_BY_TITLE else '-title'
#         result = self.model.objects.filter(title__icontains=self.contains_text).search_by(search_by)
#
#         return result
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter_form'] = FilterForm(initial={
#             'search_by': self.search_by,
#             'text': self.contains_text
#         })
#
#         return context


class MyProjectsListView(ListView):
    template_name = 'index.html'
    model = Project

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs['pk']
        context = {
            'projects': Project.objects.filter(user_id=pk),
        }
        return context

class MoreProjectDetailsView(TemplateView):
    template_name = 'all_project_details.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        data = MoreProjectDetails.objects.filter(project_id=pk)
        return {
            'project_name': Project.objects.get(pk=pk).title,
            'project_user': Project.objects.get(pk=pk).user,
            'pk': pk,
            'more_details': data
        }


class ProjectCreateView(CreateView):
    fields = ['title', 'type', 'image', 'description']
    model = Project
    template_name = 'create.html'

    def get_success_url(self):
        pk = Project.objects.all().last().id
        return reverse_lazy('add_more_details', kwargs={'pk': pk})


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# def get_context_data(self, **kwargs):
#     context = {
#         # 'project': Project.objects.get(pk=self.kwargs['pk']),
#         # 'pk': self.kwargs['pk'],
#         # 'comment': CommentForm(),
#     }
#     return context


class EditView(views.generic.UpdateView):
    fields = ['title', 'type', 'image', 'description']
    model = Project
    template_name = 'edit.html'

    def get_success_url(self):
        pk = Project.objects.all().last().id
        return reverse_lazy('details', kwargs={'pk': pk})


class EditMoreProjectDetailsView(views.generic.UpdateView):
    fields = ['image', 'description']
    model = MoreProjectDetails
    template_name = 'edit_more_project_details.html'

    # success_url = reverse_lazy('index')

    def get_success_url(self):
        pk = MoreProjectDetails.objects.filter(id=self.kwargs['pk']).last().project_id
        return reverse_lazy('all_project_details', kwargs={'pk': pk})


class DeleteView(views.generic.DeleteView):
    model = Project
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


class DeleteProjectDetailsView(views.generic.DeleteView):
    model = MoreProjectDetails
    template_name = 'delete_project_details.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        pk = MoreProjectDetails.objects.get(id=self.kwargs['pk']).project_id
        return reverse_lazy('all_project_details', kwargs={'pk': pk})


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        return {
            'data': Profile.objects.get(pk=pk)
        }

    # def dispatch(self, request, *args, **kwargs):
# def extract_filter_values(params):
#     search_by = params['search_by'] if 'search_by' in params else FilterForm.SEARCH_BY_TITLE
#     text = params['text'] if 'text' in params else ''
#
#     return {
#         'search_by': search_by,
#         'text': text,
#     }

def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.SEARCH_BY_TITLE
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }