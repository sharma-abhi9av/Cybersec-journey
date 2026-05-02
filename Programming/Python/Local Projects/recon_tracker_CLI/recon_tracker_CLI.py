import os 
import json



def load_targets():
    if os.path.exists("targets.json"):
        try :
            with open("targets.json", "r") as f:
                targets = json.load(f)
        except:
            targets =[]
    else:
        return []        
    return targets

def save_targets(targets):
    with open("targets.json", "w") as f:
        json.dump(targets, f, indent=4)

def add_target(targets):

    host = input("Enter host IP:")
    host_type = input("Host type:")
    new_target = {
        "host": host,
        "type": host_type,
        "status": "in progress",
        "findings": []
    }
    targets.append(new_target)
    save_targets(targets)

def list_targets(targets):
    for target in targets:
         print(f"host : {target['host']} | status : {target['status']}")

def add_finding(targets):
    hosttofind = input("Enter the hostname or IP to find:")
    found = False
    for target in targets: 
        if target["host"] == hosttofind:
            findingtoadd =input("Enter the finding you want to add about host:")
            target["findings"].append(findingtoadd)
            found = True
            print("Finding added.")
    if not found:
        print("Host not found.")
    else:
        save_targets(targets)

def view_target(targets):
    hosttofind = input("Enter hostname or IP:")
    found = False
    for target in targets:
        if target['host'] == hosttofind:
            found = True
            print(f"Host: {target['host']} | Type: {target['type']} | Status: {target['status']}")
            for finding in target['findings']:
                print(f"  - {finding}")
    if not found:
        print("Host not found.")

def delete_target(targets):
    hosttodel = input("Enter host")
    found = False
    for target in targets:
        if target['host'] == hosttodel:
            found =True
            targets.remove(target)
            print("Target Deleted")
    if not found:
        print("Host not found.")
    else :
        save_targets(targets)


targets = load_targets()
while True:
    print("""
1. Add target
2. List targets
3. Add finding
4. View target
5. Delete target
6. Exit""")
    try:
        menu = int(input("Choose: "))
    except ValueError:
        print("Enter a number.")
        continue
    
    if menu == 1: add_target(targets)
    if menu == 2: list_targets(targets)
    if menu == 3: add_finding(targets)
    if menu == 4: view_target(targets)
    if menu == 5: delete_target(targets)
    if menu == 6: break
