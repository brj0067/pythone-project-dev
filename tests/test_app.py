import os
from http.server import HTTPServer

import pytest

from app import SimpleHandler, APP_NAME


@pytest.fixture
def test_server_address(monkeypatch):
    # Use a different port in tests to avoid conflicts
    monkeypatch.setenv("PORT", "0")
    server_address = ("localhost", 0)
    httpd = HTTPServer(server_address, SimpleHandler)
    yield httpd
    httpd.server_close()


def test_app_name_default():
    assert APP_NAME == os.getenv("APP_NAME", "devops-demo-app")

