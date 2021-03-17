from scrapper import WebScrapper
import json

def lambda_handler(event, context):
    # driver = WebScrapper()
    # driver.scrap()
    # ### pass stuff here

    return {
        'statusCode': 200,
        'body': json.dumps({
            'data': 'DONE'
        }),
    }