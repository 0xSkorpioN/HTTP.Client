import http.client

print("** This program returns a list of methods if OPTIONS is enabled **")

host = input("Enter the Host/IP: ")
port = input("Enter the Port (Default:80): ")
url = input("Enter the Url: ")

if port == "":
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('GET', url)
    response = connection.getresponse()
    print("Server Response: ", response.status)
    connection.close()

except ConnectionRefusedError:
    print("Connection Failed!")
