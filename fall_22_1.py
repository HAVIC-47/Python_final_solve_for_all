def homepage(request):
     return render(request,"homepage.html")

from django.urls import path,include
from .import vbiews

urlpatterns=[
     path("",views.homepage , name="homepage")
]


