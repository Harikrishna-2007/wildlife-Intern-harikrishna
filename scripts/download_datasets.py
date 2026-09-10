"""Dataset manifest and download entry point.

Large datasets require their provider credentials and license acceptance. This script
keeps downloads explicit and resumable instead of silently pulling multi-gigabyte data.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Dataset:
    name: str
    source: str
    purpose: str


DATASETS = (
    Dataset("Snapshot Serengeti", "https://lila.science/datasets/snapshot-serengeti", "camera-trap detection"),
    Dataset("iNaturalist", "https://github.com/visipedia/inat_comp", "species classification"),
    Dataset("BirdCLEF", "https://www.kaggle.com/competitions/birdclef", "bioacoustic recognition"),
    Dataset("Animal Kingdom", "https://github.com/siyuan-sun/Animal-Kingdom", "wildlife action recognition"),
    Dataset("GBIF", "https://www.gbif.org/occurrence/search", "taxonomy and occurrence enrichment"),
)


def write_manifest(output_dir: str = "data/manifests") -> None:
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    manifest = destination / "datasets.tsv"
    manifest.write_text(
        "name\tsource\tpurpose\n"
        + "\n".join(f"{item.name}\t{item.source}\t{item.purpose}" for item in DATASETS)
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    write_manifest()