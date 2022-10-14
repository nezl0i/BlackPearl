from posts.models import Category
from django.template import RequestContext

# request_context = RequestContext(request)
# request_context.push({
#     "categories": Category.objects.all(),

#     })

def categories(request):
    """
    Returns all available categories to template
    """
    return {"categories": Category.objects.all()}