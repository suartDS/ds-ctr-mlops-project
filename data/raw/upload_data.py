import os
import boto3
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    
    aws_access_key_id = os.getenv("aws_access_key_id")
    aws_secret_access_key = os.getenv("aws_secret_access_id")
    
    print("aws_access_key_id", aws_access_key_id)
    print("aws_secret_access_key", aws_secret_access_key)
    
    session = boto3.session.Session()
    
    s3_client = session.client(
        service_name = "s3",
        aws_access_key_id = aws_access_key_id,
        aws_secret_access_key = aws_secret_access_key,
        endpoint_url = "http://hb.ru-msk.vkcs.cloud"
    )

    #response = s3_client.list_buckets()

    #for key in response['Buckets']:
    #    print(key['Name'])
    #"../data/raw/sampled_train_50k.csv"
    s3_client.upload_file( 
                    "./data/raw/sampled_train_50k.csv",
                    "ctr_cnt",
                    "sampled_train_50k.csv.csv"
                )
    
