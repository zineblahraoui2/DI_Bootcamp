items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
wallet_int = int(wallet.replace("$", "").replace(",", ""))
basket = []
for item, price in items_purchase.items():
    price_int = int(price.replace("$", "").replace(",", ""))
    if price_int <= wallet_int:
        basket.append(item)
        wallet_int -= price_int 

if basket:
    print(sorted(basket))  
else:
    print("Nothing")

    



        


    
