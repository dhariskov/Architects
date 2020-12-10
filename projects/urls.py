from django.urls import path

from projects import views
from projects.views import IndexView, ProjectsListView, ProjectDetailsView, ProjectCreateView, MoreProjectDetailsView, \
    FullScreenView, EditView, DeleteView

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('', ProjectsListView.as_view(), name='index'),
    path('details/<int:pk>', ProjectDetailsView.as_view(), name='details'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    # path('more_details/<int:pk>', MoreProjectDetailsView.as_view(), name='more_details')
    path('add_more_details/<int:pk>', views.ProjectCreateFormView, name='add_more_details'),
    path('all_project_details/<int:pk>', MoreProjectDetailsView.as_view(), name='all_project_details'),
    path('full_screen/<int:pk>', FullScreenView.as_view(), name='full_screen'),
    path('update_project/<int:pk>', EditView.as_view(), name='update_project'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
]