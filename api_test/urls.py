from django.urls import path,include
from django.conf.urls import url,include    
from .import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('api_test',views.MachineView)
urlpatterns = [
   url(r'',include(router.urls))   
]