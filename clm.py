# Mini CLM Tracker

contracts = []

def create_contract(name, vendor, status):
    contract = {
        "name": name,
        "vendor": vendor,
        "status": status
    }
    contracts.append(contract)
    print("✅ Contract created!")

def view_contracts():
    print("\n📄 Contract List:")
    for c in contracts:
        print(f"Name: {c['name']}, Vendor: {c['vendor']}, Status: {c['status']}")

def update_status(name, new_status):
    for c in contracts:
        if c["name"] == name:
            c["status"] = new_status
            print("✅ Status updated!")
            return
    print("❌ Contract not found")

# Sample Run
create_contract("Vendor Agreement", "ABC Corp", "Draft")
view_contracts()

update_status("Vendor Agreement", "Approved")
view_contracts()
