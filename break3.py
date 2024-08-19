# Preparing for a conference trip and checking essential items
conference_items = ["laptop", "charger", "notepad", "business cards"]
packed_items = ["laptop", "notepad", "business cards"]

for item in conference_items:
    if item not in packed_items:
        print(f"Forgot to pack {item}")