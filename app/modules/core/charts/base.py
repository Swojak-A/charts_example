from typing import TYPE_CHECKING, Optional, Union, Dict
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from pandas import DataFrame  # NOQA
    from plotly.graph_objects import Figure  # NOQA


class Chart(ABC):
    ...

    @property
    @abstractmethod
    def data(self) -> Optional[Union[Dict, "DataFrame"]]:
        ...

    @property
    @abstractmethod
    def chart(self) -> Optional["Figure"]:
        ...

    @abstractmethod
    def to_html(self) -> Optional[str]:
        ...
