from django.urls import path

from projects.views import IndexView, ProjectsListView, ProjectDetailsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('details/<int:pk>', ProjectDetailsView.as_view(), name='details'),
    path('index/', ProjectsListView.as_view(), name='index 2'),
]
