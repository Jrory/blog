# encoding:utf8
from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from app.models import UserInfo, Publisher
from app.form import PublisherForm
from django.contrib.auth.models import User

import logging
logger = logging.getLogger('blog.views')

# Create your views here.

# def index(request, name, pwd):


def index(request):
	result = UserInfo.objects.all()
	user = "Rory"
	return render(request, 'test.html',locals())


def delete(request, name):
	UserInfo.objects.filter(username=name).delete()
	result = UserInfo.objects.all()
	return render_to_response('test.html', {'data': result, 'user': 'Rory'})


def base(request):
	return render_to_response('master_templates/master.html', )


def login(request):
	if request.method == "POST":
		user = request.POST.get('username', None)
		pwd = request.POST.get('pwd', None)
		print user, pwd
		if UserInfo.objects.filter(username=user, password=pwd).count() == 1:
			return render_to_response('tag.html', {'username': user})

		else:
			return render_to_response('login.html', {'status': "用户名或密码错误"})
	else:
		return render_to_response('login.html')


def user(request):
	data = User.objects.all()
	return render_to_response('userinfo.html', locals())


def add(request):
	if request.method == "POST":
		# 使用 Django From情况
		# publisher_form = PublisherForm(request.POST)
		# if publisher_form.is_valid():
		# 	Publisher.objects.create(
		# 		name=publisher_form.cleaned_data['name'],
		# 		address=publisher_form.cleaned_data['address'],
		# 		city=publisher_form.cleaned_data['city'],
		# 		state_province=publisher_form.cleaned_data['state_province'],
		# 		country=publisher_form.cleaned_data['country'],
		# 		website=publisher_form.cleaned_data['website'],
		# 	)
		# return redirect("/app/base")

		# 使用Django ModelsForm情况
		publisher_form = PublisherForm(request.POST)
		if publisher_form.is_valid():
			publisher_form.save()
		return redirect("/app/base")
	else:
		publisher_form = PublisherForm()
		return render(request, "add_publisher.html", locals())


def app(request):
	return HttpResponse("OK")