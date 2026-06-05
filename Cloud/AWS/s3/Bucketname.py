import boto3

# 1. Initialize the S3 client
s3_client = boto3.client('s3')

# 2. Fetch the data from AWS
response = s3_client.list_buckets()

# 3. The output
print("Target Acquired. Initiating Bucket Scan...\n")

# The 'response' variable holds a dictionary containing all our buckets.
# Write a 'for' loop that iterates through response['Buckets'] 
# and prints out the Name and CreationDate of every bucket.
for Entries in response["Buckets"]:
    print(Entries["Name"], Entries["CreationDate"])
