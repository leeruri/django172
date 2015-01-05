#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import *

def views_render(request, view_url, context): 
	if request.session.get('user_email') != None :	
		context['session'] = request.session
	return render(request, view_url, context)

def main_page(request):
	context = {}
	return views_render(request, 'opinion/main_page.html', context)

def login_page(request):
	if request.method == 'POST':
		p_user_email = request.POST['user_email']
		p_user_pwd = request.POST['user_pwd']
		f_opinion_user = OpinionUser.objects.filter(user_email=p_user_email, user_pwd = p_user_pwd)
		if len(f_opinion_user) > 0 :
			request.session['user_email'] = p_user_email
			request.session['user_id'] = f_opinion_user[0].id
			request.session['user_nickname'] = f_opinion_user[0].user_nickname
			context = {'return_msg' : {'type':'info', 'msg':'hello '+f_opinion_user[0].user_nickname}}
			return views_render(request, 'opinion/main_page.html', context)
		else:
			form = OpinionUserLoginForm()
			context ={
			'return_msg' : {'type':'warning', 'msg':'Please check your Email/Password.'},
			'form' : form,
			}
			return views_render(request, 'opinion/login_page.html', context)			
	else:
		form = OpinionUserLoginForm()
		context = {
		'form' : form
		}
		return views_render(request, 'opinion/login_page.html', context)

def logout(request):
	del request.session['user_email']
	return main_page(request)

def write_page(request):
	if request.method == 'POST':  
		form = OpinionForm(request.POST)  
		if form.is_valid() :
			opinion = form.save()
			opinion.ip_address = get_client_ip(request)
			opinion.save()
			context = {
			'form' : form,
			}
			return view_page_query_no(request, opinion.id)
		else : 
			context = {
			'form' : form,
			}
			return views_render(request, 'opinion/write_page.html', context)

	else:	
		opinion = Opinion()
		opinion.writer_id = request.session['user_id'] 
		form = OpinionForm(instance=opinion)
		context = {
		'form' : form
		}
		return views_render(request, 'opinion/write_page.html', context)

def write_page_query_no(request, query):
	if request.method == 'GET':
		linked_opinion = Opinion.objects.get(id=query)
		print linked_opinion
		if linked_opinion:
			opinion = Opinion(linked_opinion_id=linked_opinion.id, writer_id=request.session['user_id'])
			form = OpinionForm(instance=opinion)
			context = {
			'form' : form,
			'return_msg' : {'type':'link', 'msg': u'〔'+linked_opinion.opinion_title+u'〕주제에 관해 작성하는 글입니다.'},
			}
			return views_render(request, 'opinion/write_page.html', context)

	else:	
		opinion = Opinion()
		opinion.writer_id = request.session['user_id'] 
		form = OpinionForm(instance=opinion)
		context = {
		'form' : form
		}
		return views_render(request, 'opinion/write_page.html', context)
 

def userinfo_page(request):
	if request.method == 'POST':

		form = OpinionUserForm()
		context = {
		'form' : form
		}
		return views_render(request, 'opinion/write_page.html', context)
 
def register_page(request):
	if request.method == 'POST':   
		p_user_email = request.POST['user_email']	 
		if len(OpinionUser.objects.filter(user_email=p_user_email)) > 0 :
			context = {
			'return_msg' :  {'type':'warning', 'msg':'already registerd user'},
			'form' : OpinionUserForm(),
			}
			return views_render(request, 'opinion/register_page.html', context)
		else :
			form = OpinionUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				user.ip_address = get_client_ip(request)
				user.save() 
				form = OpinionUserLoginForm()
				context = {
					'return_msg' : {'type':'info', 'msg':'register success.'},
					'form' : form,
				}
				return views_render(request, 'opinion/login_page.html', context) 
			else :
				context = {
					'return_msg' :  {'type':'warning', 'msg':'Please check this form.'},
					'form' : form,
				}
				return views_render(request, 'opinion/register_page.html', context)

	else:
		form = OpinionUserForm()
		context = {
		'form' : form
		}
		return views_render(request, 'opinion/register_page.html', context)

def view_page(request):
	opinions = Opinion.objects.all()
	for opinion in opinions:
		opinion.comment_count = len(Comment.objects.filter(opinion_id=opinion.id))
		opinion.linked_opinion_count = len(Opinion.objects.filter(linked_opinion_id=opinion.id))
		opinion.nickname = nicknameLink(opinion.writer_id)
	context = {'opinions' : opinions }
	return views_render(request, 'opinion/list_page.html', context)

def view_page_query_no(request, query): 
	obj = Opinion.objects.get(id=query) 
	obj.nickname = nicknameLink(obj.writer_id)
	obj.tag_name = tagLink(obj.tag_name)
	linked_opinion_id = 0
	if obj.linked_opinion_id:
		linked_opinion_id = obj.linked_opinion_id
	linked_parent_opinion = Opinion.objects.filter(id=linked_opinion_id) 
	linked_opinion_list = Opinion.objects.filter(linked_opinion_id=query) 
	opinion_comment_list = Comment.objects.filter(opinion_id=query) 
	comment = Comment(opinion_id=query, writer_id=request.session['user_id'])
	commentForm = CommentForm(instance=comment)
	if obj:
		context = {
		'opinion' : obj, 
		'commentForm' : commentForm, 
		} 
		if len(linked_opinion_list) > 0:
			for linked_opinion in linked_opinion_list :
				linked_opinion.writer = nicknameLink(linked_opinion.writer_id)
			context['linkedOpinions'] = linked_opinion_list
		if len(opinion_comment_list) > 0:
			for opinion_comment in opinion_comment_list :
				opinion_comment.writer = nicknameLink(opinion_comment.writer_id)
			context['comments'] = opinion_comment_list
		if len(linked_parent_opinion) == 1:
			context['linked_parent_opinion'] = linked_parent_opinion[0]
		return views_render(request, 'opinion/view_page.html', context)
	else:
		context = {
		'opinions' : Opinion.objects.all()
		}

		return views_render(request, 'opinion/list_page.html', context)

def view_page_query_tag(request, query): 
	opinions = Opinion.objects.filter(tag_name=query)
	for opinion in opinions:
		opinion.comment_count = len(Comment.objects.filter(opinion_id=opinion.id))
		opinion.linked_opinion_count = len(Opinion.objects.filter(linked_opinion_id=opinion.id))
		opinion.nickname = nicknameLink(opinion.writer_id)
	context = {'opinions' : opinions }
	return views_render(request, 'opinion/list_page.html', context)

def write_comment(request): 
	if request.method == 'POST':
		commentForm = CommentForm(request.POST)

		if commentForm.is_valid() : 
			comment = commentForm.save()  
			comment.ip_address = get_client_ip(request)
			comment.save()
			return  view_page_query_no(request, request.POST['opinion_id'])
		else: 
			obj = Opinion.objects.get(id=request.POST['opinion_id'])
			linked_opinion_list = Opinion.objects.filter(linked_opinion_id=request.POST['opinion_id']) 
			opinion_comment_list = Comment.objects.filter(opinion_id=request.POST['opinion_id']) 
			obj.nickname = nicknameLink(obj.writer_id)
			obj.tag_name = tagLink(obj.tag_name)
			if obj:
				context = {
				'opinion' : obj,
				'commentForm' : commentForm,
				} 
				if len(linked_opinion_list) > 0:
					for linked_opinion in linked_opinion_list :
						linked_opinion.writer = nicknameLink(linked_opinion.writer_id)
					context['linkedOpinions'] = linked_opinion_list
				if len(opinion_comment_list) > 0:
					for opinion_comment in opinion_comment_list :
						opinion_comment.writer = nicknameLink(opinion_comment.writer_id)
					context['comments'] = opinion_comment_list
				return views_render(request, 'opinion/view_page.html', context)
			else:
				context = {	
				'opinions' : Opinion.objects.all()
				}	
				return views_render(request, 'opinion/list_page.html', context) 

def nicknameLink(user_id):
	if user_id == None:
		return
	opinionUser = OpinionUser.objects.get(id=user_id)
	return "<a href='/user/"+str(opinionUser.id)+"/'>"+opinionUser.user_nickname+"</a>"
def tagLink(tag):
	if tag == None:
		return
	return "<a href='/view/tag/"+tag+"/'>"+tag+"</a>"

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip