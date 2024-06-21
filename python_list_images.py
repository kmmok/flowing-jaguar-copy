import boto3

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

# Replace 'your-bucket-name' with your bucket name
bucket_name = 'movetrkr-item-pix'
prefix = ''  # If you have a specific prefix, add it here

# Function to list objects in batches
def list_objects_v2(bucket_name, prefix):
    paginator = s3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
    
    with open('data/dam_images.yml', 'w') as file:
        for page in page_iterator:
            for obj in page.get('Contents', []):
                if obj['Key'].lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    file.write(f"- path: \"{obj['Key']}\"\n")

# List objects and generate the YAML file
list_objects_v2(bucket_name, prefix)
