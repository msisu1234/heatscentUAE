import json
import os

FILE = "catalogue.json"

with open(FILE, "r") as f:
    data = json.load(f)

def display():
    print("\nCatalogue:")
    print("\nShown:")
    for item in data["shown"]:
        print(" -", item)

    print("\nHidden:")
    for item in data["hidden"]:
        print(" -", item)
    print()

while True:
    display()

    name = input("Filename to add/change (or 'exit'): ") + ".json".strip()
    if name.lower() == "exit":
        break

    action = input("Type s to show or h to hide: ").strip().lower()

    if action not in ["s", "h"]:
        print("Invalid option.\n")
        continue

    if name in data["shown"]:
        data["shown"].remove(name)
    if name in data["hidden"]:
        data["hidden"].remove(name)

    if action == "s":
        data["shown"].append(name)
    else:
        data["hidden"].append(name)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

    print("Updated catalog.\n")