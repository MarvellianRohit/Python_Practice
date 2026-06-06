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
    try:
        print(i["Graphics_Card"])
    except KeyError:
        print("GPU Specification not found for this system.")
