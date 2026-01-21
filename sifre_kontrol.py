import re
import hashlib 


def sifre_gucu_olcer(sifre):
    puan = 0
    notlar = []

    # Kriter 1: Uzunluk
    if len(sifre) >= 8:
        puan += 1
    else:
        notlar.append("- Şifre en az 8 karakter olmalı.")

    # Kriter 2: Sayı kontrolü
    if re.search(r"\d", sifre):
        puan += 1
    else:
        notlar.append("- En az bir rakam içermeli.")

    # Kriter 3: Büyük harf kontrolü
    if re.search(r"[A-Z]", sifre):
        puan += 1
    else:
        notlar.append("- En az bir büyük harf içermeli.")

    # Kriter 4: Özel karakter kontrolü
    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", sifre):
        puan += 1
    else:
        notlar.append("- En az bir özel karakter içermeli.")

    return puan, notlar
def sifre_hashle(sifre):
    # Şifreyi SHA-256 algoritması ile geri dönülmez bir özete çevirir
    sha256_objesi = hashlib.sha256(sifre.encode())
    return sha256_objesi.hexdigest()

print("--- Güvenli Şifre Sistemi ---")
test_sifresi = input("Kontrol etmek istediğiniz şifreyi girin: ")
skor, tavsiyeler = sifre_gucu_olcer(test_sifresi)

print(f"\nŞifre Skoru: {skor}/4")
if skor == 4:
    print("Sonuç: Güçlü Şifre! ✅")
    secure_hash = sifre_hashle(test_sifresi)
    print(f"Veritabanına Kaydesilecek Güvenli Hali (SHA-256): /n{secure_hash}")
    
else:
    print("Geliştirme Tavsiyeleri:")
    for t in tavsiyeler:
        print(t)