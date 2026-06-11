from csv import reader
from csv import writer
import csv

headers = ["node_name", "cpu", "ram"]

cluster_fleet = [
    {
        "node_name" : "Macbook Air",
        "cpu" : "M5",
        "ram" : 16,
    },
    {
        "node_name" : "Macbook Pro",
        "cpu" : "M3 Max",
        "ram" : 128,
    },
    {
        "node_name" : "PC Rig",
        "cpu" : "Ryzen 9 7950X",
        "ram" : 64,
    }
]

with open("fleet_inventory.csv", "w", newline = "") as file: 
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for node in cluster_fleet:
        writer.writerow(node)

with open("fleet_inventory.csv", "r") as file:
    reader = csv.DictReader(file)

    
    for row in reader:
        if int(row["ram"]) >= 64:
           print(f"{row['node_name']} is a high performance Node running {row['cpu']}!")