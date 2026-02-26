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
            self._set_headers(content_type="text/html; charset=utf-8")
            html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{APP_NAME}</title>
    <style>
        body {{
            margin: 0;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            background: linear-gradient(135deg, #1e293b, #0f172a);
            color: #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }}
        .hero {{
            text-align: center;
            padding: 3rem 2rem;
            background: rgba(15, 23, 42, 0.9);
            border-radius: 1.25rem;
            box-shadow: 0 25px 50px rgba(15, 23, 42, 0.7);
            max-width: 640px;
            width: 100%;
        }}
        .hero-title {{
            font-size: 2.5rem;
            margin-bottom: 0.75rem;
        }}
        .hero-subtitle {{
            font-size: 1rem;
            color: #9ca3af;
            margin-bottom: 1.5rem;
        }}
        .hero-badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            background: rgba(59, 130, 246, 0.15);
            color: #93c5fd;
            font-size: 0.8rem;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }}
        .hero-actions {{
            margin-top: 1.5rem;
            display: flex;
            gap: 0.75rem;
            justify-content: center;
            flex-wrap: wrap;
        }}
        .btn {{
            padding: 0.7rem 1.4rem;
            border-radius: 999px;
            border: none;
            cursor: pointer;
            font-size: 0.95rem;
            font-weight: 600;
        }}
        .btn-primary {{
            background: #3b82f6;
            color: white;
        }}
        .btn-secondary {{
            background: transparent;
            color: #e5e7eb;
            border: 1px solid rgba(148, 163, 184, 0.6);
        }}
        .hint {{
            margin-top: 1.5rem;
            font-size: 0.8rem;
            color: #9ca3af;
        }}
        .hint code {{
            background: rgba(15, 23, 42, 0.8);
            padding: 0.15rem 0.4rem;
            border-radius: 0.3rem;
            font-size: 0.8rem;
        }}
    </style>
</head>
<body>
    <main class="hero">
        <div class="hero-badge">Python DevOps Demo</div>
        <h1 class="hero-title">Hello from {APP_NAME}!</h1>
        <p class="hero-subtitle">
            A very simple Python web service for practicing DevOps skills:
            running apps, health checks, tests, and containers.
        </p>
        <div class="hero-actions">
            <button class="btn btn-primary">/health endpoint: OK</button>
            <button class="btn btn-secondary">Container‑ready • Port {PORT}</button>
        </div>
        <p class="hint">
            Try opening <code>/health</code> in your browser, or build the Docker image
            with <code>docker build -t devops-demo-app .</code>.
        </p>
    </main>
</body>
</html>"""
            self.wfile.write(html.encode("utf-8"))
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

