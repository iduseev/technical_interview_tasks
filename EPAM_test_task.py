"""
We have third party microservice that provides sales in format 
GET /sales?day=<iso format date> "2023-01-01"
[
    {
        "product_id": <str>,
        "store_id": <str>,
        "price": float,
        "timestamp": int - in milliseconds
    },
    ...
]
product_id isn't unique serial id, it's like SKU, for example "Mac Book 15inch 2023 ..."
store_id - is unique store where product was sold
price - actual sale price after all discounts (potentially each item is sold with different price)
timestamp - timestamp in ms since epoch (sale time)

 
We want to implement api to provide aggregated metric on price of sales:
 
GET - /price?product_ids=list[<str>]&store_ids=list[<str>]&days=list[str]  - dates in iso-format like "2023-01-01"
calculates total avg price for all transactions for given set of stores and given set of products
that fall in time of given days list

We need to implement:
* GET - method returning for selected products-in-stores their average price for given list of dates
return total average price as single float Response with body that contains {"total_avg_price": <float>}
"""


import requests
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def acquire_avg_price(product_ids: list[str], store_ids: list[str], days: list[str]):
    
    for day in days:
        r = requests.get(f"/sales?day={day}")
        prices = []
        for elem in r.json():
            if elem.get("product_id") in product_ids and elem.get("store_id") in store_ids:
                price = elem.get("price")
                prices.append(price)
    avg_price = sum(prices) / len(prices)

    return {"total_avg_price": avg_price}
