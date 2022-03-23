from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView

from .forms import ReviewForm


class ReviewEmailView(FormView):
    form_class = ReviewForm
    template_name = 'celery_task/review.html'

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review!"
        return HttpResponse(msg)
