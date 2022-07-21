from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import (
    TruncDate, TruncDay, TruncHour, TruncMinute, TruncSecond,
)
from rest_framework import generics
from .serializer import UserSerializer


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        # логика анализа модели users
        users_list_all = User.objects.all()
        users_list = User.objects.annotate(day=TruncDay('date_joined')).values('day').annotate(count=Count('id'))

        context = {
            "users_list": users_list,
            "users_list_all": users_list_all
        }
        return render(request, self.template_name, context)
