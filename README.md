The pipeline's goal is to take a csv of data, validate it, clean it, and then return another csv file with cleaned data and a report of what contents were removed. The program starts by converting the provided csv file into a dataframe. To validate the data, the pipeline begins by comparing the columns present in the provided csv file to the columns stated to be required in the configuration. Afterwards, it makes sure that all the contents of the columns stated to be numeric in the config file are actually numeric. Once validation is complete, the data begins processing by removing all duplicate values. Next, it drops all missing values from the dataframe, and removes any outliers using either the IQR method or Z-scores, depending on what is specified in the config. After processing, the pipeline generates a report detailing how many rows were removed from the dataframe. The validated and cleaned data is then saved to a new csv file.
Given the input --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
The output should be as follows 
17:48:09 DEBUG    __main__ — Arguments parsed: input=fixtures/sample_data.csv, output=output/clean.csv, config=config/config.yaml
17:48:09 INFO     src.utils — Input file validated: fixtures/sample_data.csv
17:48:09 INFO     src.utils — Input file validated: config/config.yaml
17:48:09 INFO     src.data_loaders — Loaded CSV File: fixtures/sample_data.csv, (100 rows)
17:48:09 INFO     src.data_loaders — Loaded YAML file: config/config.yaml
17:48:09 WARNING  src.data_validator — Invalid row: 94
17:48:09 WARNING  src.data_validator — Invalid row: 95
17:48:09 DEBUG    src.data_validator — Dropped 2 rows
17:48:09 INFO     __main__ — Validation successful: 100 -> 98 rows
17:48:09 DEBUG    src.data_processor — Dropped 2 rows
17:48:09 DEBUG    src.data_processor — Dropped 2 rows
17:48:09 DEBUG    src.data_processor — 2 rows dropped at a threshold of 1.5 using the iqr method
17:48:09 INFO     __main__ — Processing complete: 98 → 92 rows
17:48:09 DEBUG    src.data_output — Saved 92 rows to output/clean.csv
17:48:09 INFO     __main__ — Saved cleaned data to output/clean.csv
{'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
