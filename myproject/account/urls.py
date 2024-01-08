from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name='about'),
    path('home/page/', views.homePage, name='homeV1'),
    path('test/home/<int:first>/<int:second>/', views.testHome, name='test'),
    path('test/home/<int:first>/', views.testHome, name='test1'),
    path('extend/base/', views.extend, name='extendBase'),
    path('extend/home', views.extend2, name='extendHome'),
    # path('test/home/<int:year>/<int:month>/<int:day>', views.testDate, name='test2'),
    # path('test/home/<int:year>/<int:month>', views.testDate, name='test2'),
    # path('test/home/<int:year>', views.testDate, name='test2'),
    path('human/', views.testHuman, name='testHuman')
]