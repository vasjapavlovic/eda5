from django.shortcuts import render

from django.views.generic import TemplateView


class RazdelilnikHomeView(TemplateView):
    template_name = "razdelilnik/home.html"