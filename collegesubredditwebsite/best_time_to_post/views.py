"""
References: 
https://www.youtube.com/watch?v=F5mRW0jo-U4
https://stackoverflow.com/questions/61936775/how-to-pass-matplotlib-graph-in-django-template
PA3 from CMSC 12200
"""

from django.shortcuts import render
from django import forms
from jingwen_scores_trend import main

# Create your views here.

from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np

def graphic(res):

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    return graphic

class SearchForm(forms.Form):
    start_date = forms.CharField(
        label='Start Date',
        help_text=("""In the form: MM/DD/YY.
         Earliest date for each college is as follows:
         Caltech: 04/14/11,
          Harvard: 09/13/19,
           JHU: 07/13/20,
            MIT: 10/07/19,
             Princeton: 04/01/15,
              Stanford: 08/24/20,
               UChicago: 07/30/20,
                UPenn: 10/05/20,
                 Yale: 06/28/18,
                  Columbia: 11/22/20"""),
        required=True)
    end_date = forms.CharField(
        label='End Date',
        help_text=("In the form: MM/DD/YY"),
        required=True)
    college = forms.CharField(
        label='College',
        help_text=("""e.g. UChicago"""),
        required=True)

def best_time_to_post_view(request):
    form = SearchForm()
    context = {}
    res = None
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        context["form"] = form
        if form.is_valid():
            args = {}
            if form.cleaned_data['start_date'] and form.cleaned_data['end_date']:
                args['time frame'] = (form.cleaned_data['start_date'], form.cleaned_data['end_date'])
            college = form.cleaned_data['college']
            if college:
                args['college'] = college
            res = main(args)
    # Handle different responses of res
    if res is None:
        context['result'] = None
    else:
        graphic1 = graphic(res)
        context["graphic"] = graphic1

    return render(request, 'best_time_to_post.html', context)