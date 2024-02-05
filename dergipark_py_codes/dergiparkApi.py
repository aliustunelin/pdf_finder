import dergipark_py_codes.getMakaleUrl as getMakaleUrl
import dergipark_py_codes.getMakalePDF as getMakalePDF 
import dergipark_py_codes.downloadPDF as downloadPDF


#1 dergiparkda anahtar kelimeyi  search yap
#2 makaleleri çıkan listeden al(burada makalellerin detay sayfalarını alırsın)
#3 makale detay sayfalarına git ve indirme bğlaantılarından makaleleri çek
#4 pdf bağlantısındaki pdfi dosyaya kaydet


# aranacak anahtar kelimeyi dergiparkta arayan ve makale detay sayfasını getire
liste_url_makaleler_detay_sayfasi = []







def runProject():
    aranacak_link = input("Lütfen Aramak İstediğiniz Anaktar Kelimeyi Giriniz: ")


    liste_url_makaleler_detay_sayfasi = getMakaleUrl.makale_url_getiren(aranacak_link)


    indis = 0
    for i in(liste_url_makaleler_detay_sayfasi):
        indis = indis + 1
        makale_detay_sayfa_linki = i
        makale_pdf_linki = getMakalePDF.makale_pdf_getiren(makale_detay_sayfa_linki)
        makale_pdf_linki = "https://dergipark.org.tr" + makale_pdf_linki
        print("-------------------")
        print("PDF Çözümlemesi Yapılıyor...")
        print("Tespit Edilen Makale Link:"+makale_pdf_linki)

        pdf_adi = aranacak_link + str(indis)
        pdf_indirici = downloadPDF.pdf_indir(makale_pdf_linki, pdf_adi )
        print(pdf_indirici)

    sonuc = input("\nMakale Arama Faaliyeti Başarıyla Tamamlanmıştır.")
    

