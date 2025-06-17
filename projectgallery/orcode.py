import socket
import qrcode

# Automatically get your current local IP address
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # This doesn't need to be reachable, just forces system to get the IP
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

# Generate the QR code with the detected IP
local_ip = get_local_ip()
url = f"http://{local_ip}:5000"
qr = qrcode.make(url)
qr.save("link_qr.png")

print(f"✅ QR code for {url} saved as 'link_qr.png'")

