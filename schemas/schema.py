from pydantic import BaseModel

class AddBill(BaseModel):
    item_names: list[str]
    item_quantities: list[float]
    item_prices: list[float]