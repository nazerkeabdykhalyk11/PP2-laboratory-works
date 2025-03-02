import json

with open("/Users/erkeabdykhalyk/pp2/pp2 labs/lab4/sample-data.json") as file:
    data = json.load(file)

print("Interface status")
print("=" * 85)
print("{:<50} {:<20} {:<7} {:<5}".format("DN", "Description", "Speed", "MTU"))
print("{:<50} {:<20} {:<7} {:<5}".format("-" * 50, "-" * 20, "-" * 7, "-" * 5))  

for items in data["imdata"]:
    item = items["l1PhysIf"]["attributes"]

    descr = item["descr"] if item["descr"] else "-" * 20 
    
    print("{:<50} {:<20} {:<7} {:<5}".format(item["dn"], descr, item["speed"], item["mtu"]))