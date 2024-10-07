from requester_services.llama_requester import call_llama


def make_llama_call(prompt):

    llama_response = call_llama(prompt)
    print("HELPER LLAMA RESP: ", llama_response)

    return llama_response


