
# Sample input: url = "https://www.example.com"
url = "https://www.example.com"

if url.startswith("http"):
    # If URL starts with "http": extract protocol and domain separately
    protocol, domain = url.split("/", 1)
    protocol = protocol.split(":")[0]
elif url.startswith("https"):
    # If URL starts with "https": extract protocol and domain separately
    protocol = url.split("://")[0]
    domain = url.split("/")[2]
else:
    # Handle invalid or empty URLs
    print("Invalid or empty URL provided.")
    protocol = ""
    domain = ""

# Print the extracted parts of the URL
print(f"Protocol: {protocol}")
print(f"Domain: {domain}")
