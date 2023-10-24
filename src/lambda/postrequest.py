import json
import boto3

db = boto3.resource("dynamodb")
table = db.Table("jitto-database")

def lambda_handler(event, context):
    params = event.get("multiValueQueryStringParameters")
    request_id = None
    if params:
        request_id = params.get("id")
    if request_id and request_id[0] != None: # Key is provided - return that specific result
        response = table.get_item(Key={
            "id": str(request_id[0])
        })
        data = response
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {},
            "body": json.dumps({
                "id": request_id[0],
                "entry": data["Item"]
            })
        }
    else: # No key provided - return all results
        response = table.scan()
        data = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])
            
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {},
            "body": json.dumps({
                "id": None,
                "data": data
            })
        }