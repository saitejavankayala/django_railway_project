import datetime
import time
from random import randint

from django.contrib import messages
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from online.models import station, train


def index(request):
    name = station.objects.all()
    return render(request, 'main.html', {'stations': name})


def checkpoint(request):
    if request.method == 'POST':
        from1 = request.POST.get('from')
        date = request.POST.get('date')
        year, month, day = (int(i) for i in date.split('-'))
        born = datetime.date(year, month, day)
        date = born.strftime("%A")

        from_id = station.objects.get(station_name=from1).station_name
        last = request.POST.get('to')
        last_id = station.objects.get(station_name=last).station_name
        from2 = train.objects.filter(stops__contains=[from_id, last_id]).values_list('train_name', flat=True)

        weekday = train.objects.filter(days__contains=[date]).values_list('train_name', flat=True)
        from3 = train.objects.filter(stops__contains=[from_id, last_id]).values_list('train_id', flat=True)
        if from1 == last:
            messages.info(request, 'from and to not be same')
            name = station.objects.all()
            return render(request, 'main.html', {'stations': name, 'date': date})
        elif from1 > last and list(weekday) == list(from2):

            return render(request, 'checkpoint.html',
                          {'from': from2, 'from1': from3, 'from_id': from_id, 'last_id': last_id, 'is': from1,
                           'last': last})
        else:
            return HttpResponse("No trains found!!!")


def end(request):
    return redirect('/')


def display(request):
    if request.method == 'POST':
        seat = request.POST.get('seat')
        sai2 = request.POST.get('stations')
        t = request.POST.get('t')
        last = request.POST.get('last')
        seattype = request.POST.get('seattype')
        seat2 = request.POST.get('seat2')
        sp = request.POST.get('sp')
        pnr = request.POST.get('pnr')
        ep = request.POST.get('ep')
        pn = request.POST.get('pd')
        pa = request.POST.get('pa')
        gender = request.POST.get('gender')
        td = request.POST.get('td')
        berth = request.POST.get('berth')
        seat10 = request.POST.get('seat10')

        return render(request, 'display.html',
                      {'stations': sai2, 'from': t, 'to': last, 'seat': seat, 'st': seattype, 'berth': seat2, "sp": sp,
                       'pnr': pnr, 'ep': ep, 'pn': pn, "pa": pa, "gender": gender, "td": td, "berth1": berth,"seat10":seat10})


def fill(request):
    if request.method == 'POST':
        button = int(request.POST.get('button'))
        last = request.POST.get('last')
        t = request.POST.get('from')

        sai = train.objects.filter(stops__contains=[t, last]).values_list('train_name', flat=True)
        sai2 = sai[button - 1]
        sp = train.objects.get(train_name=sai2).startpoint
        ep = train.objects.get(train_name=sai2).endpoint
        td = train.objects.get(train_name=sai2).train_id

        pnr = randint(1000000000, 9999999999)
        seat = randint(100, 999)
        seat1 = int(seat % 8)
        if seat1 == 1:
            seat2 = "Lower"
        elif seat1 == 2:
            seat2 = "Middle"
        elif seat1 == 3:
            seat2 = "Upper"
        elif seat1 == 4:
            seat2 = "Lower"
        elif seat1 == 5:
            seat2 = "Middle"
        elif seat1 == 6:
            seat2 = "UpperSide"
        elif seat1 == 7:
            seat2 = "Side Lower"
        elif seat1 == 8:
            seat2 = "Side Upper"
        seattype = train.objects.filter(train_name=sai2).values_list('seattype', flat=True)
        seattype = seattype[0]
        return render(request, 'sample.html',
                      {'stations': sai2, 'from': t, 'to': last, 'seat': seat1, 'st': seattype, 'berth': seat2, "sp": sp,
                       'pnr': pnr, 'ep': ep, "td": td})


class TrainList(ListView):
    model = train


class TrainView(DetailView):
    model = train


class TrainCreate(CreateView):
    model = train
    fields = ['train_name', 'train_id', 'startpoint', 'endpoint', 'stops', 'days', 'seats', 'seattype']
    success_url = reverse_lazy('train_list')


class TrainUpdate(UpdateView):
    model = train
    fields = ['train_name', 'train_id', 'startpoint', 'endpoint', 'stops', 'days', 'seats', 'seattype']
    success_url = reverse_lazy('train_list')


class TrainDelete(DeleteView):
    model = train
    success_url = reverse_lazy('train_list')


class TrainForm(ModelForm):
    class Meta:
        model = train
        fields = ['train_name', 'train_id', 'startpoint', 'endpoint', 'stops', 'days', 'seats', 'seattype']


def train_list(request, template_name='train_list.html'):
    trains = train.objects.all()
    data = {}
    data['object_list'] = trains
    return render(request, template_name, data)


def train_view(request, pk, template_name='train_details..html'):
    trains = get_object_or_404(train, pk=pk)
    return render(request, template_name, {'object': trains})


def train_create(request, template_name='train_form.html'):
    form = TrainForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('train_list')
    return render(request, template_name, {'form': form})


def train_update(request, pk, template_name='train_form.html'):
    trains = get_object_or_404(train, pk=pk)
    form = TrainForm(request.POST or None, instance=trains)
    if form.is_valid():
        form.save()
        return redirect('train_list')
    return render(request, template_name, {'form': form})


def train_delete(request, pk, template_name='train_confirm_delete.html'):
    trains = get_object_or_404(train, pk=pk)
    if request.method == 'POST':
        trains.delete()
        return redirect('train_list')
    return render(request, template_name, {'object': trains})


def alogin(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        if username == "saiteja" and password == "1234":
            return redirect('train_list')
        else:
            messages.info(request, 'invalid cerdentials')
            return redirect('alogin')
    else:
        return render(request, 'alogin.html')
