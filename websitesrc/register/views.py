# -*- coding:utf-8 -*- #
#! /usr/bin/env python
# Create your views here.
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
import string
import sys
import json
import time

from models import person
def sendMsg(request):
    cityList = ["北京"]
    for city in cityList:
        date = time.strftime("%d/%m/%Y")
        info = getInfo(city)
        mailto_list = getEmail(city)
        content = produceMsg(info)
        send_mail(mailto_list, "内涝通知("+date+")", content)
    return HttpResponseRedirect('/')

def getEmail(city):
    peoples = person.objects.filter(city=city)
    emails  = []
    for people in peoples:
        emails.append(people.email)
    return emails
def reg_table(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name  = request.POST.get('name')
        city  = request.POST.get('city')
        newPerson = person(email = email, name = name, city = city)
        try:
            tmp = person.objects.get(email = email)
            print "exist"
            return render_to_response('tmpFail.html',locals(),context_instance=RequestContext(request))
        except:
            print "not exist"
            newPerson.save()
            return render_to_response('tmpSuccess.html',locals(),context_instance=RequestContext(request))
    else:
        list = person.objects.all()
        for item in list:
            name = item
        return render_to_response('register.html',locals(),context_instance=RequestContext(request))




def getInfo(city):
    try:
        url = 'http://api.map.baidu.com/geosearch/v3/local?'
        urlTest = 'http://api.map.baidu.com/geosearch/v3/local?q=&ak=7xfCf9eh3Gdfdf4U2UoCqNxC&geotable_id=63787&region=%E5%8C%97%E4%BA%AC'
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        values = {
            'geotable_id'       : 63787,
            'ak'                : '7xfCf9eh3Gdfdf4U2UoCqNxC',
            'q'                 : '',
            'region'            : city
        }
        data = urllib.urlencode(values)
        # req = urllib2.Request(url, data)
        urlTest = url+data
        #print urlTest
        reqTest = urllib2.Request(urlTest)

        response = urllib2.urlopen(reqTest)
        res_page = response.read()
        res_json = json.loads(res_page)

        print  res_json['status'],  # 输出服务器返回信息
        print  res_json['total']
        return  res_json['contents']
    except:
        print "request error"

def produceMsg(infoList = []):
    date = time.strftime("%d/%m/%Y")
    date = '14/06/2013'
    dateParts = date.split('/', 2)
    currentDay   = dateParts[0]
    currentMonth = dateParts[1]
    currentYear  = dateParts[2]
    msg = ""
    for info in infoList:
        date  = info['hz_date']
        parts = date.split('-',2)
        day   = parts[1]
        month = parts[0]
        year  = parts[2]
        if currentYear == year and currentMonth == month and currentDay == day:
            msg = msg + info['title'] + "\n"
    return msg

import smtplib
from email.mime.text import MIMEText

def send_mail(to_list,sub,content):
    # 设置服务器，用户名，口令以及邮箱的后缀
    mail_host="smtp.126.com"
    mail_user="testinglife@126.com"
    mail_pass="jianchi000"
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = mail_user
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(mail_user, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False