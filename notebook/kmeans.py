from dataclasses import dataclass

import hydra
from hydra.core.config_store import ConfigStore
from sklearn.cluster import KMeans


@dataclass
class Config:
    n_clusters: int = 5
    algorithm: str = "lloyd"


cs = ConfigStore.instance()
cs.store(name="config", node=Config)


@hydra.main(version_base="1.1", config_name="config")
def main(config: Config):
    kmeans = KMeans(**config)
    print(kmeans)


if __name__ == "__main__":
    main()
