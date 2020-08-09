from typing import TYPE_CHECKING, Optional, Dict
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from plotly.graph_objects import Figure  # NOQA


class Chart(ABC):
    @abstractmethod
    def prepare_data(self) -> Optional[Dict]:
        ...

    @abstractmethod
    def prepare_chart(self) -> Optional["Figure"]:
        ...

    @abstractmethod
    def to_html(self) -> Optional[str]:
        ...
