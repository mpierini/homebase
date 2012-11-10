from django.shortcuts import render_to_response, render

def home(request):
	return render_to_response('dashboard/home.html')