from django.urls import path
from .views import signup, verify_email, login_view, about
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('verify/<uidb64>/<token>/', verify_email, name='verify_email'),
    path('about/', about, name='about'),
]
