from django.urls import path
from .views import RoomView, CategoryView

app_name = 'room'

urlpatterns = [
    path('list/', RoomView.as_view({'get': 'list'}), name="room_list"),
    path('category-list/', CategoryView.as_view({'get': 'list'}), name="category_list"),
]
