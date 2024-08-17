import numpy as np
import pandera as pa
from pandera import DataFrameModel
from pandera.typing import Series


class SalesDataSchema(DataFrameModel):
    datetime: Series[np.datetime64]
    user_id: Series[int]
    item_id: Series[int]
    quantity: Series[int] = pa.Field(ge=0)


class DatamartSchema(DataFrameModel):
    datetime: Series[np.datetime64]
    user_id: Series[int]
    sex: Series[str]
    age: Series[int] = pa.Field(ge=0)
    sales_price: Series[float]
