import ssl
import socket

def get_certificates(hostname, port=443):
    context = ssl.create_default_context()

    # Retrieve SSL certificate
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            ssl_cert = ssock.getpeercert()
            

    # Retrieve TLS certificate
    with socket.create_connection((hostname, port)) as sock:
        with ssl.SSLContext(ssl.PROTOCOL_TLS).wrap_socket(sock, server_hostname=hostname) as ssock:
            tls_cert = ssock.getpeercert()
            

    return ssl_cert, tls_cert

def print_certificate_info(cert, cert_type):
    print(f"{cert_type} Certificate Information:")
    print(f"Subject: {cert.get('subject', 'N/A')}")
    print(f"Issuer: {cert.get('issuer', 'N/A')}")
    print(f"Expiry Date: {cert.get('notAfter', 'N/A')}")
    print(f"Serial Number: {cert.get('serialNumber', 'N/A')}")
    print(f"Signature Algorithm: {cert.get('signatureAlgorithm', 'N/A')}")
    print(f"Public Key Algorithm: {cert.get('subjectPublicKeyAlgorithm', 'N/A')}")
    print(f"Public Key Size: {cert.get('subjectPublicKeySize', 'N/A')} bits")

if __name__ == "__main__":
    url = "www.google.com"  # Replace with your desired URL
    port = 443  # Default HTTPS port

    try:
        ssl_cert, tls_cert = get_certificates(url, port)
        
        print_certificate_info(ssl_cert, "SSL")
        print("\n" + "=" * 40 + "\n")  # Separator
        #print_certificate_info(tls_cert, "TLS")
    except ssl.SSLError as e:
        print(f"Error retrieving certificates: {e}")
    except socket.error as e:
        print(f"Error connecting to the server: {e}")
