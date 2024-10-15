from .import views
from django.urls import path


urlpatterns=[
    path('',views.add,name='add'),
    path('details',views.details,name='details'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvDetails/<int:pk>/',views.TaskDetailView.as_view(),name='cbvDetails'),
    path('cbvUpdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvUpdate'),
    path('cbvDelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvDelete')
]