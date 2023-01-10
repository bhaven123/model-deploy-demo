# https://huggingface.co/docs/api-inference/detailed_parameters#text-classification-task
import requests
import json

# HuggingFace Inference API
API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(filename: str):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
