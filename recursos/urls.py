from django.urls import path
from .views import v_orden_fn_asc

urlpatterns = [
    path('ordenados', v_orden_fn_asc)
]