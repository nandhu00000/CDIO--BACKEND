from django.urls import  path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/html',views.show),
    path('main/top/number/<int:id>',views.show_num ),
    path('',views.html),
    path('nandhu',views.insert)
]
