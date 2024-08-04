import requests
import json
import xmltodict


store_hash = 'YOUR_STORE_HASH'
access_token = 'YOUR_ACCESS_TOKEN'
base_url = f'https://api.bigcommerce.com/stores/{store_hash}/v3/'


headers = {
    'X-Auth-Token': access_token,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

def fetch_products():
    """Fetch products from BigCommerce."""
    url = base_url + 'catalog/products'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Failed to fetch products. Status code: {response.status_code}")
        return []

def save_as_json(products, filename):
    """Save products as JSON."""
    with open(filename, 'w') as json_file:
        json.dump(products, json_file, indent=4)
    print(f"Products saved to {filename}")

def save_as_xml(products, filename):
    """Save products as XML."""
    # Convert the product list to a dictionary format for XML conversion
    products_dict = {'products': {'product': products}}
    xml_data = xmltodict.unparse(products_dict, pretty=True)
    
    with open(filename, 'w') as xml_file:
        xml_file.write(xml_data)
    print(f"Products saved to {filename}")

def main():
    products = fetch_products()
    if products:
        save_as_json(products, 'products.json')
        save_as_xml(products, 'products.xml')

if __name__ == '__main__':
    main()
