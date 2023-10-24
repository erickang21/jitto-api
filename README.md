# Jitto API Gateway

A simple serverless API designed to store and retrieve data in a AWS DynamoDB database.

Services Used: 
AWS Lambda, DynamoDB, API Gateway, CloudFormation, CloudWatch

# API Information
DynamoDB is a schemaless structure, so there are no specific fields for data being stored, except for the unique identifier. The key "id" is used to uniquely identify each entry.

# API Documentation
The base URL to make requests are:
`https://kvotk8t3rb.execute-api.us-east-2.amazonaws.com/prod/`

**__Authorization__**
This API requires authorization via an authorized API key. You must include the following headers:
`"x-api-key": "[token]"`
where [token] is replaced with a valid API key.

**__Endpoints__**
**GET** `data`
Retrieves all entries of data.

__Response Body:__
```json
{
   "id":null,
   "data":[]
}
```
where "data" is a list containing all entries in the database.

**GET** `data?id=?`
Retrieves a specific entry of data, with the given ID.

__Query Parameters:__
(Required) id (str): The ID of the entry you want to retrieve

__Response Body:__
```json
{
   "id":null,
   "entry": {}
}
```
where "entry" is a JSON object containing that entry in the database.

**POST** `insert`
Insert an entry of data. Requires unique ID to be given.

__Sample Request Body (Required):__
```json
{
    "id": "1",
    "entry1": "value1",
    "entry2": "value2..."
}
```

__Response Body (Success):__
This is what will be returned if the request body is valid.
```json
{
    "message": "Added successfully.",
    "data": "{\"id\": \"1\", \"entry1\": \"value1\", \"entry2\": \"value2...\"}"
}
```

__Response Body (Errors):__
If you forgot to include a valid ID this will be returned:
```json
{
    "message": "Missing required identifier \"id\""
}
```

If you did not include ID as a string type, this will be returned:
```json
{
    "message": "Required identifier \"id\" is not of type String."
}
```

# Errors
`400`: Bad request
`403`: Missing authentication token. Check Authorization instructions for how to include API key.

# Ratelimits
Tracked per IP address.

- 1000 requests at a time (burst).
- 5000 requests/second
- 1,000,000 requests/month

# Contact Me!
For any additional questions or help, please contact me at eric.kang@uwaterloo.ca