from django.db import models
from .utils import excel_file_directory_path


class UserInformation(models.Model):
    start = models.PositiveIntegerField(verbose_name="START")
    provider_name = models.CharField(max_length=50, verbose_name="PROVIDER NAME")
    a_party = models.PositiveIntegerField(verbose_name="APARTY")
    b_party = models.PositiveIntegerField(verbose_name="BPARTY")
    call_duration = models.PositiveIntegerField(verbose_name="CALL DURATION")
    usage_type = models.CharField(max_length=10, verbose_name="USAGE TYPE")
    network_type = models.CharField(max_length=10, verbose_name="Network TYPE")
    mcc_start_a = models.PositiveIntegerField(verbose_name="MCCSTARTA")
    mnc_start_a = models.PositiveIntegerField(verbose_name="MNCSTARTA")
    lac_start_a = models.PositiveIntegerField(verbose_name="LACSTARTA")
    ci_start_a = models.PositiveIntegerField(verbose_name="CISTARTA")
    imei = models.PositiveIntegerField(verbose_name="IMEI")
    imsia = models.PositiveIntegerField(verbose_name="IMSIA")
    address = models.CharField(max_length=250, verbose_name="ADDRESS")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.a_party

    class Meta:
        ordering = ['-created_at']
        verbose_name = "User Information"
        verbose_name_plural = "User Information"
        db_table = "user_information"


class ExcelFile(models.Model):
    file = models.FileField(upload_to=excel_file_directory_path, verbose_name="Excel File")
