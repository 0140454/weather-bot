from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from .weather import get_current_weather
from .api_ai import intent_parser

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    DEFAULT_LOCATION = '臺南市'

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    if '天氣' in event.message.text:
                        intent = intent_parser(event.message.text)
                        if intent['result']['action'] == 'input.unknown':
                            response = '目前無法理解您要查詢哪一個城市。\n' \
                                       '以下將替您查詢%s的天氣。\n\n' \
                                       '%s' % (DEFAULT_LOCATION, get_current_weather(DEFAULT_LOCATION))
                        else:
                            place = intent['result']['parameters']['taiwan-city']
                            if len(place) == 0:
                                place = DEFAULT_LOCATION
                            response = get_current_weather(place)
                    else:
                        response = event.message.text

                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text = response)
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
