import requests

class FinGPTWrapper:
    def __init__(self):
        self.api_url = "https://e98b-35-203-178-156.ngrok-free.app"

    def __call__(self, prompt):
        payload = {"inputs": prompt}
        response = requests.post(self.api_url, json=payload)
        if response.status_code == 200:
            return response.json()['output']
        else:
            return f"Error: {response.status_code} - {response.text}"
