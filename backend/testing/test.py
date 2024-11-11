import requests

url = "http://127.0.0.1:5000/register"
data = {
  "username": "test",
  "password": "halo"
}


response = requests.post(url, json=data)

# Debugging output
print("Status Code:", response.status_code)
print("Response Text:", response.text)

# Attempt to parse JSON if response is successful
if response.status_code == 201 or response.status_code ==200:
    try:
        print(response.json())
    except ValueError:
        print("Response is not in JSON format")
else:
    print("Request failed with status code:", response.status_code)
