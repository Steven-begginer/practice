import requests

response = requests.get("https://aws.amazon.com/cn/api-gateway/#topic-0")
print(response)
print(response.raise_for_status())

# Print the content type
print("Content-Type:", response.headers.get("Content-Type"))

# Print the first 200 characters of the response
print(response.text)
