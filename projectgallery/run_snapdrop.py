import subprocess
import socket
import qrcode
import os
import webbrowser

def get_local_ip():
    """Get your local IP address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def generate_qr_and_open(ip):
    """Create QR code from IP and open it."""
    url = f"http://{ip}:5000"
    img = qrcode.make(url)
    qr_path = "snapdrop_qr.png"
    img.save(qr_path)
    os.startfile(qr_path)  # this opens the image
    print(f"\n📱 Scan this QR to open SnapDrop: {url}")
    print("🌐 Or directly open the URL in your browser.")
    return url

def start_flask_server():
    """Start the Flask server from app.py in background."""
    try:
        subprocess.Popen(["python", "app.py"], cwd=os.getcwd())
        print("🚀 Flask server started successfully!")
    except Exception as e:
        print("❌ Error starting Flask:", e)

if __name__ == "__main__":
    ip = get_local_ip()
    url = generate_qr_and_open(ip)
    start_flask_server()
    webbrowser.open(url)  # optional: open in desktop browser

    print("\n✅ Your SnapDrop server is running.")
    print("📌 Keep this window open while using SnapDrop.\n")
    input("🔒 Press Enter to exit (or close this window)...")
import subprocess
import socket
import qrcode
import os
import webbrowser

def get_local_ip():
    """Get your local IP address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def generate_qr_and_open(ip):
    """Create QR code from IP and open it."""
    url = f"http://{ip}:5000"
    img = qrcode.make(url)
    qr_path = "snapdrop_qr.png"
    img.save(qr_path)
    os.startfile(qr_path)  # this opens the image
    print(f"\n📱 Scan this QR to open SnapDrop: {url}")
    print("🌐 Or directly open the URL in your browser.")
    return url

def start_flask_server():
    """Start the Flask server from app.py in background."""
    try:
        subprocess.Popen(["python", "app.py"], cwd=os.getcwd())
        print("🚀 Flask server started successfully!")
    except Exception as e:
        print("❌ Error starting Flask:", e)

if __name__ == "__main__":
    ip = get_local_ip()
    url = generate_qr_and_open(ip)
    start_flask_server()
    webbrowser.open(url)  # optional: open in desktop browser

    print("\n✅ Your SnapDrop server is running.")
    print("📌 Keep this window open while using SnapDrop.\n")
    input("🔒 Press Enter to exit (or close this window)...")
