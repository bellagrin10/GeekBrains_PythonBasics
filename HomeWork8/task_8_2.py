"""
*Написать регулярное выражение для парсинга файла логов web-сервера nginx_logs.txt:
https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
для получения информации вида:
(<remote_address>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0
"-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
"""
import re
from itertools import zip_longest

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    txt = f.read()

    remote_address = re.compile(r'^\d+(?:[.]\d+){3}|\w+(?:[:]\w*){5,}', re.M)
    request_datetime = re.compile(r'\d{2}[/]\w+[/]\d{4}(?::\d{2}){3} \+\d{4}')
    request_type = re.compile(r'"([A-Z]+\b)')
    requested_resource = re.compile(r'(?:/[a-z]+){2}_\d')
    response_code = re.compile(r'(?<=" )(\d{3}\b)')
    response_size = re.compile(r'\b\d+(?= ")')

    remote_address = remote_address.findall(txt)
    request_datetime = request_datetime.findall(txt)
    request_type = request_type.findall(txt)
    requested_resource = requested_resource.findall(txt)
    response_code = response_code.findall(txt)
    response_size = response_size.findall(txt)
    parsed_file = zip_longest(remote_address, request_datetime, request_type, requested_resource, response_code,
                              response_size, fillvalue=None)
    print(*parsed_file)
