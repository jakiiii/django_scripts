from django.db.models import Q, Count
from django.shortcuts import render

from dfilters.models import Author, Category, Journal


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    categories = Category.objects.all()
    journal_qs = Journal.objects.all()

    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category')
    reviewed = request.GET.get('reviewed')
    not_reviewed = request.GET.get('not_reviewed')

    if is_valid_queryparam(title_contains_query):
        journal_qs = journal_qs.filter(title__icontains=title_contains_query)

    elif is_valid_queryparam(id_exact_query):
        journal_qs = journal_qs.filter(id=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        journal_qs = journal_qs.filter(
            Q(title__icontains=title_or_author_query) |
            Q(author__name__icontains=title_or_author_query)
        ).distinct()

    if is_valid_queryparam(view_count_min):
        '''
        gt = greater than
        gte = greater than or equal
        '''
        journal_qs = journal_qs.filter(views__gte=view_count_min)

    if is_valid_queryparam(view_count_max):
        '''
        lt = less than
        lte = less than or equal
        '''
        journal_qs = journal_qs.filter(views__lt=view_count_max)

    if is_valid_queryparam(date_min):
        journal_qs = journal_qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(date_max):
        journal_qs = journal_qs.filter(publish_date__lt=date_max)

    if is_valid_queryparam(category) and category != 'Choose...':
        journal_qs = journal_qs.filter(categories__name=category)

    if reviewed == 'on':
        journal_qs = journal_qs.filter(reviewed=True)
    elif not_reviewed == 'on':
        journal_qs = journal_qs.filter(reviewed=False)

    return journal_qs


def filter_view(request):
    template_name = 'dfilters/djfilter_form.html'
    journal_qs = filter(request)

    context = {
        'categories': Category.objects.all(),
        'journal_qs': journal_qs,
    }
    return render(request, template_name, context)
