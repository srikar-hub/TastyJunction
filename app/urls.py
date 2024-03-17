from django.urls import *
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',home,name='home'),
    path('recipe',recipe_list,name='recipe'),
    path('source/<id>/',source,name='source'),
    path('search',search,name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)