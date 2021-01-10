from django.urls import path, re_path
from jobs import views

urlpatterns = [
    # 职位列表
    # path(r'^joblist/', views.joblist, name='joblist'),
    path('joblist/', views.jobl_list, name='job_list'),
    # path("job/(?P<job_id>\d+)/$", views.job_detail, name='job_detail'),
    path("job/<job_id>", views.job_detail, name='job_detail'),

]



