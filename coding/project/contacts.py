import os 
import json 


contacts =[]
if os.path.exists("contact.json"):
    with open("contact.json", "r") as f:
        contacts = json.load(f)


while True :
    print("""=== Contact Book ===
1. Add contact
2. List all contacts
3. Search by name
4. Delete contact
5. Exit""")
    try:
        menu = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a number.")
        continue
    print(menu)
    if menu == 5 :
        print("Bye")
        break

# Add an contact 
    if menu == 1 : 

            print("Add an Contact")
            name = input("Enter name : ")
            phone = (input("Enter phone no: ")
            email = input("Enter email :")
            add_contact = {
                "name": name,
                "phone": phone,
                "email": email
                        }
            print(add_contact)
            contacts.append(add_contact)
            with open("contact.json" , "w") as f:
                json.dump(contacts, f, indent = 4 )
                print("Contact Saved!")
        

# All contacts 
    if menu==2 :
        if os.path.exists("contact.json"):
            with open("contact.json" , "r") as f:
                loaded = json.load(f)
            # print contact list in seperate lines 
            for item in loaded:
                print(item['name'], item["phone"], item["email"])
        else:
            print("No contacts yet.")



# Search a name in contacts 
    if menu == 3: 
        if os.path.exists("contact.json"):
            search_name = input("Search the name :")
            if not search_name:
                print("Please enter a name.")
                continue
            with open("contact.json", "r") as f :
                loaded = json.load(f)
            found = False
            for item in loaded:
                if search_name in item["name"] :
                    print(item["name"])
                    found = True
            if not found: 
                print("No contact found")
        else:
            print("No contacts yet.")





# Delete an contact
    if menu == 4: 
        if os.path.exists("contact.json"):
            delete_contact = input("Enter the name to delete:")
            if not delete_contact:
                print("Please enter a name.")
                continue
            with open("contact.json", "r") as f :
                loaded = json.load(f)
            deleted = False    
            new_list = []
            for item in loaded:
                if delete_contact not in item["name"]:
                    new_list.append(item)
                elif delete_contact in item["name"]  : 
                    deleted = True
                    print(f"Contact Deleted {item["name"]}")
            with open("contact.json", "w") as f:
                json.dump(new_list, f, indent = 4)
            if not deleted:
                print("No contact found")
        else:
            print("No contacts yet.")
