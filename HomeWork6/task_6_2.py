"""
* Find the spammer's IP address and the number of requests sent to him according to the log file data
 from the previous task.
Note: The spammer is the client with the most requests;
the code should work even with files that are larger than the computer's RAM.
"""

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    spammers = {}
    for line in file_1:
        IP = line.split()[0]
        spammers.setdefault(IP, 0)
        spammers[IP] += 1

spammers_dict_swapped = {v: k for k, v in spammers.items()}
number_of_requests = max(spammers_dict_swapped)
IP_address_of_spammer = spammers_dict_swapped[number_of_requests]
print(f"The spammer's IP address: {IP_address_of_spammer}")
print(f"The number of requests sent to him: {number_of_requests}")
