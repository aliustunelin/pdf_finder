import requests



def pdf_indir(url, hedef_dosya):
    try:
        
        response = requests.get(url)
        hedef_dosya = "./dergiparkArchive/" + hedef_dosya + ".pdf"
        
        with open(hedef_dosya, 'wb') as dosya:
            dosya.write(response.content)
        
        return (f'{hedef_dosya[1:]} download success.')
    
    except Exception as hata:
        return (f'Error: {hata}')


