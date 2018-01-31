from django.shortcuts import render

def monthly_table(requests) :
    return render(requests, 'data/monthly_table.html', {})