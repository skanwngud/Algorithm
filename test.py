cur_ip_list = {
    "0": {
        "Name": "interminds",
        "IP": "192.168.30.11",
        "anydesk": "123456789"
    },
    
    "1":
        {
            "Name": "interminds",
            "IP": "192.168.30.12",
            "anydesk": "234567890"
        }
}

add_ip_list = {
    "0":
        {
            "Name": "interminds",
            "IP": "192.168.30.11",
            "anydesk": "123123123"
        },
        
    "1": 
        {
            "Name": "interminds",
            "IP": "192.168.30.30",
            "anydesk": "321321321"
        },
        
    "2":
        {
            "Name": "interminds",
            "IP": "192.168.30.12",
            "anydesk": "111111111"
        }
}

print(cur_ip_list.values())
print(add_ip_list.values())

c = list(cur_ip_list.values())
a = list(add_ip_list.values())

try:
    for c_idx in cur_ip_list.items():
        for a_idx in add_ip_list.items():
            if a_idx[1]["IP"] != c_idx[1]["IP"]:
                cur_ip_list[len(cur_ip_list)] = add_ip_list.pop(str(a_idx[0]))
except Exception:
    pass

print(cur_ip_list)