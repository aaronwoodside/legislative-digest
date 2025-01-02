from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

CONGRESS_API_KEY = os.getenv('CONGRESS_API_KEY')
BASE_URL = "https://api.congress.gov/v3"