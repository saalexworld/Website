"""
================R_O_U_T_E_R==============

"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),  # при переходе на страницу ""(главная)
    # отсылает к юрлс из приложения хелло
    path('news/', include('news.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
