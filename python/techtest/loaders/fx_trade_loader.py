from __future__ import annotations

from datetime import datetime
from typing import Iterable

from techtest.models import Trade, FxTrade, TradeList


class FxTradeLoader:
    _SEPERATOR = "¬"

    
    def __init__(self, data_file: str) -> None:
        self.data_file = data_file

    # NOTE: This method is only here to allow the solution to run prior to the test being completed.
    def load_trades(self) -> Iterable[Trade]:
        yield from self._load_trades_from_file(self.data_file, trade_list)

    def _create_fxtrade_from_line(self, line: str) -> FxTrade:
        items = line.split(self._SEPERATOR)
        fxtrade = FxTrade(items[8])
        fxtrade.type_of_trade = items[0]
        fxtrade.trade_date = datetime.fromisoformat(items[1])

        #Instruments is the type of asset being treated for example here
        #USD->GBP I will therefore store this under instrument
        ccy1 = items[2]
        ccy2 = items[3]
        fxtrade.instrument = ccy1 + ccy2

        fxtrade.notional = float(items[4])
        fxtrade.rate = float(items[5])

        fxtrade.value_date = datetime.strptime(items[6], '%Y-%m-%d')
        fxtrade.counterparty = items[7]

        return fxtrade

    def _load_trades_from_file(self, filename: str, trade_list: TradeList) -> Generator[FxTrade, Any, None]:
        # utf-8-sig skips the byte order mark at the start of the file
        with open(filename, encoding="utf-8-sig") as stream:
            next(stream, None) # Skip the metadata line
            next(stream, None) # Skip the header line
            for line in stream:
                if not line.startswith(("FxSpot", "FxFwd")):
                    continue
                yield self._create_fxtrade_from_line(line.rstrip("\r\n")
    
