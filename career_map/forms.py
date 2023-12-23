from django import forms
from career_map.models import persion_detail
from career_map.models import post_job
from career_map.models import jobs

class persion_detailForm(forms.ModelForm):
    class Meta:
        model=persion_detail
        fields="__all__"

class post_jobForm(forms.ModelForm):
    class Meta:
        model=post_job
        fields="__all__"
class jobsForm(forms.ModelForm):
    class Meta:
        model=jobs
        fields="__all__"