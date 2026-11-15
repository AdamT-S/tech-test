from __future__ import annotations

from datetime import datetime

from techtest.models.base_trade import BaseTrade


class FxTrade(BaseTrade):
    FX_SPOT_TRADE_TYPE = "FxSpot"
    FX_FORWARD_TRADE_TYPE = "FxFwd"

    def __init__(self) -> None:
        super().__init__()
        self.value_date: datetime = datetime.min
        self._trade_id = trade_id

    @property
    def trade_type(self) -> str:
        if self.type_of_trade == 'FxSpot':
            return FxTrade.FX_SPOT_TRADE_TYPE
        if self.type_of_trade == 'FxFwd':
            return FxTrade.FX_FORWARD_TRADE_TYPE
        else:
            return None
