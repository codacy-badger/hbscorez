from django.shortcuts import render, get_object_or_404

from .models import Association


def show_all(request):
    associations = Association.objects.all()
    return render(request, 'associations/list.j2', {'associations': associations})


def detail(request, bhv_id):
    association = get_object_or_404(Association, bhv_id=bhv_id)
    return render(request, 'associations/detail.j2', {'association': association})
