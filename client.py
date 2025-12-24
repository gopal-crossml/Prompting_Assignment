from google import genai
from cred import gemini_api_key

# Function for creating client
def get_client(gemini_api_key):
    return genai.Client(api_key=gemini_api_key)
client = get_client(gemini_api_key)