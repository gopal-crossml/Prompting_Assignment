from dotenv import load_dotenv
import os

# Loading env file for the gemini api key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")