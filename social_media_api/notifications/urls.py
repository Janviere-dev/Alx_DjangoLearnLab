from django.urls import path
from .views import NotificationListView
from .views import user_notifications

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
    path('', user_notifications, name='user-notifications'),
]
