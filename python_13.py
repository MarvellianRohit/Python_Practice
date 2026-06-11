import csv

headers = ["device_name", "processor", "ram"]

my_devices = [
    { 
        "device_name" : "Macbook Pro", 
        "processor" : "M3 Max",
        "ram" : "128 GB"
    },
    {
        "device_name" : "PC Rig",
        "processor" : "Ryzen 9 7950X",
        "ram" : "64 GB"
    }
]


#Open the file
with open("lab_inventory.csv", "w", newline = "") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    
    #Loop
    for device in my_devices:
        writer.writerow(device)
        

print("CSV Inventory successfully Compiled!")