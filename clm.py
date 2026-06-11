valid_status = ["Draft", "Pending Approval", "Approved", "Signed"]

def update_status(name, new_status):
    if new_status not in valid_status:
        print("❌ Invalid status")
        return
    
    for c in contracts:
        if c["name"] == name:
            c["status"] = new_status
            print("✅ Status updated")
            return
