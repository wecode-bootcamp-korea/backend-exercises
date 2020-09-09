from django.shortcuts import render
import django.views import View
from django.http    import JsonResponse
from .models        import Users

class MainView(View):
    def post(self, request):
    data = json.loads(requset.body)

    Users(
            name     = data['name']
            img_link = data['img']
            ).save()



# Create your views here.
