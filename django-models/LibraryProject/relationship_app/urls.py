
from django.urls import path
from .views import list_books, LibraryDetailView
from django.urls import path
from .views import user_login, user_logout, register
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
        path('books/', list_books, name='list_books'),
        path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
        path('relationship/', include('relationship_app.urls')),
]


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

]


