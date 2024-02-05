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
        print("İlgili Makale Dergipark Veri Tabanında Aranıyor...")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        card_divs = soup.find_all('h5', class_='card-title')
        if not card_divs:
            print("Arama Sonucu Herhangi Bir Makale Bulunamadı...")

        for card_div in card_divs:
            a_tag = card_div.find('a')
            if a_tag:
                href_value = a_tag.get('href')
                list_makale_urls.append(href_value)
                #print('H5 Başlık Linki:', href_value)
        print("Arama Sonucu " + str(len(list_makale_urls)) + " Makale Bulunmuştur.") 
        return list_makale_urls
    else:
        print('Makale Sayfa indirme hatası:', response.status_code)




