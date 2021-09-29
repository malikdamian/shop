from django.urls import path
from .views import LoginView, LogoutView, UserRegistrationView, UserInfoView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('user-info/<int:user_id>/', UserInfoView.as_view(), name='user-info')

]