"""
Without using libraries for parsing, parse (get certain data) the log file of the web server nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) -
get a list of tuples like this: (<remote_addr>, <request_type>, <requested_resource>).
For example:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
"""

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    list_of_web_server_log_tuples = []
    for line in file_1:
        remote_addr, _, _, _, _, request_type, requested_resource, *_ = line.split()
        web_server_log_tuple = (remote_addr, request_type.lstrip('"'), requested_resource)
        list_of_web_server_log_tuples.append(web_server_log_tuple)
print(list_of_web_server_log_tuples)
