# Aptos NFT Json Creator
 This python library that makes it easy to generate json files for Aptos network.
# How does it work?
 You can edit and run the json part in the file according to yourself.
# Getting Started
 Welcome to the Aptos-Network-Json-Creator documentation!
 You must have **python 3.9** and above installed on your computer.

## Download 
open cmd (or others terminals)
```
git clone https://github.com/aycanozarpaci/Aptos-Network-Json-Creator.git
```
## Enter in folder
```
cd Aptos-Network-Json-Creator
```
## Open main.py file
Open the **main.py** file with any code editor program. Customize only the json part.
```
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
```
<details><summary>Descriptions JSON Tags</summary>
<p>

#### name

```
   Name is your NFT name after mint (look image)
```
#### description
```
   description is yout NFT description (look image)
```
#### attributes
```
   Attributes is the section where you create the properties of your NFTs. (look image Properties Section)
```
</p>
</details>

![image](https://user-images.githubusercontent.com/44923151/198416444-ab0a9227-1c75-4ee1-a164-23b42ccae4d1.png)


## After editing
After editing your config file, save it and go to cmd (or terminal) and write the following code.
```
  py main.py
```

## Sponsorships   
![cheetah-aptos](https://user-images.githubusercontent.com/44923151/198417841-0ba1a2d5-38ed-4234-a53e-01928509b0cc.png)

[Cheetah.market](https://cheetag.market/
