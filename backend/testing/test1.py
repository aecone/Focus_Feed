import requests

# Define the base URL of your Flask application
base_url = "http://127.0.0.1:5000"

# Step 1: Log in and obtain a session
def login(username, password):
    url = f"{base_url}/login"
    data = {"username": username, "password": password}
    session = requests.Session()
    response = session.post(url, json=data)

    try:
        response_data = response.json()
        if response.status_code == 200:
            print("Login successful.")
            return session  # Return the session with authentication cookies
        else:
            print("Login failed:", response_data)
    except ValueError:
        print("Non-JSON response received during login:", response.status_code, response.text)
    return None

# Step 2: Add a subscription using the authenticated session
def add_subscription(session, insta_username):
    url = f"{base_url}/subscriptions"
    data = {"insta_username": insta_username}
    response = session.post(url, json=data)

    try:
        response_data = response.json()
    except ValueError:
        print("Non-JSON response received:", response.status_code, response.text)
        return False

    print("Add Subscription Response:", response_data)
    return response.status_code == 201

# Test function that performs login and attempts to add a subscription
def test_add_subscription(username, password, insta_username):
    session = login(username, password)
    if session:
        success = add_subscription(session, insta_username)
        if success:
            print(f"Subscription to {insta_username} added successfully.")
        else:
            print(f"Failed to add subscription to {insta_username}.")
    else:
        print("Login failed; could not proceed with adding subscription.")

# Run the test with specified credentials and Instagram username
test_add_subscription("test", "halo", "rutgerswics")
