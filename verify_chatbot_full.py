import requests # Pyre trigger 2
import json
import time

BASE_URL = "http://localhost:8000"

def full_test():
    email = f"test_{int(time.time())}@example.com"
    password = "Password123!"
    
    # 1. Signup
    print(f"Signing up with {email}...")
    signup_data = {
        "email": email,
        "password": password,
        "full_name": "Test User",
        "phone": "1234567890",
        "address": "123 Test St",
        "date_of_birth": "1990-01-01",
        "gender": "Other"
    }
    try:
        response = requests.post(f"{BASE_URL}/auth/signup", json=signup_data)
        print(f"Signup Response: {response.status_code}")
    except Exception as e:
        print(f"Signup Error: {e}")
        return

    # 2. Login
    print("Logging in...")
    login_data = {
        "email": email,
        "password": password
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    if response.status_code != 200:
        print(f"Login failed: {response.text}")
        return
    
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    print("Login successful.")

    # 3. Test Chatbot
    print("Testing Chatbot...")
    chat_data = {"message": "Hello, can you tell me about the hospital's emergency services?"}
    response = requests.post(f"{BASE_URL}/chatbot/", json=chat_data, headers=headers)
    
    if response.status_code == 200:
        print("Chatbot Response:")
        print(response.json()["response"])
    else:
        print(f"Chatbot request failed: {response.status_code}")
        print(response.text)

    # 4. Test History
    print("\nTesting Chat History...")
    response = requests.get(f"{BASE_URL}/chatbot/history", headers=headers)
    if response.status_code == 200:
        history = response.json()
        print(f"History items found: {len(history)}")
        for item in history:
            print(f"- User: {item['user_message']}")
            print(f"  AI: {item['ai_response'][:100]}...")
    else:
        print(f"History request failed: {response.status_code}")

if __name__ == "__main__":
    full_test()

# IDE Refresher