from django.urls import path

from projects.views import IndexView, ProjectsListView, ProjectDetailsView, ProjectCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('details/<int:pk>', ProjectDetailsView.as_view(), name='details'),
    path('index/', ProjectsListView.as_view(), name='index 2'),
    path('create/', ProjectCreateView.as_view(), name='create')
    path('add_details/', ProjectCreateView.as_view(), name='create')
]
