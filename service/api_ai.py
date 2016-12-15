from django.conf import settings
import apiai
import json

def intent_parser(input):
    client = apiai.ApiAI(settings.API_AI_CLIENT_ACCESS_TOKEN)

    request = client.text_request()
    request.query = input

    response = request.getresponse()
    return json.loads(response.read().decode())

if __name__ == '__main__':
    print(intent_parser('今天屏東天氣怎樣'))
    print(intent_parser('高雄天氣好嗎'))
    print(intent_parser('快告訴我台南的天氣'))
    print(intent_parser('跟我說說臺北的天氣'))
