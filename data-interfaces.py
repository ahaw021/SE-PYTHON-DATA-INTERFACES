import json
import urllib3
import socket
import ssl

# DISABLE ssl warnings. We should try to make these work with a Mozilla Cert Bundle
# Set Timeout to 2 seconds so we don't slow down the script for non responsive servers

urllib3.disable_warnings()
HTTP_CLIENT = urllib3.PoolManager(timeout=10.0)

def write_file(path,name,data):
    file = open(path+"/"+name,'w')
    file.write(data)
    file.close

def write_file_from_json_dict(path,name,data):
    file = open(path+"/"+name,'w')
    file.write(json.dumps(data))
    file.close

def append_file(path,name,data):
    file = open(path+"/"+name,'a')
    file.write(data)
    file.close

def open_file(path,name):
    file = open(path+"/"+name,'r')
    return file.read()

def to_json(json_string):
    json_dict = json.loads(json_string)
    return json_dict

def http_get(url):
    https_response = HTTP_CLIENT.request('GET',url)
    return response

def http_post(url,body):
    https_response = HTTP_CLIENT.request('POST',url)
    return response

def http_get_custom_headers(url,headers):
    https_response = HTTP_CLIENT.request('GET',url)
    return response

def http_post_custom_headers(url,body,headers):
    https_response = HTTP_CLIENT.request('POST',url)
    return response

def socket_create_connect(host,port,TRANSPORT,IP_VERSION):

    if(IP_VERSION == 4 and TRANSPORT == "TCP"):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    elif(IP_VERSION == 4 and TRANSPORT == "UDP"):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    elif(IP_VERSION == 6 and TRANSPORT == "TCP"):
        client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM,0,0)

    elif(IP_VERSION == 6 and TRANSPORT == "UDP"):
        client = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM,0,0)

    else:
        print("The Socket You asked for is not in the Right Format. Acceptable Options are: 4 and 6 for IP Version and TCP or UDP for Transport")

        client.connect((HOST, PORT))
        banner = client.recv(1024)
        return client, banner

def socket_tcp_raw_send_data(client,data):
    client.send(data)
    response = client.recv(1024)
    return response

def socket_tcp_raw_close_completely(client):
    client.close()
