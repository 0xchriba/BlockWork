from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from . import myforms
from web3 import Web3
from . import utils
from . import modelo
from django.http import HttpResponseRedirect
from django.urls import reverse
import os

class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


class FindFreelancerPage(generic.TemplateView):
    template_name = "find_freelancer.html"

    def get(self, request):
        form = myforms.FindFreelancerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = myforms.FindFreelancerForm(request.POST)
        if form.is_valid():
            project_skills = form.cleaned_data['Project_Skills']
            project_skills_html = ""
            for skill in project_skills[:-1]:
                project_skills_html += skill + ", "
            project_skills_html += "and " + project_skills[-1] + "."
        return render(request, self.template_name, {'form': form, 'project_skills': project_skills_html})

class NewProjectPage(generic.TemplateView):
    template_name = "new_project.html"

    def get(self, request):
        form = myforms.NewProjectForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = myforms.NewProjectForm(request.POST)
        if form.is_valid():
            project_title = form.cleaned_data['Project_Title']

        project_title = form.cleaned_data['Project_Title']
        project_desc = form.cleaned_data['Project_Description']
        project_amount = form.cleaned_data['Project_Amount']

        ''' THIS NEEDS TO BE WORKED ON look at myforms.py'''
        milestone_descriptions = form.cleaned_data['Milestone_Descriptions']

        utils.run_generate_contract("alice", project_title, project_desc, int(project_amount), milestone_descriptions)


        text = utils.get_info()

        project_title_html = 'Project Title: ' + project_title
        project_desc_html = 'Project Description: ' + project_desc
        project_amount_html = 'Project Amount: ' + project_amount
        args = {
            'form': myforms.NewProjectForm(),
            'project_title' : project_title_html,
            'project_desc' : project_desc_html,
            'project_amount' : project_amount_html,
            }
        return render(request, self.template_name, args)


def SubmitCodePage(request):
    template_name = "submit_code.html"
    if request.method=="POST":
        print(dir(myforms.GetIndexForm(request.POST)))
        get_index = myforms.GetIndexForm(request.POST)
        i = get_index.data['Get_Index']
        file = modelo.SubmitCodeForm(request.POST, request.FILES)
        if file.is_valid():
            file.save()
            path = "media/tmp/" + file.cleaned_data['file'].name
            hash = utils.ipfs_upload(path)
            print(hash)
            os.remove(path)
            print("File Removed!")

            percent = utils.update_milestones(int(i), hash)
            if percent == 100:
                return HttpResponseRedirect(reverse("finish-project"))

            # render(request,"code_result.html",{'percent': percent})
            return HttpResponseRedirect(reverse("code-result"))
    else:
        get_index = myforms.GetIndexForm()
        file = modelo.SubmitCodeForm()
    files = modelo.SubmitCode.objects.all()
    return render(request,template_name,{'form':file,'files': files, 'get_index' : get_index})


def CodeResultPage(request):
    template_name = "code_result.html"
    state = utils.get_status()
    status = state[0]
    url = utils.ipfs_domain + state[1]
    return render(request, template_name, {'status': status, 'url':url})

class FinishProjectPage(generic.TemplateView):
    template_name = "finish_project.html"

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        funds = utils.finish_project()
        print(funds)
        return render(request, self.template_name, {'F': funds['F Pay'], 'B': funds['B Pay'], 'A': funds['A Pay']})



def ProjectStatusPage(request):
    template_name = "project_status.html"
    status = utils.get_status()
    code = utils.ipfs_download(status[1])
    print(code)
    return render(request, template_name, {'status': status, 'code': code})

def ProjectHistoryPage(request):
    template_name = "project_history.html"
    history = utils.get_history()
    print(history[0])
    return render(request, template_name, {'history': history})
