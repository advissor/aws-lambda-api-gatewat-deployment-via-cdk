def lambda_handler(event, context):
    message = 'Transaction: {}'.format("id-12314124124124")  
    return { 
        "isBase64Encoded": "false",
        "statusCode": 200,
        'body' : message
    }