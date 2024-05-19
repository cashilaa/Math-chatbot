# test_project.py

import pytest # type: ignore
from project import chatbot_response, calculate

def test_chatbot_response_hello():
    assert chatbot_response("hello") == "Hello there! How can I help you?"

def test_chatbot_response_bye():
    assert chatbot_response("bye") == "Goodbye!"

def test_chatbot_response_calculate():
    assert chatbot_response("2 + 2") == "4"
    assert chatbot_response("10 * 5") == "50"
    assert chatbot_response("10 / 2") == "5.0"

def test_calculate():
    assert calculate("2 + 2") == 4
    assert calculate("10 * 5") == 50
    assert calculate("10 / 2") == 5.0

# Additional tests can be added as needed

if __name__ == "__main__":
    pytest.main()
