def lambda_handler(event, context):
    print("Message received")
    print(event)
    return {
        "statusCode": 200
    }
