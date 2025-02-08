# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# can use API view


# new function called index
def index(request):
    print(request.user)
    return render(request, 'index.html')
    # template = loader.get_template('index.html')
    #    return HttpResponse("Homepage!")
    # return HttpResponse(template.render({}, request))


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


class ProfileView(LoginRequiredMixin, TemplateView):
    # block profile page without log, will bring you to login page instead
    # ProfileView extends TemplateView
    template_name = 'accounts/profile.html'
