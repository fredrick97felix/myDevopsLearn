python -m http.server 8000 // to server on one line

openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes // ssl key