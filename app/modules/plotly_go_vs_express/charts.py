from typing import TYPE_CHECKING, Optional

import pandas as pd
import plotly.express as px

from django.db.models import F, Value as V
from django.db.models.functions import Concat

from modules.core.charts import Chart

if TYPE_CHECKING:
    from django.db.models.query import QuerySet  # NOQA
    from pandas import DataFrame  # NOQA
    from plotly.graph_objects import Figure  # NOQA


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
