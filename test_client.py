from src.legislative_digest.api.client import CongressClient
import json
def test_api():
    client = CongressClient()
    bills = client.get_recent_bills(limit=1)
    try:
        json_data = json.loads(json.dumps(bills))
        print("Bills data is valid JSON!")
    except ValueError as e:
            print(f"Bills data is not valid JSON! Error:{str(e)}")
    #print(json.dumps(bills))
    print_all_keys(bills)

def print_all_keys(data, level=0):
    indent = '    ' * level  # Four spaces per level
    if isinstance(data, dict):
        for key, value in data.items():
            print(f'{indent}{key}')
            if isinstance(value, (dict, list)):
                print_all_keys(value, level + 1)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                print_all_keys(item, level + 1)



if __name__ == "__main__":
    test_api()