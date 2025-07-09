import requests
import json
import time

url = "https://search.nosto.com/v1/graphql"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'text/plain',
    'X-Nosto-Integration': 'Search Templates',
    'Origin': 'https://prima-coffee.com',
    'Connection': 'keep-alive',
    'Referer': 'https://prima-coffee.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'TE': 'trailers'
}


def get_all_products() -> list:
  all_products = []
  #got this value from their website as the maximum results per page
  size = 100
  from_value = 0
      
  #Pagination to get all the products
  while True:
      payload_dict = {
          "query": """query ( $abTests: [InputSearchABTest!], $accountId: String, $query: String, $segments: [String!], $rules: [String!], $products: InputSearchProducts, $keywords: InputSearchKeywords, $sessionParams: InputSearchQuery ) { search( accountId: $accountId query: $query segments: $segments rules: $rules products: $products keywords: $keywords sessionParams: $sessionParams abTests: $abTests ) { query redirect products { hits { productId url name imageUrl thumbUrl description brand variantId availability price priceText categoryIds categories customFields { key value } priceCurrencyCode datePublished listPrice unitPricingBaseMeasure unitPricingUnit unitPricingMeasure googleCategory gtin ageGroup gender condition alternateImageUrls ratingValue reviewCount inventoryLevel skus { id name price listPrice priceText url imageUrl inventoryLevel customFields { key value } availability } pid onDiscount extra { key value } saleable available tags1 tags2 tags3 } total size from facets { ... on SearchTermsFacet { id field type name data { value count selected } } ... on SearchStatsFacet { id field type name min max } } collapse fuzzy categoryId categoryPath } abTests { id activeVariation { id } } } }""",
          "variables": {
              "accountId": "bigcommerce-6h7ychjk4",
              "products": {
                  "facets": ["*"],
                  "categoryPath": "brew/coffee",
                  "filter": [{
                      "not": [{
                          "all": [
                              {"field": "availability", "value": ["OutOfStock"]},
                              {"field": "categories", "value": ["Deals"]}
                          ]
                      }]
                  }],
                  "size": size,
                  "from": from_value
              },
              "sessionParams": {
                  "segments": [
                      "65dce9ec52aa186fcce15157", "613aa0000000000000000002", "61c26a800000000000000002",
                      "5b71f1500000000000000006", "66cf84f56c5b924dabb17178", "654e6bc80bc6a20068cb13ad",
                      "650c7f9bde6fa168ee878afd"
                  ],
                  "products": {
                      "personalizationBoost": [{
                          "field": "affinities.categories",
                          "weight": 1,
                          "value": ["brew/coffee", "brew"]
                      }]
                  }
              },
              "abTests": []
          }
      }
      response = requests.post(url, headers=headers, data=json.dumps(payload_dict))
      response.raise_for_status()
      hits = response.json()["data"]["search"]["products"]["hits"]
      if not hits:
        break

      all_products.extend(hits)
      from_value += size

      # delay to avoid overloading the server
      time.sleep(0.5)
  return all_products