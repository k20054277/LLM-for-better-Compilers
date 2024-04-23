import urllib.request

def download_file(url):
    """Downloads a file from a URL"""
    response = urllib.request.urlopen(url)
    data = response.read()
    
    # Check that the response status code is 200 (OK)
    assert response.status == 200, "Error downloading file"
    
    # Save the downloaded file to a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "downloaded_file")
        with open(filename, "wb") as f:
            f.write(data)
    
    # Return the path to the downloaded file
    return filename