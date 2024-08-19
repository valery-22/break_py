# Suppose we have a list of last-minute items to check before leaving for the trip
last_minute_items = ["boarding pass", "sunglasses", "novel"]
packed_items = ["sunglasses", "novel"]

for item in last_minute_items:
    if item not in packed_items:
        # TODO: Add a print statement to warn about the forgotten item
        print(f"Don't forget your {item}!")
        break