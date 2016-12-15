# Weather Bot

A LINE chat bot for querying current weather.

## Requirements

* Python 3
    * Django (`Django`)
    * gunicorn (`gunicorn`)
    * SDK for LINE Messaging API (`line-bot-api`)

## How to build this bot

1. Setup secret information

    There are two ways to reach it.

    * Using environment variables
    ```shell
    export SECRET_KEY='SECRET_KEY'
    export CWB_AUTHED_KEY='CWB_AUTHED_KEY'
    export LINE_CHANNEL_SECRET='LINE_CHANNEL_SECRET'
    export LINE_CHANNEL_ACCESS_TOKEN='LINE_CHANNEL_ACCESS_TOKEN'
    ```

    * Write secret to `weather_bot/secret.py`
    ```python
    SECRET_KEY = 'SECRET_KEY'
    CWB_AUTHED_KEY = 'CWB_AUTHED_KEY'
    LINE_CHANNEL_SECRET = 'LINE_CHANNEL_SECRET'
    LINE_CHANNEL_ACCESS_TOKEN = 'LINE_CHANNEL_ACCESS_TOKEN'
    ```

2. Modify `ALLOWED_HOSTS` in `weather_bot/settings.py`
    ```python
    ALLOWED_HOSTS = [
        'YOUR_HOST'
    ]
    ```

3. Deploy this web application in HTTPS server

    You may use [Heroku](https://www.heroku.com/) to help you get HTTPS URL.

4. Go to LINE Bot setting page

    Fill callback url for bot in `Webhook URL` field.

    (e.g. `https://YOUR_HOST/service/callback/`)

## Reference

* [HaoTse's Blog](http://haotse-blog.logdown.com/)
