with open("hardware_log.txt", "w") as file:
    file.write("Primary Workstation: Macbook Pro M3 Max\n")
    file.write("Backup Rig: AMD Ryzen 9 7950X\n")

with open("hardware_log.txt", "r") as file:
    content = file.read()
    print(content)