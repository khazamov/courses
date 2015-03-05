from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from workshops.models import Workshop, Registration
from django.shortcuts import render_to_response,get_object_or_404,redirect,render
from django.contrib.auth import logout, authenticate,login
from django.contrib.auth.decorators import login_required
import pdb


def login_user(request):
    logout(request)
    username = password = ''
    if request.GET:
        username = request.GET.get('username')
        password = request.GET.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
    return render_to_response('login/login.html', context_instance=RequestContext(request))

@login_required(login_url='/login_auth')
def profile(request):
    workshops_registered = []
    if request.user.is_authenticated():
        workshops_registered = request.user.workshop_set.all()
    c = RequestContext(request,{'workshops_registered':workshops_registered})
    template = loader.get_template('profile.html')
    return HttpResponse(template.render(c))




@login_required(login_url='url "login_auth"')
def remove_result(request, workshop_id):
       workshop_to_remove=get_object_or_404(Workshop,pk=workshop_id)
       reg_obj=get_object_or_404(Registration,user=request.user,workshop=workshop_to_remove)
       reg_obj.workshop = None
       reg_obj.save()
       del reg_obj
       template = loader.get_template('result.html')
       c = RequestContext(request,{'workshop_to_remove':workshop_to_remove})
       return HttpResponse(template.render(c))

@login_required(login_url='url "login_auth"')
def add_result(request,workshop_id):
    try:
       user_to_add = request.user
       workshop_to_add = get_object_or_404(Workshop, pk=workshop_id)
       reg = Registration.create(user_to_add,workshop_to_add)
       reg.save()
       c = RequestContext(request,{'workshop_to_add':workshop_to_add})
       template = loader.get_template('result.html')
       return HttpResponse(template.render(c))
    except Exception, msg:
        c = RequestContext(request,{'error_message':msg})
        template = loader.get_template('error.html')
        return HttpResponse(template.render(c))



def index(request):
    workshop_list = Workshop.objects.all()
    template = loader.get_template('base.html')
    context = RequestContext(request, {
        'workshop_list': workshop_list,
    })
    return HttpResponse(template.render(context))