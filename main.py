import json
import time
from fetchers import get_all_products, get_product_details

def main():
    try:
        products = get_all_products()
        print(f"total products fetched: {len(products)}")
    except Exception as e:
        print(f"failed to get products, with exception {e}")
        return
    
    products.sort(key=lambda x: float(x["price"]))
    
    #Exporting all products sorted
    formatted_products = []
    for product in products:
        formatted_products.append(
            {
                "url": product["url"],
                "price": product["price"],
                "title": product["name"]
            }
        )
    with open("sorted-products.json", "w", encoding="utf-8") as f:
        json.dump(formatted_products, f, ensure_ascii=False, indent=2)
    
    #Exporting cheapest 5 products in complete detail
    detailed_cheapest_products = []
    for product in products[:5]:
        try:
            details = get_product_details(product["productId"])
            detailed_cheapest_products.append(details)
        except Exception as e:
            print(f"failed to fetch details for product {product['productId']}, with exception {e}")
        # delay to avoid overloading the server
        time.sleep(0.5)

    with open("5-cheapest-products.json", "w", encoding="utf-8") as f:
        json.dump(detailed_cheapest_products, f, ensure_ascii=False, indent=2)
    
if __name__ == '__main__':
    main()
