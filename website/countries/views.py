from django.shortcuts import render
from .serializers import CountrySerializer
from rest_framework.generics import ListCreateAPIView
from django.http import JsonResponse
from django.db.models import Sum

from .models import Country


class CountryListAPIView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


def home_view(request):
    return render(request, "base.html")


def bar_chart_view(request):
    return render(request, "bar_chart.html")


def pie_chart_view(request):
    return render(request, "pie_chart.html")


def line_chart_view(request):
    return render(request, "line_chart.html")


def bar_chart_view_data(request):
    labels = []
    data = []

    queryset = (
        Country.objects.all()
        .annotate(euro_pricing=Sum("lpg_euro"))
        .order_by("-euro_pricing")
    )
    for country in queryset:
        labels.append(country.name)
        data.append(float(country.lpg_euro.split(" ")[0]))

    return JsonResponse(
        data={
            "labels": labels,
            "data": data,
        }
    )


def pie_chart_view_data(request):
    labels = []
    data = []

    queryset = Country.objects.order_by("-lpg_euro")[:5]
    for country in queryset:
        labels.append(country.name)
        data.append(float(country.lpg_euro.split(" ")[0]))

    print(f"labels: {labels} \n data: {data}")
    return JsonResponse(
        data={
            "labels": labels,
            "data": data,
        }
    )


def pie_chart_view_embedded(request):
    labels = []
    data = []

    queryset = Country.objects.order_by("-lpg_euro")[:5]
    for country in queryset:
        labels.append(country.name)
        data.append(float(country.lpg_euro.split(" ")[0]))

    return render(
        request,
        "pie_chart_embedded.html",
        {
            "labels": labels,
            "data": data,
        },
    )


def line_chart_view_data(request):
    labels = []
    data = []

    queryset = Country.objects.all()[:10]
    for country in queryset:
        labels.append(country.name)
        data.append(float(country.lpg_euro.split(" ")[0]))

    print(f"labels: {labels} \n data: {data}")

    return JsonResponse(
        data={
            "labels": labels,
            "data": data,
        }
    )
