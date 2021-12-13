from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Language, Entry
from .forms import EntryCreationForm, EntryMultipleCreationForm, CountryCreationForm


def select_searching(request):
    form = EntryCreationForm()
    if request.is_ajax():
        term = request.GET.get('term')
        languages = Language.objects.all().filter(title__contains=term)
        response_content = list(languages.values())
        return JsonResponse(response_content, safe=False)
    if request.method == "POST":
        form = EntryCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sel:select-search')
        else:
            return redirect('home:home')
    return render(request, 'select_two/single_select.html', {'form': form})


def select_multiple(request):
    form = EntryMultipleCreationForm()
    languages = Language.objects.all()
    if request.method == "POST":
        form = EntryMultipleCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sel:select-multiple')
        else:
            return redirect('home:home')
    context = {
        'form': form,
        'languages': languages
    }
    return render(request, 'select_two/multiple_select.html', context)


def array_country_name(request):
    form = CountryCreationForm()
    if request.method == "POST":
        form = CountryCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            print(instance.name)
            form.save()
            return redirect('sel:country-multiple')
        else:
            return redirect('home:home')
    context = {
        'form': form,
    }
    return render(request, 'select_two/country.html', context)
