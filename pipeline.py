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
from data_loaders import load_data
from data_processor import process_data, create_cleaning_report

logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO, format="%(asctime)s %(levelname)-8s %(name)s — %(message)s", datefmt="%H:%M:%S")



def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description= "data pipeline")
    parser.add_argument("--input", "-i", type=Path, required=True, help="Path to input file")
    parser.add_argument("--config","-c",type=Path, required=True, help="Path to YAML Config file")
    parser.add_argument("--output", "-o", type=Path, required=True, help="Path to output file")
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
    logger.debug(f"Arguments parsed: input={args.input}, output={args.output}, config={args.config}")
    if validate_input(args.input) == False:
        sys.exit(1)
    if validate_input(args.config) == False:
            sys.exit(1)
    try:
        data = load_data(args.input)
        config = load_data(args.config)
    except ValueError:
        sys.exit(1)
    original_df = data.copy()
    try:
        cleaned_df = process_data(data, config)
    except ValueError:
        sys.exit(1)
    report = create_cleaning_report(original_df,cleaned_df)
    print(report)
    logger.info(f"Processing complete: {report['rows_before']} → {report['rows_after']} rows")
    cleaned_df.to_csv(args.output, index= False)
    logger.info(f"Saved cleaned data to {args.output}")



if __name__ == "__main__":
    main()