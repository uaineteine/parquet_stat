import pyarrow.parquet as pq

def parquet_file_info(file_path):
    # Open the Parquet file
    parquet_file = pq.ParquetFile(file_path)

    # Get the metadata
    metadata = parquet_file.metadata

    # Extract the file size and row count
    file_size = metadata.serialized_size
    num_rows = metadata.num_rows

    # Extract the schema
    schema = metadata.schema

    return file_size, num_rows, schema

# Example usage
file_path = 'path/to/your/file.parquet'
size, rows, schema = parquet_file_info(file_path)
print(f"File Size: {size} bytes")
print(f"Number of Rows: {rows}")
print(f"Schema: {schema}")
