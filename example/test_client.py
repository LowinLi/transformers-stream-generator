import requests
from datetime import datetime
data = {
    "prompt": "Hello, Amanda! How are you doing?\n",
    "parameters": {
        "max_tokens":180,
        "do_sample":True,
        "top_k":30,
        "top_p":0.85,
        "temperature":0.35,
        "repetition_penalty":1.2,
        "seed":0,
    }
}
# without stream
now = datetime.now()
res = requests.post("http://0.0.0.0:8000/inference", json=data)
print(res.json()["result"])
waste_seconds = (datetime.now() - now).microseconds//1000 + (datetime.now() - now).seconds * 1000
print(f"###\nOriginal api return when inference finished, waste: {waste_seconds} ms\n\n\n")

# with stream
now = datetime.now()
res = requests.post("http://0.0.0.0:8000/inference_stream", json=data, stream=True)
for x in res:
    waste_seconds = (datetime.now() - now).microseconds//1000 + (datetime.now() - now).seconds * 1000
    print(f"at {waste_seconds} ms", x)
print(f"###\nNew api return real-time chunk during inference")