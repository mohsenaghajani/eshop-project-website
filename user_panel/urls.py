from django.urls import path
from .views import *

urlpatterns = [
    path('profile', UserProfileView.as_view(), name='profile-page'),
    path('profile/edit', ProfileEditView.as_view(), name='profile-edit-page'),
]