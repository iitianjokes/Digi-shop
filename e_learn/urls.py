
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from e_learn.settings import MEDIA_URL ,MEDIA_ROOT ,STATIC_URL,STATIC_ROOT
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),

] + static(MEDIA_URL ,
           document_root = MEDIA_ROOT)+ static(STATIC_URL ,
                                                          document_root = STATIC_ROOT)
