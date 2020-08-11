from typing import TYPE_CHECKING, Optional

import pandas as pd
import plotly.express as px

from django.db.models import Count, Sum
from django.db.models.functions import TruncYear

from modules.core.charts import Chart

if TYPE_CHECKING:
    from django.db.models.query import QuerySet  # NOQA
    from .models import DonationReport  # NOQA
    from pandas import DataFrame  # NOQA
    from plotly.graph_objects import Figure  # NOQA


class DonationCountChart(Chart):
    def __init__(self, queryset: Optional["QuerySet"]):
        self.initial_queryset = queryset
        self.queryset = self.prepare_queryset(queryset=queryset)
        self.from_dataframe = True

    def prepare_queryset(self, queryset) -> Optional["QuerySet"]:
        if not queryset:
            return None

        queryset = (
            queryset.annotate(year=TruncYear("donation_date"))
                .values("year")
                .annotate(count=Count("id"))
                .order_by("year")
        )
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
            y="count",
            height=400,
            title="Number of Donations and Grants",
            labels={"year": "Fiscal Year", "count": "Total Number of Donations and Grants"},
        )
        fig.update_traces(
            marker_color="#79aec8",
            showlegend=True
        )
        fig.data[0]["name"] = "Count"
        fig.update_layout(legend=dict(
            title=dict(
                text=""
            ),
            yanchor="top",
            y=0.95,
            xanchor="left",
            x=0.01
        ))
        return fig

    def to_html(self) -> Optional[str]:
        if not self.chart:
            return None

        return self.chart.to_html()

