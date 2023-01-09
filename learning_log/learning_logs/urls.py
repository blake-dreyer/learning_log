"""Define the URL Pattern for Learning Logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
    #Page that shows all topics
    path('topics/', views.topics, name='topics'),
    #Detail Page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Page for adding a new topic - User
    path('new_topic/', views.new_topic, name='new_topic'),
    #Page for adding a new entry - User
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]