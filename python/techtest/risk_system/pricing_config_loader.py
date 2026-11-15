from __future__ import annotations

class PricingConfigLoader:
    def __init__(self) -> None:
        self.config_file: str | None = None

    def load_config(self) -> object:
        
        engine_config_items = []
        tree = ElementTree.parse(self.config_file)
        root = tree.getroot()

        for engine in root:

            configItem = PricingEngineConfigItem(
                trade_type = engine.attrib["tradeType"],
                module = engine.attrib["module"],
                class_name = engine.attrib["class"]
            )

            engine_config_items.append(configItem)
        return engine_config_items
                
