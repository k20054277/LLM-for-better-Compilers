from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class DependencyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get the dependency data from the request query string
        dependency = self.path.split('?')[1]

        # Check if the dependency is valid
        if not dependency:
            return False, 400, {'Content-Type': 'text/plain'}

        # Load the dependency JSON file
        with open(dependency + '.json') as f:
            data = json.load(f)

        # Return the dependency data
        return True, 200, {'Content-Type': 'application/json'}, json.dumps(data)

# Create an HTTP server on port 8080 and start it
httpd = HTTPServer(('', 8080), DependencyHandler)
print("Starting httpd...")
httpd.serve_forever()