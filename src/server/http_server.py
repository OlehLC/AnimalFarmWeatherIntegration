import http.server
import socketserver
import urllib.parse

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Парсинг параметрів запиту
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        # Перевірка параметра login
        login = query_params.get('login', [None])[0]

        if login == "lobko_oleg":
            # Формування відповіді
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            response = "Лобко, Олег, 2, ІС-31".encode('utf-8')
            self.wfile.write(response)
        else:
            # Помилка, якщо логін неправильний
            self.send_response(400)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Неправильний логін!".encode('utf-8'))

# Запуск сервера
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Сервер запущено на порту {PORT}")
    httpd.serve_forever()