from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_groups, name="users"),
    path('<int:pk>/delete', views.UsersDeleteView.as_view(), name='users-delete'),
    path('<int:pk>/update', views.UsersUpdateView.as_view(), name='users-update'),
    path('create', views.create, name='create'),
    path('create_groups', views.create_groups, name='create_groups'),
    path('<int:pk>/delete_groups', views.GroupsDeleteView.as_view(), name='groups-delete'),
    path('<int:pk>/update_groups', views.GroupsUpdateView.as_view(), name='groups-update'),
]