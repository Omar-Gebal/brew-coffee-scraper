import sys
from fetchers import get_all_products

def main():
    """Echo the input arguments to standard output"""
    products = get_all_products()
    print(products[0])
    
if __name__ == '__main__':
    main()