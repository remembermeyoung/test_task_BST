from django.urls import path
from robots.views import RobotCreateView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('robot/', csrf_exempt(RobotCreateView.as_view()))
]
