from django import forms
from . import utils


class NewProjectForm(forms.Form):
    Project_Title = forms.CharField(label= "Project Title")
    Project_Description = forms.CharField(label= "Project Description", widget=forms.Textarea)
    Project_Amount = forms.CharField(label= "Project Amount", max_length=7)
    Milestone_Descriptions = forms.TypedMultipleChoiceField(choices=[(str(x), str(x)) for x in range(1, 11)])

class FindFreelancerForm(forms.Form):
    Project_Skills = forms.TypedMultipleChoiceField(choices=[(x,x) for x in utils.skills])

class GetIndexForm(forms.Form):
    Get_Index = forms.CharField(max_length=2)
