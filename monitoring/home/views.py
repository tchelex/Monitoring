from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from datetime import date, datetime
from django.db.models import Count
from django.db.models.functions import (
    TruncDate, TruncDay, TruncHour, TruncMinute, TruncSecond,
    )
class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        # логика анализа модели users
        users_list_all = User.objects.all()
        users_list = User.objects.annotate(day=TruncDay('date_joined')).values('day').annotate(count=Count('id'))
        # for user in users_list:
        #     print(user['day'], user['count'])

        context = {
            "users_list": users_list,
            "users_list_all": users_list_all

        }
        return render(request, self.template_name, context)
