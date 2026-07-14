"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from Home.views import index, about,contact, success_page, recipe ,get_update_recipe,get_delete_recipe,user_login,user_register,user_logout
# from vege.views import recipe,delete_recipe,update_recipe,login_recipe,register_recipe,logout_recipe,get_student_report,student_report_detail
# for showing media files that was stored in the local folder
from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
       

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('success/', success_page, name='success'),
    # path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('recipe/', recipe, name='recipe'),
    path('get_delete_recipe/<int:recipe_id>',get_delete_recipe , name='get_delete_recipe'),
    path('get_update_recipe/<int:recipe_id>',get_update_recipe , name='get_update_recipe'),
    path('user_login/', user_login,name='user_login'),
    path('user_register/',user_register,name='user_register'),
    path('user_logout/', user_logout, name='user_logout'),
]

# for showing media files that was stored in the local folder
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     ...
# ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)