import pandas as pd
import io
import boto3

def clean_dataset_from_s3(s3_client, bucket_name, file_name, columns_to_drop):
    # Download dataset from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    body = response['Body'].read().decode('utf-8')
    data = pd.read_csv(io.StringIO(body))

    # Drop columns
    data = data.drop(columns=columns_to_drop)

    # Remove duplicates
    data = data.drop_duplicates()

    # Remove rows with missing data
    data = data.dropna()

    # Reset index
    data = data.reset_index(drop=True)

    return data
