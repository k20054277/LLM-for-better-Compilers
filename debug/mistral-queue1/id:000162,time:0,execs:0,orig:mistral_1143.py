
import urllib.request

def download_url(url, output_file):
    """
    Function to download URL content and save it as output_file
    :param url: str, URL to be downloaded
    :param output_file: str, file path to save the content
    """

    # Using context manager for handling exceptions in case of network issues or other errors
    with urllib.request.urlopen(url) as response:

        if response.status == 200:
            print("Downloading webpage...")
            
            # Reading the entire content at once (can also use 'chunked' mode to read in smaller parts)
            content = response.read()
            
            print(f"Saving content to {output_file}...")
            with open(output_file, "wb") as file:
                file.write(content)
                print("File saved successfully.")
        else:
            print(f"Error while downloading the webpage. Status code received: {response.status}")

if __name__ == "__main__":
    url = "https://example.com"
    output_file = "example.html"
    download_url(url, output_file)
