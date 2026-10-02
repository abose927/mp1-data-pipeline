"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1
Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys
from pathlib import Path


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%H:%M:%S")

logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description= "data pipeline")
    parser.add_argument("--input", "-i", type=Path, required=True, help="Path to input file")
    parser.add_argument("--output", "-o", type=Path, required=True, help="Path to output file")
    



def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    file_path = Path(filepath)
    if not file_path.exists():
        logger.error(f"File does not exist: {file_path}")
        return False
    else:
        logger.info(f"File found: {file_path.name}")
        if file_path.is_file():
            logger.info(f"Input file validated: {file_path.name} ")
            return True
        else:
            logger.error(f"Input file not found {file_path.name}")
            return False


def main():
    """Main pipeline function."""
    pass  # TODO: implement


if __name__ == "__main__":
    main()