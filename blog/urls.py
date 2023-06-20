from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.index , name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("category/<slug:slug>",views.blogs_by_category,name ="blogs_by_category"),
    path("blogs/<slug:slug>", views.blogs_details,name="blogs_details"),  
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
 + static(settings.STATIC_URL,document_root=settings.STATIC_URL)
