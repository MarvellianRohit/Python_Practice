
my_setup = [
    {
        "name" : "Macbook",
        "processor" : "M3 Max",
        "RAM" : "128GB",
        "Storage" : "4 TB",
        "OS" : "macOS",
    },
    {
        "name" : "PC Setup",
        "processor" : "AMD Ryzen 9 7950x",
        "RAM" : "64GB",
        "Storage" : "4 TB",
        "OS" : "Windows 11",
    },
]

for i in my_setup:
    print(f"{i['name']} runs on {i['OS']}")
