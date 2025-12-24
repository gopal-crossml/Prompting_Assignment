from client import get_client
from constant import MODEL_NAME, GENERATION_CONFIG
from client import client

# This function returns the text from the client model
def run_experiment(prompts):
    '''
     Generate model output for the given prompts using the configured Gemini model.

    Args:
        prompts: Prompt or the contents send to the model.

    Returns:
        str: Generated text response from the model.
    '''

# Creating response with the help of client model,content and config
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompts,
        config=GENERATION_CONFIG
    )

    return response.text

