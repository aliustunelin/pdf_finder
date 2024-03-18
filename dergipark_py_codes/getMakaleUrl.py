import requests
from bs4 import BeautifulSoup


def makale_url_getiren(aranacak_link):
    return makale_detay_sayfası_url_topla(aranacak_link)



def makale_detay_sayfası_url_topla(aranacak_link):
    anahtarKelime = aranacak_link
    list_makale_urls = []
    # Web sayfasının URL'sini belirtin
    
    url = 'https://dergipark.org.tr/tr/search?q=' + anahtarKelime + '&section=articles'

    # Web sayfasını indirin
    response = requests.get(url)

    # Hata kontrolü
    if response.status_code == 200:
        # HTML içeriğini analiz etmek için BeautifulSoup kullanın
        print("Search Paper From DB...")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        card_divs = soup.find_all('h5', class_='card-title')
        if not card_divs:
            print("No Paper Found as a Search Result...")

        for card_div in card_divs:
            a_tag = card_div.find('a')
            if a_tag:
                href_value = a_tag.get('href')
                list_makale_urls.append(href_value)
                #print('H5 Başlık Linki:', href_value)
        print("Search Result " + str(len(list_makale_urls)) + " Paper Find.") 
        return list_makale_urls
    else:
        print('PDF Paper Download Error: ', response.status_code)




