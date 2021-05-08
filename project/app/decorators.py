from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

def manager_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'staff':
			return redirect('home')

		if group == 'manager':
			return view_func(request, *args, **kwargs)
		
		if group==None:
			return HttpResponse('You are not authorized to view this page')

	return wrapper_function