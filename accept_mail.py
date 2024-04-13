import requests

url = "http://localhost:8083/candidate/QWNjZXB0OnlvdXItZW1haWxAZXhhbXBsZS5jb20vMDA1NjAyYzgtNzkzYy00ZmMyLWI0MDMtMTQyYmMzOTQwMWE5"
url = "http://localhost:8083/employment/RW1wbG95bWVudFZlcmlmaWNhdGlvbjp5b3VyLWVtYWlsMDFAZXhhbXBsZS5jb20vNDI5MjI5M2EtMzU4Ni00OGQwLThiM2QtODNmNjk2YzMzNDJk"

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