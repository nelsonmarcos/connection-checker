import datetime, time
import http.client as httplib

#Set the domains lists
#domains = ['www.google.com', 'www.facebook.com', 'www.amazon.com']
#domains = ['127.0.0.1:8000']

toleration = 0


def is_internet_down(domains_list, toleration_limit):
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
        time_stamp = time.strftime("%d-%m-%Y %H:%M:%S")
        print('\n{} - Internet is down!'.format(time_stamp))
        start_time = time.time()
        while is_internet_down(domains, toleration):
            time.sleep(5)
        elapsed_time = time.time() - start_time
        time_stamp = time.strftime("%d-%m-%Y %H:%M:%S")
        print ('{} - The internet was down for {} seconds'.format(time_stamp, int(elapsed_time)))
    else:
        print('.', end='', flush=True)
        time.sleep(1)
