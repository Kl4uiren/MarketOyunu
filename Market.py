import time
market_listesi = ["Patates","Elma","Muz"]
alınacaklar_listesi = ["Süt","Kiraz","Ceviz"]

print("Marketten Sana Gereken Eşyaları Alman Gerekiyor Yoksa Kaybedersin Devam Etmek İçin Herhangi Bir Tuşa Basınız")
input()
print("Elinde Olan Eşyalar",market_listesi)
print(alınacaklar_listesi,"Bunları Satın Alman Gerek")
time.sleep(1)
print("1")
time.sleep(1)
print("2")
time.sleep(1)
print("3")
time.sleep(1)
print("Başlamak İçin Herhangi Bir Tuşa Basınız...")
input()
soru1 = input("Kiraz mı Alacaksın Oyuncak Araba mı?")

if soru1 == "Kiraz":
    market_listesi.append("Kiraz")
    print("Elindekiler",market_listesi)
    time.sleep(1)
    soru2 = input("Mango mu Alacaksın Ceviz mi?")
    if soru2 == "Ceviz":
        market_listesi.append("Ceviz")
        print("Elindekiler",market_listesi)
        time.sleep(1)
        soru3 = input("Süt mü Alacaksın Pirinç mi?")
        if soru3 == "Süt":
            market_listesi.append("Süt")
            print("Elindekiler",market_listesi)
            time.sleep(1)
            print("Tebrikler Kazandın")
        else:
            print("Kaybettin...")

    else:
        print("Kaybettin...")

else:
    print("Kaybettin...")


