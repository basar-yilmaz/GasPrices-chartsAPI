from django.contrib import admin
from django.urls import path
from countries import views

urlpatterns = [
    path("admin/", admin.site.urls, name="admin_page"),
    path("countries/", views.CountryListAPIView.as_view(), name="country_list"),
    
    path("", views.home_view, name="home"),
    
    path("bar-chart/", views.bar_chart_view, name="bar-chart"),
    path("bar-chart-data/", views.bar_chart_view_data, name="bar-chart-data"),
    
    path("pie-chart/", views.pie_chart_view, name="pie-chart"),
    path("pie-chart-data/", views.pie_chart_view_data, name="pie-chart-data"),
    
    path("pie-chart-embedded/", views.pie_chart_view_embedded, name="pie-chart-embedded"),
    
    
    path("line-chart/", views.line_chart_view, name="line-chart"),
    path("line-chart-data/", views.line_chart_view_data, name="line-chart-data"),
]
