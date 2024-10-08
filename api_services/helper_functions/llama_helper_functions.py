from requester_services.llama_requester import call_llama


def make_llama_call(user_post):
    prompt_length = len(user_post.split())
    print(prompt_length)

    prompt = f"Using {prompt_length} words, respond only with the rewritten text for the following prompt: Please rewrite the following sentence to give it positive sentiment while keeping the context the same: {user_post}. Do not answer questions."
    llama_response = call_llama(prompt)
    print("HELPER LLAMA RESP: ", llama_response)

    return llama_response


