import tkinter as tk
from tkinter import scrolledtext, INSERT, END, messagebox

def main():
    root = tk.Tk()
    root.title("ChatBot")

    # Create a scrolled text box to display chat history
    chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
    chat_history.pack(padx=10, pady=10)

    # Create an entry for user input
    user_input = tk.Entry(root, width=50)
    user_input.pack(padx=10, pady=(0, 10))

    # Function to handle user input and chatbot response
    def send_message():
        user_message = user_input.get().strip()
        if user_message.lower() == 'exit':
            chat_history.insert(tk.END, "You: " + user_message + "\n")
            chat_history.insert(tk.END, "ChatBot: Goodbye!\n")
            user_input.delete(0, tk.END)
            user_input.config(state=tk.DISABLED)
        else:
            chat_history.insert(tk.END, "You: " + user_message + "\n")
            response = chatbot_response(user_message)
            chat_history.insert(tk.END, "ChatBot: " + response + "\n")
            chat_history.see(tk.END)
            user_input.delete(0, tk.END)

    # Function to handle chatbot responses
    def chatbot_response(input_text):
        if input_text.lower() == 'hello':
            return "Hello there! How can I help you?"
        elif input_text.lower() == 'bye':
            return "Goodbye!"
        elif input_text.lower() == 'thanks':
            return "You're welcome!"
        else:
            try:
                result = calculate(input_text)
                return str(result)
            except ValueError:
                return "Sorry, I don't understand that."

    # Calculator function
    def calculate(expression):
        try:
            result = eval(expression)
            return result
        except Exception as e:
            return "Error: " + str(e)

    # Bind Enter key to send_message function
    root.bind('<Return>', lambda event: send_message())

    root.mainloop()

# Functions for testing
def test_chatbot_response_hello():
    assert chatbot_response("hello") == "Hello there! How can I help you?" # type: ignore

def test_chatbot_response_bye():
    assert chatbot_response("bye") == "Goodbye!" # type: ignore

def test_chatbot_response_calculate():
    assert chatbot_response("2 + 2") == "4" # type: ignore
    assert chatbot_response("10 * 5") == "50" # type: ignore
    assert chatbot_response("10 / 2") == "5.0" # type: ignore

if __name__ == "__main__":
    main()
