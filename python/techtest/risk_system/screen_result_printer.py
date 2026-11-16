from __future__ import annotations

from techtest.models import ScalarResults


class ScreenResultPrinter:
    def print_results(self, results: ScalarResults) -> None:
        for result in results:
            if result.result != None and result.error != None:
                 print(f"{result.trade_id} : {result.result} : {result.error}")

            elif result.result != None:
                print(f"{result.trade_id} : {result.result}")

            else:
                print(f"{result.trade_id} : {result.error}")

