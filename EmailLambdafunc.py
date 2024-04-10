import json
import boto3
import csv
import uuid  # Import the uuid module to generate unique IDs

# Initialize AWS SDK clients
s3_client = boto3.client('s3')
dynamodb_client = boto3.client('dynamodb')
ses_client = boto3.client('ses')

# DynamoDB table name
dynamodb_table_name = 'your dynamodb table name'

def lambda_handler(event, context):
    # Get the S3 bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Retrieve CSV content from S3 object
    csv_file = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    
    # Parse the CSV content, handling BOM character if present
    csv_content = csv_file['Body'].read().decode('utf-8-sig')  # Use 'utf-8-sig' to handle BOM
    reader = csv.DictReader(csv_content.splitlines())
    
    # Parse the CSV content
    recipient_data = []
    for row in reader:
        # Check if 'email' and 'message' keys exist in the row
        if 'email' in row and 'message' in row:
            recipient_data.append({
                'email': row['email'],
                'message': row['message']
            })
        else:
            # Handle missing keys or unexpected CSV format
            print("Warning: Missing 'email' or 'message' key in row:", row)



    # Import recipient data into DynamoDB
    for item in recipient_data:
        partition_key_value = str(uuid.uuid4())  # Generate a unique value for the partition key
        dynamodb_client.put_item(
            TableName=dynamodb_table_name,
            Item={
                'your partition key name': {'S': item['your partition ket value']},
                'email': {'S': item['email']},
                'message': {'S': item['message']}
            }
        )

    # Retrieve recipient data from DynamoDB
    # You can perform further processing or send emails directly here
    for item in recipient_data:
        email = item['email']
        message = item['message']
        send_email(email, message)

def send_email(email, message):
    # Send personalized email using AWS SES
    response = ses_client.send_email(
        Source='email source(your email)',
        Destination={'ToAddresses': [email]},
        Message={
            'Subject': {'Data': 'Your Subject'},
            'Body': {'Text': {'Data': message}}
        }
    )
    print(f"Email sent to {email}. Message ID: {response['MessageId']}")
