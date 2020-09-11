kulad=input("Kullanıcı Adınızı Giriniz:")
sifre=input("Şifrenizi Giriniz:")
while sifre=="123" and kulad=="admin":
    try:
        islem=int(input("Lütfen işlem seçiniz(1=Çarpma 2=Bölme 3=Toplama 4=Çıkarma 5=Programdan Çıkış):"))
    except (ValueError):
        print("Lütfen Sadece Sayı Girin!")
        break



    if islem==(1):
        print("Çarpma İşlemi Seçildi.")
        try:
           carpma1=int(input("Çarpılacak 2 sayıdan ilkini giriniz:"))
           carpma2=int(input("Çarpılacak 2 sayıdan ikincisini giriniz:"))
        except ValueError:
           print("Lütfen Sadece Tam Sayı Girin!")
        else:
           print(carpma1*carpma2)
    elif islem==(2):
        try:
            bolme1=int(input("Bölünecek 2 sayıdan ilkini giriniz:"))
            bolme2=int(input("Bölünecek 2 sayıdan ikincisini giriniz:"))
        except ValueError:
            print("Lütfen Sadece Tam Sayı Girin!")
        else:
            try:
                print(bolme1/bolme2)
            except ZeroDivisionError:
                print("Bu iki sayı Birbirine bölünemez!")
    elif islem==(3):
        try:
            toplama1=int(input("Toplanacak 2 sayıdan ilkini giriniz:"))
            toplama2=int(input("Toplanacak 2 sayıdan ikincisini giriniz:"))
        except ValueError:
            print("Lütfen Sadece Tam Sayı Girin!")

        else:
            print(toplama1+toplama2)
    elif islem==(4):
        try:
            cikarma1=int(input("Çıkarılacak 2 sayıdan ilkini giriniz:"))
            cikarma2=int(input("Çıkarılacak 2 sayıdan ikincisini giriniz:"))
        except ValueError:
            print("Lütfen Sadece Tam Sayı Girin!")
        else:
            print(cikarma1-cikarma2)
    elif islem==(5):
        print("Programdan Çıkış Yapılıyor.")
        break

    else:
        print("Lütfen Sadece Verilen Sayılardan Seçim Yapınız!")
else:
    print("Kullanıcı adı/Şifre Hatalı Programdan Çıkış Yapılıyor.")










