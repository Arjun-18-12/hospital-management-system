import requests # Pyre trigger 2
import json

BASE_URL = "http://localhost:8000"

def test_chatbot():
    # 1. Login to get token
    print("Logging in...")
    login_data = {
        "email": "test4@example.com",
        "password": "password123"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    if response.status_code != 200:
        print(f"Login failed: {response.text}")
        return
    
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    print("Login successful.")

    # 2. Test Chatbot
    print("Testing Chatbot...")
    chat_data = {"message": "Hello AI assistant, what services does this hospital provide?"}
    response = requests.post(f"{BASE_URL}/chatbot/", json=chat_data, headers=headers)
    
    if response.status_code == 200:
        print("Chatbot Response:")
        print(response.json()["response"])
    else:
        print(f"Chatbot request failed: {response.status_code}")
        print(response.text)

    # 3. Test History
    print("\nTesting Chat History...")
    response = requests.get(f"{BASE_URL}/chatbot/history", headers=headers)
    if response.status_code == 200:
        history = response.json()
        print(f"History items found: {len(history)}")
        for item in history:
            print(f"- User: {item['user_message'][:50]}...")
            print(f"  AI: {item['ai_response'][:50]}...")
    else:
        print(f"History request failed: {response.status_code}")

if __name__ == "__main__":
    test_chatbot()

# IDE Refresher