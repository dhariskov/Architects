from django.urls import path

from projects import views
from projects.views import ProjectsListView, ProjectDetailsView, ProjectCreateView, MoreProjectDetailsView, \
    FullScreenView, EditView, DeleteView, EditMoreProjectDetailsView, DeleteProjectDetailsView, AboutView, \
    MyProjectsListView

urlpatterns = [
    path('', ProjectsListView.as_view(), name='index'),
    path('<int:pk>/', MyProjectsListView.as_view(), name='my_projects'),
    path('details/<int:pk>/', ProjectDetailsView.as_view(), name='details'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('add_more_details/<int:pk>/', views.project_create_form_view, name='add_more_details'),
    path('all_project_details/<int:pk>/', MoreProjectDetailsView.as_view(), name='all_project_details'),
    path('full_screen/<int:pk>/', FullScreenView.as_view(), name='full_screen'),
    path('update_project/<int:pk>/', EditView.as_view(), name='update_project'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('update_moredetails/<int:pk>/', EditMoreProjectDetailsView.as_view(), name='update_moredetails'),
    path('delete_project_details/<int:pk>/', DeleteProjectDetailsView.as_view(), name='delete_project_details'),
    path('<int:pk>/about/', AboutView.as_view(), name='about'),
]