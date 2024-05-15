import base64
import json
import pandas as pd

def lambda_handler(event, context):
    print("Event is", event)

    output_records = []

    for record in event['records']:
        # Try to decode and transform the record
        try:
            # Decode the input data from base64
            payload = base64.b64decode(record['data'])
            payload_json = json.loads(payload)

            print("Payload_Json or Deserialised data is", payload_json)

            # Access the 'eventName' and 'ApproximateCreationDateTime' from the payload
            event_name = payload_json['eventName']
            approx_creation_datetime = payload_json['dynamodb']['ApproximateCreationDateTime']
            
            # Convert the Unix timestamp to a human-readable date format
            # creation_datetime = datetime.utcfromtimestamp(approx_creation_datetime).isoformat() + 'Z'
    
            # Convert the Unix timestamp to a pandas datetime object
            creation_datetime = pd.to_datetime(approx_creation_datetime, unit='s', utc=True)
            
            # # Convert the pandas datetime to a formatted string
            creation_datetime_str = creation_datetime.isoformat() + 'Z'

            # Access the data in the 'dynamodb' key
            dynamodb_data = payload_json['dynamodb']
            new_image = dynamodb_data['NewImage']
            print(new_image)

            # Extract required fields from NewImage
            transformed_data = {
                'order_id': new_image['order_id']['S'],
                'product_name': new_image['product_name']['S'],
                'quantity': int(new_image['quantity']['N']),
                'price': float(new_image['price']['N']),
                'cdc_event_type': event_name,  # Include the event name
                'creation_datetime': creation_datetime_str  # Include the creation datetime
            }
            
            # Convert the transformed data to a JSON string and then encode it as base64
            transformed_data_str = json.dumps(transformed_data) + '\n'
            transformed_data_encoded = base64.b64encode(transformed_data_str.encode('utf-8')).decode('utf-8')

            # Append the transformed record to the output using 'eventID' as 'recordId'
            output_records.append({
                'recordId': record['recordId'],
                'result': 'Ok',
                'data': transformed_data_encoded
            })

        except Exception as e:
            # If there's any error with processing the record, mark it as ProcessingFailed but still return the recordId
            output_records.append({
                'recordId': record['recordId'],
                'result': 'ProcessingFailed',
                'data': record['data']  # simply pass the original data back
            })

    return {
        'records': output_records
    }
