import os
import socket
import qrcode
import subprocess
from PIL import Image

# Step 1: Get local IP
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

# Step 2: Generate QR code
def generate_qr(ip):
    url = f"http://{ip}:5000"
    qr = qrcode.make(url)
    qr_path = "link_qr.png"
    qr.save(qr_path)
    print(f"✅ QR code saved for {url} as 'link_qr.png'")
    
    # FIXED: show QR image reliably
    try:
        Image.open(qr_path).show()
    except Exception as e:
        print("❌ Failed to open QR image:", e)
    return url

# Step 3: Start Flask server
def start_server():
    try:
        subprocess.Popen(
    [r"C:\Users\Anu Dwivedi\AppData\Local\Programs\Python\Python311\pythonw.exe", "run.py"],
    creationflags=subprocess.CREATE_NO_WINDOW
)

        print("🚀 Flask server started in background!")
    except Exception as e:
        print("❌ Failed to start Flask app:", e)

# Full flow
if __name__ == "__main__":
    ip = get_local_ip()
    url = generate_qr(ip)
    start_server()

    print("\n📱 Scan the QR with your phone or open:", url)
    input("🔒 Press Enter to close this window...")
