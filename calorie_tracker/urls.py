from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from app.views import food_list, add_food, edit_food, delete_food

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', add_food, name='add_food'),
    path('food_list', food_list, name='food_list'),
    path('edit_food/<int:food_id>/',edit_food, name='edit_food'),
    path('delete_food/<int:food_id>/', delete_food, name='delete_food'),
    # path('register', register, name='register'),
    # path('login',LoginView.as_view(template_name='user_login.html'), name='login'),

]