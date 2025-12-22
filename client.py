from google import genai

def get_client(api_key):
    return genai.Client(api_key=api_key)