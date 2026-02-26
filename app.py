import os
from http.server import BaseHTTPRequestHandler, HTTPServer


PORT = int(os.getenv("PORT", "8000"))
APP_NAME = os.getenv("APP_NAME", "devops-demo-app")


class SimpleHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code: int = 200, content_type: str = "text/plain") -> None:
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self) -> None:  # type: ignore[override]
        if self.path == "/":
            self._set_headers()
            self.wfile.write(f"Hello from {APP_NAME}!\n".encode("utf-8"))
        elif self.path == "/health":
            self._set_headers()
            self.wfile.write(b"OK\n")
        else:
            self._set_headers(404)
            self.wfile.write(b"Not Found\n")


def run_server() -> None:
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Starting {APP_NAME} on port {PORT}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()

