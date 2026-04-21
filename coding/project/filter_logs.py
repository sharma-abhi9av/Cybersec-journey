# Input gped here
targets = [{"ip": "192.168.1.1", "port": 22}, {"ip": "10.0.0.5"}, {"ip": "172.16.0.8", "port": 80}]

for target in targets:
    ip = target["ip"]
    try:
        port = target["port"] 
    except:
        port = "No port provided"
    print(f"IP: {ip} | Port: {port}")
    
