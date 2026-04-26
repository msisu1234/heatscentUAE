import json
import os

name = input("Name: ")
tag = input("Tag: ")
sort = input("Sort(Men, Women): ").lower() 
new = input("New?(y/n):" ).lower() 

ingredients = input("Ingredients: ")
smell = input("Smell description: ")
info = input("Additional info: ")

image1 = "images/" + input("Image 1 filename: ")
image2 = "images/" + input("Image 2 filename: ")
thumbnail = input("Thumbnail filename: ")

price_25 = float(input("Price for 25ml: "))
price_50 = float(input("Price for 50ml: "))
price_75 = float(input("Price for 75ml: "))
price_100 = float(input("Price for 100ml: "))
sale = 1 - (float(input("Sale %(0 if none)?: ")) / 100) #ask gpt for html rendeirng

data = {
    "name": name,
    "ingredients": ingredients,
    "smell": smell,
    "images": [image1, image2],
    "prices": {
        "25ml": price_25 * sale,
        "50ml": price_50 * sale,
        "75ml": price_75 * sale,
        "100ml": price_100 * sale, #prob wrong format
    },
    "moreInfo": info,
    "thumbnail": thumbnail,
    "tag": tag,
    "bookMessege": f"Hello! I am interested in buying the {name} fragrance in the size [ENTER VOLUME]",
    "sort": {
        "sort": sort,
        "new": new,
    }
        
}

folder = "perfumes"


filename = f"{name.replace(' ', '_').lower()}.json"
filepath = os.path.join(folder, filename)


with open(filepath, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"{filename} created.")


catalogue_path = "catalogue.json"

with open(catalogue_path, "r", encoding="utf-8") as f:
    catalogue = json.load(f)


if "shown" not in catalogue:
    catalogue["shown"] = []


if filename not in catalogue["shown"]:
    catalogue["shown"].append(filename)

with open(catalogue_path, "w", encoding="utf-8") as f:
    json.dump(catalogue, f, indent=2)

print(f"{filename} added to catalogue.json.")