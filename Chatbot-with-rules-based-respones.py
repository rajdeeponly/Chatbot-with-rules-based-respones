data={
    "hi":"Hi there! I'm a friendly chatbot here to assist you?",
    "hello":"Hello! How can I help you today?",
    "what is your name":"So I don't have a name, but you can call me ChatBot.",
    "where are you from":"I'm from the internet server,always ready to chat!",
    "how are you":"I'm just a chatbot,but I'm here to assist you.",
    "bye":"Bye! Take care and have a great day!",
}
def get_response(user_input):
    for pattern,response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry,I didn't understand that.Can you please rephrase your sentence?"
print("Chatbot: Hi! I'm a simple chatbot,I'm here to assist you!")
while True:
    user_input=input("Mass: ")
    if user_input=='bye':
       print("Chatbot: Goodbye! Have a great day!")
       break
    response=get_response(user_input)
    print("Chatbot:",response)
    

    

    