import pandas as pd
import boto3

def clean_dataset_from_s3(bucket_name, file_name, columns_to_drop):
    # Download dataset from S3
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, file_name)
    body = obj.get()['Body'].read().decode('utf-8')
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
