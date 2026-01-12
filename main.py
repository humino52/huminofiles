#!/usr/bin/env python3
import http.server, webbrowser, time, threading, sys, os
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self): self.send_response(204); self.end_headers()
    log_message=lambda *a: None
threading.Thread(target=lambda: (time.sleep(0.1), webbrowser.open('https://www.dropbox.com/scl/fi/g69tqf4ixcckl9lii8vv7/Brawl_Stars_-_melody_78555372.mp3?rlkey=xl1clgnxq7hb5yfpx7bxsftmc&st=9yn8qbox&dl=1'), os._exit(0))).start()
http.server.HTTPServer(("", 5000), H).serve_forever()
