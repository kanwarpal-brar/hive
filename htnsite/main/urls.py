from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name='index'),
	path("getstarted/", views.getstarted, name="getstarted"),
	path("contribute/", views.contribute, name="contribute"),
	path("faq/", views.faq, name="faq"),
]