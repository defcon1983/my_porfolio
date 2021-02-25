"""my_porfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import index, detalles, mis_datos, skill_detalles, Error404, Error505
from django.conf.urls import handler404, handler500

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('project/<int:project_id>/', detalles, name="detalles"),
    path('mis-datos/<int:mis_datos_id>/', mis_datos, name="mis_datos"),
    path('skill-detalles/<int:skill_detalles_id>/', skill_detalles, name="skill_detalles"),
    

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = Error404.as_view()

handler500 = Error505.as_error_view()