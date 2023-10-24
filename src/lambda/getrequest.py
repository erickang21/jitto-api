import json
import boto3

db = boto3.resource("dynamodb")
table = db.Table("jitto-database")

def lambda_handler(event, context):
    from_query = event["queryStringParameters"]
    from_body = event["body"]
    if from_body:
        try:
            from_body = json.loads(event["body"])
        except:
            return {
                "isBase64Encoded": False,
                "statusCode": 400,
                "headers": {},
                "body": json.dumps({
                    "message": "Invalid body"
                })
            }
    data = from_query if from_query else from_body
    if not data.get("id"):
        return {
            "isBase64Encoded": False,
            "statusCode": 400,
            "headers": {},
            "body": json.dumps({
                "message": "Missing required identifier \"id\""
            })
        }
    elif not isinstance(data.get("id"), str):
        return {
            "isBase64Encoded": False,
            "statusCode": 400,
            "headers": {},
            "body": json.dumps({
                "message": "Required identifier \"id\" is not of type String."
            })
        }
    table.put_item(Item=data);
    return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {},
            "body": json.dumps({
                "message": "Added successfully.",
                "data": json.dumps(data)
            })
        }
