import os
from django.conf import settings
from django.http import FileResponse
from robots.excel_report import robots_report


def download_file(request):
    robots_report()
    file = os.path.join(settings.BASE_DIR, 'report.xlsx')
    flopen = open(file, 'rb')
    return FileResponse(flopen)
