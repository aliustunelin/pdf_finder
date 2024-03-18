import requests
from bs4 import BeautifulSoup


def makale_pdf_getiren(detay_sayfa_linki):
    
    return makale_PDF_linki_ceken(detay_sayfa_linki)



def makale_PDF_linki_ceken(detay_sayfa_linki):
    list_makale_urls = []

    # Web sayfasının URL'sini belirtin
    url = detay_sayfa_linki

    response = requests.get(url)

    if response.status_code == 200:
        # HTML içeriğini analiz etmek için BeautifulSoup kullanın
        soup = BeautifulSoup(response.text, 'html.parser')
        card_divs = soup.find_all('li', class_='kt-nav__item')
        

        for card_div in card_divs:
            a_tag = card_div.find('a')
            if a_tag:
                href_value = a_tag.get('href')
                list_makale_urls.append(href_value)
                #print('H5 Başlık Linki:', href_value)
        return list_makale_urls[0]
    else:
        print('PDF Paper Download Error:', response.status_code)




