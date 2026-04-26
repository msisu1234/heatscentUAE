import subprocess


print("\nHEATSCENT ADMIN APP")
print("1. Create new perfume JSON")
print("2. Edit catalog")
print("3. Exit")

while True:
    choice = input("Choose an option: ").strip()

    if choice == "1":
        subprocess.run(["python3.14", "create.py"])
    elif choice == "2":
        subprocess.run(["python3.14", "catalogue.py"])
    elif choice == "3":
        break
    else:
        print("Invalid choice, choose 1, 2 or 3")