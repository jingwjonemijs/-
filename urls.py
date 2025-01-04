from django.urls import path
from apps.period import views

urlpatterns = [
    # ... 其他URL配置 ...
    path('period/', views.PeriodListView.as_view(), name='period_list'),
    path('period/add/', views.PeriodCreateView.as_view(), name='period_add'),
    path('period/next/', views.get_next_period, name='period_next'),
] 