from typing import TYPE_CHECKING, Optional

import plotly.graph_objects as go

from django.db.models import Count, Sum
from django.db.models.functions import TruncYear

from modules.core.charts import Chart
from modules.trunc_year.constants import DonationTypes

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
            "count": [obj["count"] for obj in queryset],
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
                y=data["count"],
                hovertext=data["hovertext"],
                name="Number of Donations",
                marker_color="#79aec8",
                width=0.3,
                showlegend=True,
            )
        )
        fig.update_layout(
            title_text="Number of Donations",
            legend=dict(yanchor="top", y=0.95, xanchor="left", x=0.01),
        )
        return fig

    def to_html(self):
        if not (fig := self.prepare_chart()):
            return None

        return fig.to_html()


class DonationTypeComparisonChart(Chart):
    def __init__(self, queryset: Optional["QuerySet"]):
        self.queryset = queryset

    def prepare_data(self):
        if not self.queryset:
            return None

        queryset = (
            self.queryset.annotate(year=TruncYear("donation_date"))
            .values("year", "type")
            .annotate(value=Sum("value"))
            .order_by("type", "year")
        )

        data = {
            "donation_years": [
                obj["year"].year
                for obj in queryset
                if obj["type"] == DonationTypes.donation.name
            ],
            "donation_value": [
                obj["value"]
                for obj in queryset
                if obj["type"] == DonationTypes.donation.name
            ],
            "donation_hovertext": [
                f"{obj['value']} donations in {obj['year'].year}"
                for obj in queryset
                if obj["type"] == DonationTypes.donation.name
            ],
            "grant_years": [
                obj["year"].year
                for obj in queryset
                if obj["type"] == DonationTypes.grant.name
            ],
            "grant_value": [
                obj["value"]
                for obj in queryset
                if obj["type"] == DonationTypes.grant.name
            ],
            "grant_hovertext": [
                f"{obj['value']} grants in {obj['year'].year}"
                for obj in queryset
                if obj["type"] == DonationTypes.grant.name
            ],
        }
        return data

    def prepare_chart(self):
        if not (data := self.prepare_data()):
            return None

        fig = go.Figure(
            data=[
                go.Bar(
                    x=data["donation_years"],
                    y=data["donation_value"],
                    hovertext=data["donation_hovertext"],
                    name="Combined Value of Donations",
                    marker_color="#79aec8",
                    width=0.3,
                ),
                go.Bar(
                    x=data["grant_years"],
                    y=data["grant_value"],
                    hovertext=data["grant_hovertext"],
                    name="Combined Value of Grants",
                    marker_color="#91aeae",
                    width=0.3,
                ),
            ]
        )
        fig.update_layout(
            title_text="Number of Donations in relation to numer of Grants",
            legend=dict(yanchor="top", y=0.95, xanchor="left", x=0.01),
        )
        return fig

    def to_html(self):
        if not (fig := self.prepare_chart()):
            return None

        return fig.to_html()
