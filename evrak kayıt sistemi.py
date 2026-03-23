# Evrakları tutmak için boş bir liste oluşturuluyorum
evraklar  []  # Evraklar burada saklanıyor

# Yeni evrak eklemek için fonksiyonumuz
def evrak_ekle():
    print("\n--- Yeni Evrak Ekle ---")
    # Kullanıcıdan evrak bilgilerini alıyorum
    evrak_no = input("Evrak No: ")
    konu = input("Konu: ")
    gonderici = input("Gönderici: ")
    tarih = input("Tarih (GG.AA.YYYY): ")

    # Bilgiler bir sözlük (dict) içinde depolanıyor
    evrak = {
        "evrak_no": evrak_no,
        "konu": konu,
        "gonderici": gonderici,
        "tarih": tarih
    }

    #evrak sözlüğünü listeye ekliyoruz
    evraklarappend(evrak)
    print(" Evrak başarıyla eklendi!")

# Tüm evrakları listeleyen fonksiyonu yazıyoruz
def evraklari_listele():
    print("\n--- Tüm Evraklar ---")
    # Eğer listede evrak yoksa kullanıcıya bilgi veriliyor
    if not evraklar:
        print(" Kayıtlı evrak yok.")
    else:
        # Listedeki tüm evraklar sırayla yazdırılıyor
        for i, evrak in enumerate(evraklar, 1):
            print(f"{i}. No: {evrak['evrak_no']}, Konu: {evrak['konu']}, Gönderici: {evrak['gonderici']}, Tarih: {evrak['tarih']}")

# Evrak numarasına göre arama yapan fonksiyon
def evrak_ara():
    print("\n--- Evrak Ara ---")
    aranacak_no = input("Aranacak Evrak No: ")  # Aranacak evrak numarası isteniyor
    bulundu = False  # Başlangıçta evrak bulunmadı varsayılıyor

    # Listedeki her evrağa bakılıyor
    for evrak in evraklar:
        if evrak["evrak_no"] == aranacak_no:
            # Aranan evrak bulunursa yazdırıyor
            print(f"Bulundu: {evrak}")
            bulundu = True
            break

    # Eğer evrak bulunmazsa kullanıcıya bilgi veriyor
    if not bulundu:
        print("Evrak bulunamadı.")

# Evrak silme fonksiyonu
def evrak_sil():
    print("\n--- Evrak Sil ---")
    silinecek_no = input("Silinecek Evrak No: ")  # Silinmek istenen evrak noyu alıyor
    for evrak in evraklar:
        if evrak["evrak_no"] == silinecek_no:
            # Eğer evrak bulunursa listeden siliyor
            evraklar.remove(evrak)
            print(" Evrak başarıyla silindi.")
            return
    # Evrak bulunamazsa uyarı veriyor
    print(" Evrak bulunamadı.")

# Ana menüyü oluşturan ve kullanıcıdan seçim alıp yönlendirme yapan fonksiyon
def menu():
    while True:  # Sürekli dönen bir döngü
        print("\n Evrak Takip Sistemi")
        print("1 - Evrak Ekle")
        print("2 - Evrakları Listele")
        print("3 - Evrak Ara")
        print("4 - Evrak Sil")
        print("5 - Çıkış")

        secim = input("Seçiminiz (1-5): ")  # Kullanıcıdan seçim alıyor

        # Girilen seçime göre fonksiyonu veriyoruz
        if secim == "1":
            evrak_ekle()
        elif secim == "2":
            evraklari_listele()
        elif secim == "3":
            evrak_ara()
        elif secim == "4":
            evrak_sil()
        elif secim == "5":
            print("Çıkılıyor...")
            break  # Döngüden çıkarak programı bitiriyor
        else:
            # Geçersiz bir seçim yapılırsa uyarı veriyor
            print(" Geçersiz seçim. Tekrar deneyin.")

# Programı başlatan ana fonksiyon çağrısı
menu()
11