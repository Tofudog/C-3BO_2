from django.urls import path
from . import views

from django.conf import settings
# from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path('citations/', views.citations, name="blog-citations"),
    #path("simple_function", views.simple_function),
    #path(r'button/', views.button, name="click_button")
    path('click_button/', views.click_button, name="click_button"),
    path('hospital/', views.hospital, name="hospital"),
    path('diagnose/', views.diagnose, name="diagnose"),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)