import requests
from bs4 import BeautifulSoup

class Scrapper:

  def get_dictionary(self):

    URL = 'https://monitordolarvenezuela.com/inicio-amp'
    response = requests.get(URL, timeout=30)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.findAll("div", class_="col-12 col-sm-4 col-md-2 col-lg-2 boxes")
    rates = []
    hours = []
    for p in data:
      rates.append(p.find_all('p'))
    for small in data:
      hours.append(small.find_all('small'))

    BVC_TIME = str(hours[0])
    PARALL_TIME = str(hours[2])
    BVC = str(rates[0])
    PARALL = str(rates[2])
    BVC_DATE = (BVC_TIME[66:-24], BVC_TIME[92:-9])
    PARALL_DATE = (PARALL_TIME[66:-24], PARALL_TIME[92:-9])

    dictionary = {
      'BVC': round(float(BVC[51:-5].replace(',', '.')), 2),
      'PARALELO': float(PARALL[53:-5].replace(',', '.')),
      'BVC_TIMER': BVC_DATE,
      'PARALL_TIMER': PARALL_DATE
    }
    return dictionary
