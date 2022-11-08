from django.views.generic import ListView
from django.contrib.admin.views.decorators import staff_member_required
from .models import Contact
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class FeedbackView(ListView):
    template_name = 'feedback/feedback.html'
    model = Contact


@staff_member_required
def read_msg(request, pk):
    if request.user.is_staff:
        contact = get_object_or_404(Contact, pk=pk)
        contact.is_read = True
        contact.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@staff_member_required
def delete_msg(request, pk):
    if request.user.is_staff:
        comment = get_object_or_404(Contact, pk=pk)
        comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

