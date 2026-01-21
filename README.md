# 🛡️ Password Strength Checker (Python)

Bu proje, kullanıcıların oluşturduğu şifrelerin güvenliğini siber güvenlik prensiplerine göre analiz eden basit ama etkili bir Python aracıdır.

## 🚀 Özellikler
- **Uzunluk Kontrolü:** Şifrenin en az 8 karakter olup olmadığını denetler.
- **Karakter Çeşitliliği:** Büyük harf, rakam ve özel karakter kullanımını kontrol eder.
- **Geri Bildirim:** Zayıf şifreler için kullanıcıya somut iyileştirme önerileri sunar.
- **Skor Sistemi:** Şifreyi 4 üzerinden puanlayarak güvenlik seviyesini görselleştirir.

## 🛠️ Teknik Detaylar
- **Dil:** Python
- **Kütüphaneler:** `re` (Regular Expressions) kütüphanesi kullanılarak karakter desenleri analiz edilmiştir.
- ---
### 🛡️ Siber Güvenlik İpucu: Neden Hashing?
Bir sistem yöneticisi veya yazılımcı olarak kullanıcı şifrelerini asla "olduğu gibi" saklamamalısınız. 
Bu projede kullandığımız **SHA-256**, tek yönlü bir özetleme (hashing) algoritmasıdır. 

**Neden Önemli?**
- Veritabanınız ele geçirilse bile, saldırganlar sadece karmaşık özetleri görür; gerçek şifreleri göremez.
- Şifreleme (Encryption) geri döndürülebilirken, Hashing geri döndürülemez. Bu, kullanıcı gizliliği için altın kuraldır.
---

## 💻 Nasıl Çalıştırılır?
1. Depoyu klonlayın.
2. Terminale `python sifre_kontrol.py` yazarak uygulamayı başlatın.
