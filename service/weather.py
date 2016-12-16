from django.conf import settings
import xml.etree.ElementTree as ET
import urllib.request

def get_current_weather(city):
    """
    Get current weather in specific city.

    Args:
        city: City Name

    Returns:
        Current weather string
    """
    response = urllib.request.urlopen('http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey=%s' % settings.CWB_AUTHED_KEY)
    tree = ET.parse(response).getroot()

    for location in tree.findall('.//{urn:cwb:gov:tw:cwbcommon:0.1}location'):
        if city in location[0].text:
            # If the city is found, access its child direct.
            return '%s目前的天氣為%s。\n' \
                   '溫度為 %s 至 %s ℃，降雨機率為 %s %%。' \
                   % (location[0].text, location[1][1][2][0].text,
                      location[3][1][2][0].text, location[2][1][2][0].text,
                      location[5][1][2][0].text)

    return '很抱歉，無法提供您該城市的天氣。'

if __name__ == '__main__':
    print(get_current_weather('臺南'))
