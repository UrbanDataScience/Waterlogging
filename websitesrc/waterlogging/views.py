#!/usr/bin/env python
# coding: utf-8

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>Honghe home page!</h1> <a href=\"hello\">hello</a>.")

from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.conf import global_settings
from django.contrib import auth
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS

import urllib
import urllib2

def index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))
def graph(request):
    cityName = request.POST.get('city')
    # url = "http://api.map.baidu.com/geosearch/v3/local"
    # values = {
    #     'q'          : '',
    #     'filter'     : '',
    #     'radius'     : 1000,
    #     'geotable_id': 61976,
    #     'region'     : cityName,
    #     'page_index' : 0,
    #     'page_size'  : 10,
    #     'ak'         : 'XGyE1v4MgjGyiw1DObKCu7xs'
    # }
    # data = urllib.urlencode(values)
    # request = urllib2.Request(url, data)
    # response   = urllib2.urlopen(request)
    # the_page   = response.read()
    data = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,11, 12]
    return render_to_response('graph.html',locals(),context_instance=RequestContext(request))