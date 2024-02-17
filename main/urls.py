from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('story/', views.story, name='story'),
    # path('contact/', views.contact, name='contact'),
    path('contact/qform', views.contact, name='qform'),
    path('contact/task', views.task, name='task'),
    path('menu/<int:pk>', views.FoodDetailView.as_view(), name='food_detail'),
    path('menu/<str:type>', views.menu_filter, name='filter'),

]