import boto3
import csv

def read_csv_from_s3(bucket_id: str, object_key: str) -> list:
    """
    Reads a CSV file from an S3 bucket and returns the data as a list of lists.
    """
    s3 = boto3.client("s3")
    response = s3.get_object(Bucket=bucket_id, Key=object_key)
    file_content = response["Body"].read().decode("utf-8").splitlines()
    reader = csv.reader(file_content)
    return [line for line in reader]

def filter_and_format_rows(records: list) -> list:
    """
    Filters out rows with missing data and applies formatting to each cell.
    """
    updated_rows = []
    for entry in records:
        if all(cell.strip() for cell in entry):  # Valid row: no blank fields
            cleaned = [field.strip().capitalize() for field in entry]
            updated_rows.append(cleaned)
    return updated_rows

def write_csv_to_s3(records: list, destination_bucket: str, filename: str):
    """
    Converts a list of records into a CSV-formatted string and writes to S3.
    """
    s3 = boto3.client("s3")
    content = "\n".join([",".join(row) for row in records])
    s3.put_object(Bucket=destination_bucket, Key=filename, Body=content.encode("utf-8"))

def lambda_handler(event, context):
    """
    AWS Lambda entry point. Processes a CSV uploaded to S3 by cleaning it
    and saving the result in another bucket.
    """
    # Extracting S3 object details from the event payload
    source_bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    uploaded_filename = event["Records"][0]["s3"]["object"]["key"]

    # Define where the cleaned file will be stored
    processed_bucket_name = "yourname-processed-data"  # Change as needed
    cleaned_filename = f"cleaned_{uploaded_filename}"

    # Complete processing pipeline
    raw_csv_data = read_csv_from_s3(source_bucket_name, uploaded_filename)
    refined_data = filter_and_format_rows(raw_csv_data)
    write_csv_to_s3(refined_data, processed_bucket_name, cleaned_filename)

    # Return HTTP-style response
    return {
        "statusCode": 200,
        "body": f"CSV has been cleaned and saved as: {cleaned_filename}"
    }
