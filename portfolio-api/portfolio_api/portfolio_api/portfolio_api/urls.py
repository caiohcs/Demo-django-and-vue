from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    re_path('^admin/', admin.site.urls),
    path('api/', include('portfolio.urls')),

]
