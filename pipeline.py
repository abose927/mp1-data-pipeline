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
from src import (
create_cleaning_report,
load_data,
process_data,
save_data,
setup_logging,
validate_dataframe,
validate_input,
)

logger = logging.getLogger(__name__)





def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description= "data pipeline")
    parser.add_argument("--input", "-i", type=Path, required=True, help="Path to input file")
    parser.add_argument("--config","-c",type=Path, required=True, help="Path to YAML Config file")
    parser.add_argument("--output", "-o", type=Path, required=True, help="Path to output file")
    parser.add_argument("--verbose", "-v", action="store_true", required=False, help="Enable verbose logging")
    return parser.parse_args()







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
    required_columns = config["validation"]["required_columns"]
    numeric_columns = config["validation"]["numeric_columns"]
    try:
        validated_df = validate_dataframe(data, required_columns, numeric_columns)
    except ValueError:
        sys.exit(1)
    original_df = validated_df.copy()
    logger.info(f"Validation successful: {len(data)} -> {len(validated_df)} rows")
    try:
        cleaned_df = process_data(validated_df, config)
    except ValueError:
        sys.exit(1)
    report = create_cleaning_report(original_df,cleaned_df)
    logger.info(f"Processing complete: {report['rows_before']} → {report['rows_after']} rows")
    save_data(cleaned_df, args.output)
    logger.info(f"Saved cleaned data to {args.output}")
    print(report)



if __name__ == "__main__":
    main()