from django.db import models
from django.forms import ModelForm

class SubmitCode(models.Model):
    Index = models.CharField(max_length=2)
    file = models.FileField(upload_to="tmp/")

class SubmitCodeForm(ModelForm):
    class Meta:
        model = SubmitCode
        fields = ('file',)
