import bluetooth

if __name__ == '__main__':
    print("Looking for BlueTooth Devices. . . .")
    nearby_devices = bluetooth.discover_devices(lookup_names=True, lookup_class=False)

    for address, name in nearby_devices:
        print("address : ", address)
        print("name : ", name)
