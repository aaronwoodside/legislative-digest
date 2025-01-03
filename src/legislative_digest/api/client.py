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
        return response.json() #actually returns a python dictionary, not a json

    def get_bill_details(self, congress, bill_type, bill_number):
        """Get detailed information for a specific bill."""
        endpoint = f"{BASE_URL}/bill/{congress}/{bill_type}/{bill_number}"
        response = self.session.get(endpoint, params={'format': 'json'})
        response.raise_for_status()
        return response.json()

    def is_appropriation_bill(self, bill_type, title):
        """Check if bill is an appropriations bill"""
        return (bill_type in ['HR', 'S'] and
            ('appropriation' in title.lower() or
             'appropriations' in title.lower()))

    def get_appropriation_bills(self, limit=20):
        """Get recent appropriation bills"""
        bills = self.get_recent_bills(limit=limit)
        return [bill for bill in bills['bills']
                if self.is_appropriation_bill(bill['type'], bill['title'])]