from msal import PublicClientApplication
import json
import requests
class LLMClient:
    _ENDPOINT = 'https://fe-26.qas.bing.net/sdf/'
    _SCOPES = ['https://substrate.office.com/llmapi/LLMAPI.dev']
    _API = 'chat/completions'
    def __init__(self, endpoint):
        self._app = PublicClientApplication('68df66a4-cad9-4bfd-872b-c6ddde00d6b2',
                                            authority='https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47',
                                            allow_broker=True)
        if endpoint != None:
            LLMClient._ENDPOINT = endpoint
        LLMClient._ENDPOINT += self._API
    def send_request(self, model_name, request):
        # get the token
        token = self._get_token()
        # populate the headers
        headers = {
            'Content-Type':'application/json', 
            'Authorization': 'Bearer ' + token, 
            'X-ModelType': model_name }
        body = str.encode(json.dumps(request))
        # DELETE , verify=False !!!!!
        response = requests.post(LLMClient._ENDPOINT, data=body, headers=headers, verify=False)
        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}. Response: {response.text}")
        return response.json()
    def _get_token(self):
        accounts = self._app.get_accounts()
        result = None
        if accounts:
            # Assuming the end user chose this one
            chosen = accounts[0]
            # Now let's try to find a token in cache for this account
            result = self._app.acquire_token_silent(LLMClient._SCOPES, account=chosen)
        if not result:
            result = self._app.acquire_token_interactive(scopes=LLMClient._SCOPES, parent_window_handle=self._app.CONSOLE_WINDOW_HANDLE)
            if 'error' in result:
                raise ValueError(
                    f"Failed to acquire token. Error: {json.dumps(result, indent=4)}"
                )
        return result["access_token"]
def get_gpt_response(prompt, model_name):
    request_data = {
        "messages": [
            {
                "role": "system",
                "content": "You are an expert in data analysis. Provide detailed information to help the user.",
            },
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ],
        "max_tokens": 4000,
        "temperature": 0.6,
        "top_p": 1,
        "n": 1,
        "logprobs": None,
        "stop": "\r\n"
    }
    response = llm_client.send_request(model_name, request_data)
    response_content = response['choices'][0]['message']['content']
    return response_content
_ENDPOINT = 'https://fe-26.qas.bing.net/sdf/'
llm_client = LLMClient(_ENDPOINT)