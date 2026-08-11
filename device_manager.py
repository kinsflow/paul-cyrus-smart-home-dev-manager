# Smart Home Device Manager for Bright Minds Academy
# Stores devices in a list of dictionaries (no database needed)

# each device looks like: {"name": "Smart Light A1", "room": "Room 3", "status": "online"}
devices = []

VALID_STATUSES = ["online", "offline", "maintenance"]


def find_device(name):
    # returns the device dictionary if it exists, otherwise None
    for device in devices:
        if device["name"].lower() == name.lower():
            return device
    return None


def add_device():
    name = input("Enter device name: ").strip()
    if name == "":
        print("Device name cannot be empty.")
        return

    if find_device(name) is not None:
        print("A device with that name already exists.")
        return

    room = input("Enter the room it is located in: ").strip()
    if room == "":
        print("Room cannot be empty.")
        return

    device = {"name": name, "room": room, "status": "offline"}
    devices.append(device)
    print(name + " was added to " + room + " (status: offline).")


def update_status():
    if len(devices) == 0:
        print("There are no devices yet.")
        return

    name = input("Enter the device name to update: ").strip()
    device = find_device(name)
    if device is None:
        print("Device not found.")
        return

    print("Status options: online / offline / maintenance")
    new_status = input("Enter the new status: ").strip().lower()
    if new_status not in VALID_STATUSES:
        print("That is not a valid status.")
        return

    device["status"] = new_status
    print(device["name"] + " is now " + new_status + ".")


def view_devices():
    if len(devices) == 0:
        print("There are no devices yet.")
        return

    print("\nName                 Room            Status")
    print("-" * 45)
    for device in devices:
        print(device["name"].ljust(20), device["room"].ljust(15), device["status"])
    print()


def search_device():
    name = input("Enter the device name to search for: ").strip()
    device = find_device(name)
    if device is None:
        print("Device not found.")
    else:
        print("Name: " + device["name"])
        print("Room: " + device["room"])
        print("Status: " + device["status"])


def main():
    print("Welcome to the Smart Home Device Manager")

    while True:
        print("\n----- MENU -----")
        print("1. Add a new device")
        print("2. Update device status")
        print("3. View all devices")
        print("4. Search for a device")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_device()
        elif choice == "2":
            update_status()
        elif choice == "3":
            view_devices()
        elif choice == "4":
            search_device()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please enter a number between 1 and 5.")


main()
