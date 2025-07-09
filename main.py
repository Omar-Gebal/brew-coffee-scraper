import json
from fetchers import get_all_products

def main():
    try:
        products = get_all_products()
        print(f"total products fetched: {len(products)}")
    except Exception as e:
        print(f"failed to get products, with exception {e}")

    products.sort(key=lambda x: float(x["price"]))
    
    #Exporting all products
    formatted_products = []
    for product in products:
        formatted_products.append(
            {
                "url": product.get("url"),
                "price": product.get("price"),
                "title": product.get("name")
            }
        )
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(formatted_products, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
