from django.views.generic import DetailView, ListView
from .models import ReferenceStory

# Create your views here.
class ReferenceStoryView(DetailView):
    model = ReferenceStory
    template_name = "_reference_story_detail.html"

class ReferenceStoryListView(ListView):
    model = ReferenceStory
    template_name = "project.html"
    context_object_name = 'reference_list'