import boto3
def lambda_handler(event, context):
    type = event['type'];
    email = event['email'];
    title = event['title'];
    artist = event['artist'];
    year = event['year'];

    # this will create dynamodb resource object and
    # here dynamodb is resource name
    client = boto3.resource('dynamodb')
   
    # this will search for dynamoDB table
    table = client.Table("music_subscribe")
   
   # SCAN all music subscribed
    if type=="scan":
        db_items=table.scan(
            ExpressionAttributeValues={
                ':e': email
            },
            ExpressionAttributeNames={
                '#y': 'year'
            },
            FilterExpression='email = :e',
            ProjectionExpression='title, artist, #y'
        )
        
        if len(db_items['Items']) > 0 :
            resp = {
             'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'body': {
                    'Items': db_items['Items']
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
                    'message': 'no music subscribed'
                }
            }
    # DELETE music subscribed
    elif type=="delete":
        resp = table.delete_item(
            Key={
                'email': email,
                'title': title
            }
        )
    # PUT new music subscribed
    elif type=="put":
        resp = table.put_item(
            Item={
                'email': email,
                'title': title,
                'artist': artist,
                'year': int(year)
            }
        )
        
    return resp
    


