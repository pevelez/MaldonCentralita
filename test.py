import json

def lambda_handler(event, context):
    print("Maldon was called")
    print(event)
    if event['httpMethod'] != 'POST':
        return {
            "statusCode": 400,
            'body': json.dumps('Invalid REST format')
        }
    if 'body' not in event:
        return {
            "statusCode": 400,
            "body": json.dumps('Body not found')
        }
    mensaje = "Esta es una prueba para Manel. Este es otro enunciado. Este tercer enunciado tiene acentos y comas, camión, butano, prueba."
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            "phoneActionType": "EXTERNAL_REQUEST",
            "phoneActionId": "1",
            "variables": {
                "tts_play": mensaje,
                "tts_voice": "Lucia::neural"
            }
        })
    }
