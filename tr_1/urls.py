from django.contrib import admin
from django.urls import path
from career_map import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.log),
    path('show/', views.show),
    path('log',views.log),
    path('login',views.su),
    path('ret/',views.ret),
    path('ret',views.ret),
    path('add',views.add),
    path('reset_password',views.reset_password),
    path('check',views.check),
    path('reset/<id>',views.change),
    path('go_to_login',views.go_to_login),
    path('add_details',views.add_details),
    path('about_us',views.about_us),
    path('home',views.home),
    path('post_jobs',views.post_jobs),
    path('verify',views.poster),#######
    path('register the recruter',views.register_the_recruter),
    path('recruter_forgot_password',views.recruter_forgot_password),
    path('check_recrutor',views.check_recrutor),
    path('reset_recrutor/<id>',views.change_recrutor_password),
    path('info',views.info),
    path('check post',views.new_post),
    path('add job',views.add_job),
    path('new_post',views.new_post),
    path('search',views.search),
    path('contact_details',views.contact_details),
    path('service',views.service),
    path('conditions',views.conditions),
    path('logins',views.logins),
    path('apply',views.apply),
    path('emails',views.emails),



]
