valid_transitions = {
    "Draft": "Pending Approval",
    "Pending Approval": "Approved",
    "Approved": "Signed"
}

def move_to_next_stage(name):
    for c in contracts:
        current_status = c["status"]
        if c["name"] == name and current_status in valid_transitions:
            c["status"] = valid_transitions[current_status]
            print(f"✅ Moved to {c['status']}")
            return
    print("❌ Cannot move to next stage")
``
