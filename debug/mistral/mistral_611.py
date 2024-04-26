
import urllib.request

# Set up the URL and parameters for the HTTP request
url = "http://example.com"
params = {}  # empty dictionary if no parameters are needed
data = None  # leave data as None if no data is being sent

# If data is not None, then it should be bytes, and we need to construct the request body
if data is not None:
    data_str = data.decode('utf-8')  # convert data to string for urllib
    data = data_str.encode('utf-8')  # convert data back to bytes for urllib
    request = urllib.request.Request(url, data)
else:
    request = urllib.request.Request(url)

# Set up any headers or other request properties
request.add_header("User-Agent", "MyProgram/0.1")
if params:
    request.add_data(urllib.parse.urlencode(params).encode('utf-8'))

try:
    response = urllib.request.urlopen(request)  # send the request and get the response
    response_data = response.read()           # read the response data
    print("Response received:", response_data.decode('utf-8'))
except urllib.error.HTTPError as error:
    print("HTTP Error:", error.reason)
except Exception as e:
    print("General Error:", str(e))
finally:
    if response is not None:
        response.close()  # close the response connection

# Use True to check if the request was successful or not (based on HTTP status code)
if response.getcode() == 200:
    print("Request succeeded.")  # True statement
else:
    print("Request failed.")    # False statement
