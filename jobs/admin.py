from django.contrib import admin

# Register your models here.
from jobs.models import Jobs

class JobsAdmin(admin.ModelAdmin):
    """
    列表展示
    """
    exclude = ('create','create_date','modified_data')
    # 列表隐藏字段
    list_per_page = 1
    list_display = ('job_name','job_type','job_city','create','create_date','modified_data')
    # 展示字段

    # 保存
    def save_model(self, request, obj, form, change):
        obj.create = request.user
        super().save_model(request, obj, form, change)




admin.site.register(Jobs,JobsAdmin)
# 注册JobsAdmin

