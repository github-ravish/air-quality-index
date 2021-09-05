from django.urls import path
from django.contrib.auth import views as auth_views

from user_account.views import (
    UserAccountCreateView,
    UserAccountLoginView,
    UserAccountDetailView,
    UserAccountChangePasswordView
)

app_name = 'user_account'

urlpatterns = [
    path('signup/<str:referral_code>/', UserAccountCreateView.as_view(),
         name='create_with_referral'),
    path('signup/', UserAccountCreateView.as_view(), name='create'),

    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


# For profile routes
urlpatterns += [
    path('profile/', UserAccountDetailView.as_view(), name='detail_home'),
]

# For password

urlpatterns += [
    path('password/change/', UserAccountChangePasswordView.as_view(),
         name='change_password'),
]
