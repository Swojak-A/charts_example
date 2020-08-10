from typing import TYPE_CHECKING, Optional

import pandas as pd
import plotly.express as px

from django.db.models import Count, Sum
from django.db.models.functions import TruncYear

from modules.core.charts import Chart
from modules.trunc_year.constants import DonationTypes

if TYPE_CHECKING:
    from django.db.models.query import QuerySet  # NOQA
    from .models import DonationReport  # NOQA


class DonationCountChart(Chart):
    def __init__(self, queryset: Optional["QuerySet"]):
        self.initial_queryset = queryset
        self.queryset = self.prepare_queryset(queryset=queryset)
        self.from_dataframe = True

    def prepare_queryset(self, queryset):
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
    def data(self):
        if not self.queryset:
            return None

        data = pd.DataFrame(list(self.queryset))
        return data

    @property
    def chart(self):
        if self.data.empty:
            return None

        fig = px.bar(
            data_frame=self.data,
            x="year",
            y="count",
            height=400,
            title="Number of Donations",
            labels={"year": "Donation Year", "count": "Total Number of Donations"},
        )
        return fig

    def to_html(self):
        if not self.chart:
            return None

        return self.chart.to_html()

