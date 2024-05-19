from django.urls import path
from .views import *

urlpatterns = [
    path('profile', UserProfileView.as_view(), name='profile-page'),
    path('profile/edit', ProfileEditView.as_view(), name='profile-edit-page'),
    path('profile/change-pass', ChangePassView.as_view(), name='change-pass'),
    path('profile/my_shopping', MyShoppingList.as_view(), name='my-shopping'),
]