from django.urls import path, include
from .views import custom_users, custom_user_detail, category, category_detail, post, post_detail

urlpatterns = [
    path('custom_users', custom_users),
    path('custom_user/<int:pk>/', custom_user_detail),
    path('category/', category),
    path('category/<int:pk>/', category_detail),
    path('post/', post),
    path('post/<int:pk>/', post_detail),

    path('auth/', include('dj_rest_auth.urls'))
]

