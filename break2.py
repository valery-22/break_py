# Essential gadgets needed for the conference
essential_gadgets = ["laptop", "charger", "adapter", "USB drive"]
packed_items = ["laptop", "USB drive", "notebooks", "pens"]

for gadget in essential_gadgets:
    if gadget not in packed_items:
        print(f"Remember to pack your {gadget}.")
        # This logic currently does not stop after finding the first missing item.
        break