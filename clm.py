while True:
    print("\n1. Create Contract")
    print("2. View Contracts")
    print("3. Update Status")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter contract name: ")
        vendor = input("Enter vendor: ")
        status = input("Enter status: ")
        create_contract(name, vendor, status)

    elif choice == "2":
        view_contracts()

    elif choice == "3":
        name = input("Enter contract name: ")
        new_status = input("Enter new status: ")
        update_status(name, new_status)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
``
