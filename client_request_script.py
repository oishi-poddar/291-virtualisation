import logging
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np


THREAD_POOL = 16

# This is how to create a reusable connection pool with python requests.
session = requests.Session()
session.mount(
    'https://',
    requests.adapters.HTTPAdapter(pool_maxsize=THREAD_POOL,
                                  max_retries=3,
                                  pool_block=True)
)


def get(url):
    response = session.get(url)

    logging.info("request was completed in %s seconds [%s]", response.elapsed.total_seconds(), response.url)

    if response.status_code != 200:
        logging.error("request failed, error code %s [%s]", response.status_code, response.url)
    if 500 <= response.status_code < 600:
        # server is overloaded? give it a break
        time.sleep(5)
    # print(len(response_times))
    return response,response.elapsed.total_seconds()

  # send requests in parallel
def download(urls, response_times):
    with ThreadPoolExecutor(max_workers=THREAD_POOL) as executor:
        # wrap in a list() to wait for all requests to complete
        for response,response_time in list(executor.map(get, urls)):
            response_times.append(response.elapsed.total_seconds())
            if response.status_code == 200:
                print("Application run time", response.content)
        print("len response time",len(response_times))
        print("avg response time", )
        return response_times


def main():
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    print("starting req")
    avg_response_time_across_i_requests_j_times=[]
    urls_list=[]
    cdf_freq = [5,10,100,1000]
    request_url = "http://34.212.175.253/predict"
    
    # To append the request URL for cdf_freq number of times
    for f in range(len(cdf_freq)):
        url=[]
        for freq in range(cdf_freq[f]):
            url.append(request_url)
        urls_list.append(url)
        
    
    for urls in urls_list:
        # to average out response times across requests 5 times
        for i in range(5):
            response_times = []
            response_times= download(urls, response_times)
            avg_5_resonse_times = np.mean(response_times)
            avg_response_time_across_i_requests_j_times.append(avg_5_resonse_times)
            print("request done")
        print("Final_avg_request_across_5_requests_",len(urls),"_times", np.mean(avg_response_time_across_i_requests_j_times))

if __name__ == "__main__":
    main()
