from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('palavra/', include('palavra.urls')),
    path('admin/', admin.site.urls),
]