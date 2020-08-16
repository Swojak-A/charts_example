from typing import TYPE_CHECKING, Optional, Dict

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from django.db.models import F, Sum, Value as V
from django.db.models.functions import Concat

from modules.core.charts import Chart
from .constants import EmployeeRoles

if TYPE_CHECKING:
    from django.db.models.query import QuerySet  # NOQA
    from pandas import DataFrame  # NOQA
    from plotly.graph_objects import Figure  # NOQA


class EmployerExpensesGoChart(Chart):
    def __init__(self, queryset: Optional["QuerySet"]):
        self.initial_queryset = queryset
        self.queryset = self.prepare_queryset()
        self.from_dataframe = False

    def prepare_queryset(self):
        if not self.initial_queryset:
            return None

        queryset = (
            self.initial_queryset.annotate(role=F("employee__role"))
            .values("year", "role")
            .annotate(value=Sum("value"))
            .order_by("role", "year")
        )
        return queryset

    @property
    def data(self) -> Optional[Dict]:
        if not self.queryset:
            return pd.DataFrame(None)

        data = {
            "board_sum": [
                obj["value"]
                for obj in self.queryset
                if obj["role"] == EmployeeRoles.board.name
            ],
            "guide_sum": [
                obj["value"]
                for obj in self.queryset
                if obj["role"] == EmployeeRoles.guide.name
            ],
            "maintenance_sum": [
                obj["value"]
                for obj in self.queryset
                if obj["role"] == EmployeeRoles.maintenance.name
            ],
            "researcher_sum": [
                obj["value"]
                for obj in self.queryset
                if obj["role"] == EmployeeRoles.researcher.name
            ],
            "year": list(set([obj["year"] for obj in self.queryset])),
        }
        return data

    @property
    def chart(self) -> Optional["Figure"]:
        if not self.data:
            return None

        fig = go.Figure(
            data=[
                go.Bar(
                    name="Researcher",
                    x=self.data["year"],
                    y=self.data["researcher_sum"],
                    marker_color="#6c9cb4",
                ),
                go.Bar(
                    name="Maintenance",
                    x=self.data["year"],
                    y=self.data["maintenance_sum"],
                    marker_color="#b2c6c6",
                ),
                go.Bar(
                    name="Board",
                    x=self.data["year"],
                    y=self.data["board_sum"],
                    marker_color="#79aec8",
                ),
                go.Bar(
                    name="Guide",
                    x=self.data["year"],
                    y=self.data["guide_sum"],
                    marker_color="#91aeae",
                ),
            ]
        )
        fig.update_layout(
            title="Total Employer Expenses (Plotly Graph Object)",
            height=530,
            barmode="stack",
            legend=dict(
                title=dict(text=""), yanchor="top", y=0.95, xanchor="left", x=0.01
            ),
            xaxis = dict(
                title_text="Fiscal Year"
            ),
            yaxis=dict(
                title_text="Expenses"
            )
        )
        return fig

    def to_html(self) -> Optional[str]:
        if not self.chart:
            return None

        return self.chart.to_html()


class EmployerExpensesExpressChart(Chart):
    def __init__(self, queryset: Optional["QuerySet"]):
        self.initial_queryset = queryset
        self.queryset = self.prepare_queryset(queryset=queryset)
        self.from_dataframe = True

    def prepare_queryset(self, queryset) -> Optional["QuerySet"]:
        if not queryset:
            return None

        queryset = queryset.annotate(
            employee_name=Concat(
                "employee__first_name",
                V(" "),
                "employee__last_name",
                V(" ("),
                "employee__position",
                V(")"),
            ),
            role=F("employee__role"),
        ).values("year", "value", "employee_name", "role")
        return queryset

    @property
    def data(self) -> "DataFrame":

        if not self.queryset:
            return pd.DataFrame(None)

        data = pd.DataFrame(list(self.queryset))
        return data

    @property
    def chart(self) -> Optional["Figure"]:
        if self.data.empty:
            return None

        fig = px.bar(
            data_frame=self.data,
            x="year",
            y="value",
            color="role",
            barmode="relative",
            orientation="v",
            height=530,
            title="Total Employer Expenses (Plotly Express)",
            hover_name="employee_name",
            labels={
                "employee_name": "Employer",
                "year": "Fiscal Year",
                "value": "Expenses",
                "role": "Branch",
            },
            color_discrete_map={
                "board": "#79aec8",
                "guide": "#91aeae",
                "maintenance": "#b2c6c6",
                "researcher": "#6c9cb4",
            },
        )
        capitalize = lambda x: x[0].upper() + x[1:]
        for i, data_obj in enumerate(fig.data):
            fig.data[i]["name"] = capitalize(fig.data[i]["name"])
        fig.update_layout(
            legend=dict(
                title=dict(text=""), yanchor="top", y=0.95, xanchor="left", x=0.01
            )
        )
        return fig

    def to_html(self) -> Optional[str]:
        if not self.chart:
            return None

        return self.chart.to_html()
