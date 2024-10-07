import requests


llama_model = "llama3.2:1b"
llama_role = "user"
llama_stream = False

def call_llama(prompt):
    url = "http://ollama:11434/api/chat"
    payload = {
        "model": llama_model,
        "messages": [
            {
                "role": llama_role,
                "content": "Rewrite this post to make it nicer: I hate waiting in line."
            }
        ],
        "stream": llama_stream
    }

    response = requests.post(url, json=payload)

    print("RESPONSE STATUS CODE: ", response.status_code)
    print("RESPONSE JSON: ", response.json())


# call_llama("Rewrite this post to make it nicer: I hate waiting in line.")

