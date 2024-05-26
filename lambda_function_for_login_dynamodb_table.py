import boto3
def lambda_handler(event, context):
    type = event['type'];
    email = event['email'];
    password =event['password'];
    user_name = event['user_name'];
    # this will create dynamodb resource object and
    # here dynamodb is resource name
    client = boto3.resource('dynamodb')
   
    # this will search for dynamoDB table
    table = client.Table("login")
   
   # GET the exisitng login credentials with email and password
    if type=="get":
        db_item=table.get_item(Key={'email': email})
        
        if 'Item' in db_item and db_item['Item']['password'] == password:
            resp = {
             'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'body': {
                    'Item': db_item['Item']
                }
            }
        else:
            resp = {
                'statusCode': 401,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'body': {
                    'message': 'credential not found'
                }
            }
    # CHECK if credential exists with email only
    elif type=="check":
        db_item=table.get_item(Key={'email': email})
        
        if 'Item' in db_item:
            resp = {
             'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'body': {
                    'Item': db_item['Item']
                }
            }
        else:
            resp = {
                'statusCode': 401,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'body': {
                    'message': 'credential not found'
                }
            }
    elif type=="options":
        db_item=table.get_item(Key={'email': email})
        
        if 'Item' in db_item and db_item['Item']['password'] == password:
            resp = {
             'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'body': {
                    'Item': db_item['Item']
                }
            }
        else:
            resp = {
                'statusCode': 401,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'body': {
                    'message': 'credential not found'
                }
            }
    # POST if credential exists with email only
    elif type=="post":
            table.put_item(
                Item={
                    'email': email,
                    'password': password,
                    'user_name': user_name
                }
            )
            
            resp = {
             'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'body': {
                    'message': 'credential added'
                }
            }
            
    return resp
    


