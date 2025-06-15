from django.urls import path
from . import views
urlpatterns = [
    path('records', views.get_records, name='record-list'),
    path('records/create', views.add_record, name='create-record'),
    path('records/<int:pk>/update', views.edit_record, name='update-record'),
    path('records/<int:pk>/delete', views.delete_record, name='delete-record'),

]