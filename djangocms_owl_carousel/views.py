from django.shortcuts import render
from django.views.generic import DetailView
from .models import ReferenceStory

# Create your views here.
class ReferenceStoryView(DetailView):
    model = ReferenceStory
    template_name = "_reference_story_detail.html"
