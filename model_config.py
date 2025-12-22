from google.genai import types

MODEL_NAME = "gemini-3-flash-preview"

GENERATION_CONFIG = types.GenerateContentConfig(
    temperature=0.1,
    top_p=0.9,
    max_output_tokens=1000

)
