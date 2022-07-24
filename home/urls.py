from django.urls import path, include
from home.views import HomeView, UserAPIView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/user/', UserAPIView.as_view(), name='api')

]
