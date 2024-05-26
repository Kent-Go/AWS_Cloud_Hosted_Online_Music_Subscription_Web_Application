import boto3
def lambda_handler(event, context):
    type = event['type'];
    title = event['title'];
    year = event['year'];
    artist = event['artist'];

    # this will create dynamodb resource object and
    # here dynamodb is resource name
    client = boto3.resource('dynamodb')
   
    # this will search for dynamoDB table
    table = client.Table("music")
   
    # SCAN music
    if type=="scan":
        filter_expression_string = ''
        expression_attribute_values_dict = {}
        
        conditions_dict = {
            'title': title,
            'artist': artist,
            'y': year
        }
        
        filtered_conditions_dict = {attribute:value for (attribute, value) in conditions_dict.items() if value is not None}

        for index, (attribute, value) in enumerate(filtered_conditions_dict.items()):
            if index > 0:
                filter_expression_string += ' AND '
            expression_attribute_values_dict[f':{attribute}'] = value
            if attribute == 'y':
                filter_expression_string += f'#y = :{attribute}'
            else:
                filter_expression_string += f'{attribute} = :{attribute}'
        
        db_items=table.scan(
            Select = 'SPECIFIC_ATTRIBUTES',
            ExpressionAttributeNames={
                '#y': 'year'
            },
            ExpressionAttributeValues=expression_attribute_values_dict,
            FilterExpression=filter_expression_string,

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
                    'message': 'no matched music found'
                }
            }
        
    return resp
    


