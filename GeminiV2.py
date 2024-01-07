import google.generativeai as genai
#insert gemini api here
genai.configure(api_key='')

def to_markdown(text):
    text = text.replace('•', '  *')
    return text

def chat_with_gemini():
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    print("Gemini Chat: Type 'END GEMINI' to exit the conversation.")

    while True:
        user_input = input("You: ")
        
        if user_input.upper() == 'END GEMINI':
            print("Exiting Gemini Chat...")
            break
        
        response = chat.send_message(user_input)
        formatted_response = to_markdown(response.text)

        print("Gemini:", formatted_response)


chat_with_gemini()
