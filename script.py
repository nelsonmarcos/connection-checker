import time
import http.client as httplib

#domains = ['https://www.globo.com', 'https://www.google.com.br', 'https://www.facebook.com']
domains = ['localhost:8000']
toleration = 0

def is_internet_down(domains, toleration):
    counter = 0
    status = False
    for domain in domains:
        conn = httplib.HTTPConnection(domain, timeout=2)
        try:
            conn.request("HEAD", "/")
            conn.close()
        except:
            conn.close()
            counter +=1

    if counter > toleration:
        status = True

    return status

while True:
    if is_internet_down(domains, toleration):
        print('\nInternet is down!')
        start_time = time.time()
        while is_internet_down(domains, toleration):
            time.sleep(5)
        elapsed_time = time.time() - start_time
        print ('The internet was down for {} seconds'.format(elapsed_time))
    else:
        print('.', end='', flush=True)
        time.sleep(1)


