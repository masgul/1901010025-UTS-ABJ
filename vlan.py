while True:
    def menuVLAN():
        print("*"*20)
        print("MENU VLAN")
        print("*"*20)
        print("1. Add New VLAN \n2. Show VLAN \n0. Exit")
        print("*"*20)

    def addVLAN():
        while True:
            file = open("vlan-database.txt","a")
            x = input("Enter VLAN ID or type 0 to stop: ")
            if x == '0':
                break
            y = input("Enter VLAN Name: ")
            file.write("VLAN ID: "+x+", VLAN NAME: "+y+"\n")

    def showVLAN():
        file = open("vlan-database.txt","r")
        print("*"*20)
        for item in file:
            item = item.strip()
            print(item)
        print("*"*20)
        file.close()
        
# Main Apps
    menuVLAN()
    i = input("Enter the choice: ")
    print("*"*20)
    if i == '1' :
        addVLAN()
        print("\n")
    elif i == '2':
        print()
        showVLAN()
        print("\n")
    elif i == '0':
        break
    else :
        print("Please provide valid input!")
        print("\n")