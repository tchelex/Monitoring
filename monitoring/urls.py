from django.contrib import admin
from django.urls import path, include
from users import views as userReg
from django.contrib.auth import views as authReg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', userReg.register, name='reg'),
    path('profile/', userReg.profile, name='profile'),
    path('auth/', authReg.LoginView.as_view(template_name='users/auth.html'), name='auth'),
    path('exit/', authReg.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('', include('home.urls'))
]
