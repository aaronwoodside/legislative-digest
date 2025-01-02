import requests
from ..config import CONGRESS_API_KEY, BASE_URL

class CongressClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.params = {'api_key': CONGRESS_API_KEY}

    def get_recent_bills(self, limit=20, offset=0):
        """Get most recently updated bills."""
        endpoint = f"{BASE_URL}/bill"
        params = {
            'limit': limit,
            'offset': offset,
            'format': 'json'
        }
        response = self.session.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    def get_bill_details(self, congress, bill_type, bill_number):
        """Get detailed information for a specific bill."""
        endpoint = f"{BASE_URL}/bill/{congress}/{bill_type}/{bill_number}"
        response = self.session.get(endpoint, params={'format': 'json'})
        response.raise_for_status()
        return response.json()