import json
import os

file_name = input('Folder Name (e.g metadata) = ?\n')
start_number = input('Start Number (Json name eg. 1.json) ?\n')
total_json_number = input('How many json files do you want to create? \n')
dirName = file_name
try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")
print("==================================================")
for x  in range(int(total_json_number)):
  dictionary = {
    "name": "Your_Nft_Name_Here # "+str(x+int(start_number))+"",
    "description": "Your_Description_Here",
    "attributes": [
      { "trait_type": "Background", "value": "Black" },
      { "trait_type": "Eyeball", "value": "Red" },
      { "trait_type": "Eye color", "value": "Yellow" },
      { "trait_type": "Iris", "value": "Small" },
      { "trait_type": "Shine", "value": "Shapes" },
      { "trait_type": "Bottom lid", "value": "Low" },
      { "trait_type": "Rarity", "value": "Special" }
    ]
  }
  print("Created " + str(x+int(start_number)) + ".json file in "+file_name+" Folder")
  json_object = json.dumps(dictionary, indent=4)
  with open(file_name+"/"+str(x+1)+".json", "w") as outfile:
      outfile.write(json_object)
print("==================================================")
print("Total Created json File : "+str(total_json_number)+" Job Fineshed.")