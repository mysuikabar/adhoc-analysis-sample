import pandas as pd
import pandera as pa
from pandera.typing import DataFrame
from util.consts import REPO_ROOT

from data_processor.schema import SalesDataSchema


@pa.check_types
def process_sales_data(df_raw: pd.DataFrame) -> DataFrame[SalesDataSchema]:
    df_processed = df_raw.copy()
    df_processed["datetime"] = pd.to_datetime(df_processed["datetime"])
    return df_processed


def main():
    df_raw = pd.read_csv(REPO_ROOT / "data" / "raw" / "sales_data.csv")
    df_processed = process_sales_data(df_raw)
    df_processed.to_csv(
        REPO_ROOT / "data" / "processed" / "sales_data.csv", index=False
    )


if __name__ == "__main__":
    main()
