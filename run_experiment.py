from client import get_client
from model_config import MODEL_NAME, GENERATION_CONFIG
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
def run_experiment(prompts):
    client = get_client(api_key)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompts,
        config=GENERATION_CONFIG
    )

    return response.text

