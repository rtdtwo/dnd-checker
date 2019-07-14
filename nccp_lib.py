import requests
from bs4 import BeautifulSoup


# Defines APIs that access NCCP TRAI data

def get_dnd_status(phone):
    url = "http://www.nccptrai.gov.in/nccpregistry/saveSearchSub.misc"
    payload = "phoneno={}".format(phone)
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'Accept-Language': "en-US,en;q=0.5",
        'Content-Type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'Referer': "http://www.nccptrai.gov.in/nccpregistry/saveSearchSub.misc",
        'Upgrade-Insecure-Requests': "1",
        'cache-control': "no-cache",
    }
    response = requests.post(url, data=payload, headers=headers)

    result = response.text
    status_code = response.status_code

    if status_code == 200:
        # Successfully retrieved data
        soup = BeautifulSoup(result, 'html.parser')
        form = soup.find('form', {'name': "registrationForm"})
        tds = form.findAll('td')
        phone = tds[4].text
        dnd_status = tds[7].text

        result = {'phone': phone, 'dnd_status': dnd_status}

    return status_code, result
