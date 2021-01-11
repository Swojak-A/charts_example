from typing import TYPE_CHECKING, Optional, Dict
from datetime import timedelta
import json

from django.utils import timezone

import plotly.express as px
import pandas as pd

from modules.core.charts import Chart

if TYPE_CHECKING:
    from django.db.models.query import QuerySet  # NOQA
    from modules.trunc_day.models import PokeInstituteVisitsReport  # NOQA


class PokeVisitsPerDayChart(Chart):
    def __init__(self, queryset: Optional["QuerySet[PokeInstituteVisitsReport]"] = None):
        self.queryset = queryset

    def prepare_chart(self) -> Optional[Dict]:
        if not self.queryset:
            return None

        # adjust queryset
        qs = self.queryset.all()

        # prepare data


        # chart dict
        # temperature_chart_data = {
        #     "date": temperature_chart_date,
        #     "temp_chart_cooler": json.dumps(temperature_chart_cooler)
        # }
        return 