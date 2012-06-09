#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from vpnauth.vpn.forms import VpnForm
from django.utils.translation import ugettext_lazy, ugettext as _
from django.template import RequestContext

ERROR_MESSAGE = "Please enter a correct username and password. "

def index(request):
        form = VpnForm()
        return render_to_response('vpn/edit.html',{'form': form},context_instance=RequestContext(request)) 

def save(request):
    if request.method == 'POST':
        form = VpnForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                newpasswd=User.objects.make_random_password(length=15, allowed_chars='_abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789')
                user.set_password(newpasswd)
                user.save()
                return render_to_response('vpn/password_change_done.html',{'newpasswd': newpasswd},context_instance=RequestContext(request)) 
#                return HttpResponseRedirect("/result")
            else:
                return HttpResponseRedirect("/error")

###		u=User.objects.create_user(username=cd['username'],password=cd['password'],email='')
####               u.save

                #return HttpResponseRedirect("/result")

    else:
        form = VpnForm()
    return render_to_response('vpn/edit.html',{'form': form},context_instance=RequestContext(request))


