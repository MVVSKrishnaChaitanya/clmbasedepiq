# Mini CLM Tracker

contracts = []

def create_contract(name, vendor, status):
    contract = {
        "name": name,
        "vendor": vendor,
        "status": status
    }
    contracts.append(contract)
    print("Contract created successfully!")

def view_contracts():
    for c in contracts:
        print(c)

# sample usage
create_contract("Vendor Agreement", "ABC Corp", "Draft")
view_contracts()
``
