from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from jobs.models import job_city_list, job_type_list, Jobs
from django.forms.models import model_to_dict
from django.http import Http404


def jobl_list(request):
    job_list = Jobs.objects.order_by('job_type')
    # for i in job_list:
    #     info = {}
    #     i = model_to_dict(i)
    #     for c in job_city_list:
    #         if c[0] == i['job_city']:
    #             info['job_city'] = c[1]
    #             break
    #     for t in job_type_list:
    #         if t[0] == i['job_type']:
    #             info['job_type'] = t[1]
    #             break
    #     info['job_name'] = i['job_name']
    #     context.append(info)
    # return render(request, 'jobs.html', {'job_list': context})

    context = {'job_list':job_list}
    for job in job_list:
        job.job_city = job_city_list[job.job_city][1]
        job.job_type = job_type_list[job.job_type][1]

    template = loader.get_template('jobs.html')
    return HttpResponse(template.render(context))


def job_detail(request,job_id):
    try:
        job = Jobs.objects.get(pk=job_id)
        job.job_city = job_city_list[job.job_city][1]
        context = {'job': job}
    except Jobs.DoesNotExist:
        raise  Http404('Jobs DoesNotExist')

    return render(request,'job.html',context)