from ..imports.shared_imports import *

api_key : str = ""
serper_api_key : str = ""
# function to load variables
def gemini_key():
    dotenv_path = os.path.join(os.path.dirname(__file__), r'..\configuration\.env')
    if load_dotenv(dotenv_path) == True:
        api_key = os.getenv('api_key')
        print("API Key accessed successfully")
    else:
        raise RuntimeError ("api key not found")
    return api_key

def serper_key():
    dotenv_path = os.path.join(os.path.dirname(__file__), r'..\configuration\.env')
    if load_dotenv(dotenv_path) == True:
        serper_api_key = os.getenv('serper_api_key')
        print("Serper api Key accessed successfully")
    else:
        raise RuntimeError ("api key not found")
    return serper_api_key
