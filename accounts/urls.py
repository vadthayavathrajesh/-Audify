from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('dashboard/',views.dashboard,name="video_list"),
    path('',views.home, name='home'),
    path('home/',views.home_page,name="home-page"),
    path('audio/<str:audio_fileName>/', views.audio_page, name='audio_page'),
    path('save_comments/', views.save_comments, name='save_comments'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
    path('login/', views.login_page, name="login"),
    path('logout/',views.logoutuser,name ="logout"),
    path('register/', views.register_page, name="register"),
    path('ytlink/',views.upload_youtube_video, name ="link"),
    path('delete_link/<int:link_id>/', views.delete_link, name='delete_link'),
    path('audio_page_links/<str:audio_fileName>/', views.audio_page_links, name="audio_page_links"),
    path('fblink/',views.upload_facebook_video, name="fblink"),
    path('fb_audio_page_links/<str:audio_fileName>/', views.fb_audio_page_links, name="fb_audio_page_links"),
    path('twitchlink/',views.upload_twitch_video, name="twitchlink"),
    path('twitch_audio_page_links/<str:audio_fileName>/', views.tw_audio_page_links, name="tw_audio_page_links"),
]
