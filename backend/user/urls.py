from django.urls import path
from .views import SignUpView, SignInView, GetUserView

urlpatterns = [
    path('sign_up/', SignUpView.as_view()),
    path('sign_in/', SignInView.as_view()),
    path('user/', GetUserView.as_view()),
]