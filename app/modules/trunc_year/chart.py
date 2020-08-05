from typing import TYPE_CHECKING, Optional

import plotly.graph_objects as go

from django.db.models import Count
from django.db.models.functions import TruncYear

from modules.core.charts import Chart

if TYPE_CHECKING:
    from django.db.models.query import QuerySet  # NOQA
    from .models import DonationReport  # NOQA


class DonationCountChart(Chart):
    def __init__(self, queryset: Optional["QuerySet"]):
        self.queryset = queryset

    def prepare_data(self):
        if not self.queryset:
            return None

        queryset = (
            self.queryset.annotate(year=TruncYear("donation_date"))
            .values("year")
            .annotate(count=Count("id"))
            .order_by("year")
        )

        data = {
            "years": [obj["year"].year for obj in queryset],
            "donation_count": [obj["count"] for obj in queryset],
            "hovertext": [
                f"{obj['count']} donations in {obj['year'].year}" for obj in queryset
            ],
        }
        return data

    def prepare_chart(self):
        if not (data := self.prepare_data()):
            return None

        fig = go.Figure(
            go.Bar(
                x=data["years"],
                y=data["donation_count"],
                hovertext=data["hovertext"],
                name="Number of Donations",
                marker_color="#79aec8",
                width=0.3,
            )
        )
        fig.update_layout(title_text="Number of Donations")
        return fig

    def to_html(self):
        if not (fig := self.prepare_chart()):
            return None

        return fig.to_html()
