from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

# 候选人学历
DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))

job_type_list = [
    (0, '开发'),
    (1, '运营'),
    (2, '设计'),
]

job_city_list = [
    (0, '北京'),
    (1, '上海'),
    (2, '深圳'),
]


class Jobs(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=job_type_list, verbose_name='职位类型')
    job_name = models.CharField(max_length=200,blank=False,verbose_name='职位名称')
    job_city = models.SmallIntegerField(blank=False, choices=job_city_list, verbose_name='职位类型')
    job_responsibilty = models.TextField(blank=False,max_length=1024,verbose_name='职位职责')
    job_requirement = models.TextField(blank=False, max_length=1024, verbose_name='职位要求')
    create = models.ForeignKey(User,verbose_name='创建人',on_delete=models.SET_NULL,null=True,default='admin')
    create_date = models.DateTimeField(verbose_name='创建日期',default=datetime.now)
    modified_data = models.DateTimeField(verbose_name='修改日期',default=datetime.now)