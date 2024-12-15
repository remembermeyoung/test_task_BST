import mimetypes
import os
from django.conf import settings
from django.db.models import Count

from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from openpyxl.workbook import Workbook

from robots.excel_report import robots_report
from robots.models import Robot


def download_file(request):
    # fill these variables with real values
    # fl_path = os.getcwd() + '\\robots\Book.xlsx'
    # filename = 'Book.xlsx'
    #
    # fl = open(fl_path, 'r')
    # mime_type, _ = mimetypes.guess_type(fl_path)
    # response = HttpResponse(fl, content_type=mime_type)
    # response['Content-Disposition'] = 'attachment; filename=%s' % filename
    # return response

    robots_report()
    file = os.path.join(settings.BASE_DIR, 'report.xlsx')
    flopen = open(file, 'rb')
    return FileResponse(flopen)


