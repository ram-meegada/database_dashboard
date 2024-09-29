from django.urls import path
from db_dashboard_app.views import *

urlpatterns = [
    path("dashboard/", DashBoardView.as_view(), name="dashboard"),
    path("create-table/", CreateTableView.as_view(), name="create_table"),
]