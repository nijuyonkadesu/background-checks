import requests

url = "http://localhost:8083/employment/RW1wbG95bWVudFZlcmlmaWNhdGlvbjp5b3VyLWVtYWlsMDEyQGV4YW1wbGUuY29tL2ZkOWRlMDQ0LTJmNTMtNDFhMC04YTY4LWZjYzc2MjBmM2FiZg=="

# Define the form data
data = {
   "full_name": "John Doe",
   "ssn": "111-11-1111",
   "employer": "Acme Inc.",
   "action": "accept"
}


# Send the POST request with the form data
response = requests.post(url, data=data)


# Print the response content
print(response.content)