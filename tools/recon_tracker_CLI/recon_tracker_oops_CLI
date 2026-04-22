import os 
import json


class Recon_tracker:
    def __init__(self):
        self.targets = self.load_targets()

    def load_targets(self):
        if os.path.exists("targets.json"):
            try :
                with open("targets.json", "r") as f:
                    self.targets = json.load(f)
            except:
                self.targets =[]
        else:
            return []        
        return self.targets

    def save_targets(self):
        with open("targets.json", "w") as f:
            json.dump(self.targets, f, indent=4)

    def add_target(self):

        host = input("Enter host IP:")
        host_type = input("Host type:")
        new_target = {
            "host": host,
            "type": host_type,
            "status": "in progress",
            "findings": []
        }
        self.targets.append(new_target)
        self.save_targets()

    def list_targets(self):
        for target in self.targets:
            print(f"host : {target['host']} | status : {target['status']}")

    def add_finding(self):
        hosttofind = input("Enter the host IP to find:")
        found = False
        for target in self.targets: 
            if target["host"] == hosttofind:
                findingtoadd =input("Enter the finding you found about host:")
                target["findings"].append(findingtoadd)
                found = True
                print("Finding added.")
        if not found:
            print("Host not found.")
        else:
            self.save_targets()

    def view_target(self):
        hosttofind = input("Enter host:")
        found = False
        for target in self.targets:
            if target['host'] == hosttofind:
                found = True
                print(f"Host: {target['host']} | Type: {target['type']} | Status: {target['status']}")
                for finding in target['findings']:
                    print(f"  - {finding}")
        if not found:
            print("Host not found.")

    def delete_target(self):
        hosttodel = input("Enter host")
        found = False
        for target in self.targets:
            if target['host'] == hosttodel:
                found =True
                self.targets.remove(target)
                print("Target Deleted")
        if not found:
            print("Host not found.")
        else :
            self.save_targets()



tracker = Recon_tracker()
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
    
    if menu == 1: tracker.add_target()
    if menu == 2: tracker.list_targets()
    if menu == 3: tracker.add_finding()
    if menu == 4: tracker.view_target()
    if menu == 5: tracker.delete_target()
    if menu == 6: break
