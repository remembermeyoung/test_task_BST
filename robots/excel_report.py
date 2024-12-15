from datetime import date, timezone, timedelta, datetime
from django.db.models import Count
from openpyxl.styles import Alignment, Side, Border
from robots.models import Robot
from openpyxl import Workbook

thins = Side(border_style="thin", color="000000")


# функция для заполнения строки + применение стилей
def row_fill(columns, ws, row_data, row, new_ws=False):
    if new_ws:
        titles = ['Модель', 'Версия', 'Количество за неделю']
        for i in range(len(columns)):
            ws[f'{columns[i]}{row-1}'] = titles[i]
            ws[f'{columns[i]}{row-1}'].border = Border(top=thins, bottom=thins, left=thins, right=thins)
            ws[f'{columns[i]}{row-1}'].alignment = Alignment(horizontal='center')
        ws.column_dimensions['D'].width = 25
    for i in range(len(columns)):
        ws[f'{columns[i]}{row}'] = row_data[i]
        ws[f'{columns[i]}{row}'].border = Border(top=thins, bottom=thins, left=thins, right=thins)
        ws[f'{columns[i]}{row}'].alignment = Alignment(horizontal='center')


# основная функция формирования отчёта
def robots_report():
    wb = Workbook()

    start_date = datetime.now() - timedelta(days=7)
    end_date = datetime.now()
    data = (
        Robot.objects.values_list('model', 'version').
        annotate(robot_count=Count('*'))
        .filter(created__range=[start_date, end_date])
        .order_by('model')
    )
    # <QuerySet_Output_Example -> [('R2', 'D2', 12), ('R2', 'D3', 2), ('R2', 'D4', 15), ('R3', 'D4', 26)]>

    columns = ['B', 'C', 'D']
    row = 3
    current_model = ''

    for tup in data:
        if tup[0] != current_model:
            row = 3
            current_model = tup[0]
            ws = wb.create_sheet(current_model)
            row_fill(columns, ws, tup, row, new_ws=True)
            row += 1
        else:
            ws = wb[current_model]
            row_fill(columns, ws, tup, row)
            row += 1

    wb.remove(wb['Sheet'])
    wb.save('report.xlsx')
