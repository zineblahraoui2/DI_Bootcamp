brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": 
        {"France" : "blue", 
        "Spain": "red", 
        "US": ["pink", "green"]}
    }
brand.update({"number_stores": 2})
print(f"the values of the key type of the clothes {brand["type_of_clothes"]}")
brand.update({"country_creation":"Spain"})
if "international_competitors" in brand.keys():
    brand["international_competitors"].append("Desigual")  
del brand["creation_date"]
print(brand["international_competitors"][2])
print(brand["major_color"]["US"])
print(len(brand))   
print(brand.keys()) 
more_on_zara = {"creation_date":"number_stores"}
brand.update(more_on_zara) 
print(brand)