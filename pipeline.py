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


logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%H:%M:%S")



def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description= "data pipeline")
    parser.add_argument("--input", "-i", type=Path, required=True, help="Path to input file")
    parser.add_argument("--output", "-o", type=Path, required=True, help="Path to output file")
    parser.add_argument("--format", choices=["csv","json"], default="csv", required=False, help="States what format (csv or JSON) the output is")
    parser.add_argument("--verbose", "-v", action="store_true", required=False, help="Enable verbose logging")
    return parser.parse_args()





def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    file_path = Path(filepath)
    if file_path.is_file():
        logger.info(f"Input file validated: {file_path}")
        return True
    else:
        logger.error(f"Input file not found: {file_path}")
        return False

def main():
    """Main pipeline function."""
    args = parse_arguments()
    setup_logging(args.verbose)
    logger.debug(f"Arguments parsed: input={args.input}, output={args.output}, format={args.format}")
    if validate_input(args.input) == False:
        sys.exit(1)


if __name__ == "__main__":
    main()