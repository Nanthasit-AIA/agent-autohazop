from __future__ import annotations

import argparse
from pathlib import Path

from ag_template_modulee import create_hazop_vector_store_from_folder


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-folder", required=True, help="Folder containing HAZOP PDF/JSON/XLSX guide files")
    parser.add_argument("--name", default="HAZOP_LOPA_KNOWLEDGE_BASE", help="Vector store name")
    parser.add_argument("--config", default="hazop_vector_store_config.json", help="Output config JSON path")
    args = parser.parse_args()

    vector_store_id = create_hazop_vector_store_from_folder(
        Path(args.source_folder),
        vector_store_name=args.name,
        config_path=args.config,
    )
    print(f"Vector store created: {vector_store_id}")
    print(f"Config saved to: {args.config}")


if __name__ == "__main__":
    main()
