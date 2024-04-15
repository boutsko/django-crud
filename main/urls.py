from django.contrib import admin
from django.urls import path, include
# importing from app folder, the view file
from main.views import Home, Create, Detail,Update, Delete

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    path('create/', Create.as_view(), name='create'),
    path('<int:pk>/', Detail.as_view(), name='detail'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
]
