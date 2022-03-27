from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

from .models import UserInformation, ExcelFile


def export_excel(request):
    objects = UserInformation.objects.all()
    data = []

    for obj in objects:
        data.append({
            "start": obj.start,
            "provider_name": obj.provider_name,
            "a_party": obj.a_party,
            "b_party": obj.b_party,
            "call_duration": obj.call_duration,
            "usage_type": obj.usage_type,
            "network_type": obj.network_type,
            "mcc_start_a": obj.mcc_start_a,
            "mnc_start_a": obj.mnc_start_a,
            "lac_start_a": obj.lac_start_a,
            "ci_start_a": obj.ci_start_a,
            "imei": obj.imei,
            "imsia": obj.imsia,
            "address": obj.address
        })
    _datetime = datetime.now()
    pd.DataFrame(data).to_excel('excelhandling/output_{}.xlsx'.format(_datetime.strftime("%Y-%m-%d-%H-%M-%S")))
    return JsonResponse({'status': 200})


def import_excel(request):
    if request.method == "POST":
        file = request.FILES['file']
        obj = ExcelFile.objects.create(file=file)
        path = str(obj.file)
        final_path = f'{settings.MEDIA_ROOT}/{path}'
        objects = pd.read_excel(final_path)
        for obj in objects.values:
            print(obj)
        ExcelFile.objects.update()
    return render(request, 'excelhandling/upload.html')


'''
start
provider_name
a_party
b_party
call_duration
usage_type
network_type
mcc_start_a
mnc_start_a
lac_start_a
ci_start_a
imei
imsia
address
'''
