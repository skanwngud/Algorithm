cur_ip_list = {
    "0": {
        "Name": "interminds",
        "IP": "192.168.30.11",
        "anydesk": "123456789"
    },
    
    "1":
        {
            "Name": "val1",
            "IP": "192.168.30.12",
            "anydesk": "234567890"
        }
}

add_ip_list = {
    "0":
        {
            "key1": "val1",
            "key2": "val1",
            "key3": "val12313"
        },
        
    "1": 
        {
            "key1": "val1",
            "key2": "val2",
            "key3": "val4334"
        },
        
    "2":
        {
            "key1": "val0",
            "key2": "val223",
            "key3": "val12312313231"
        }
}

print(b)

for idx in list(a.values()):
    for jdx in list(b.values()):
        if idx["key2"] == jdx["key2"]:
            print(idx["key2"])
            b[len(b.values())] = idx
            
print(b)