# %%
from dataclasses import dataclass, field
from pathlib import Path

from data_processor.loader import load_sales_data
from util.consts import REPO_ROOT


# %%
@dataclass
class Config:
    data_dir: Path = REPO_ROOT / "data"
    output_dir: Path = REPO_ROOT / "outputs"
    group: list[str] = field(default_factory=lambda: ["user_id"])


config = Config()

# %%
df = load_sales_data(config.data_dir / "processed" / "sales_data.csv")
df_result = df.groupby(config.group)["quantity"].mean().reset_index()
df_result.to_csv(config.output_dir / "output.csv", index=False)

# %%
