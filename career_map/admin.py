from django.contrib import admin
from career_map.models import persion_detail,post_job,jobs

# Register your models here.
class persion_detailAdmin(admin.ModelAdmin):
    list=["user_name","password","phone_number","mail_id","resume","domain"]
    radio_fields = {
        'domain':admin.HORIZONTAL
    }

class postAdmin(admin.ModelAdmin):
    list=["user_name","password","mail_id","company_name"]


class jobsAdmin(admin.ModelAdmin):
    list=["job_title","job_description","contact","company_name"]


admin.site.register(persion_detail,persion_detailAdmin)
admin.site.register(post_job,postAdmin)
admin.site.register(jobs,jobsAdmin)