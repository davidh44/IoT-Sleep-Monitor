import http.client as http
import urllib

key = 'MYDJQA0ID1PVD4N9'


def upload_to_ts(val1=None, val2=None, val3=None):

    params = urllib.parse.urlencode({'field1': val1, 'field2': val2, 'field4': val3, 'key': key})
    headers = {"Content-typZZe": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.HTTPConnection("api.thingspeak.com:80")  

    try:  
        conn.request("POST", "/update", params, headers)  
        response = conn.getresponse()  
        data = response.read()  
        conn.close()  
    except Exception:  
        print("Connection failed")
    except KeyboardInterrupt:  
        print("\nExiting.....")
        exit()


