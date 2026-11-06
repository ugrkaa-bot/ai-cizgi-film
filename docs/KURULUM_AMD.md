# Kurulum: AMD RX 6600 (8 GB) üzerinde Wan2GP

Hedef makine: ASUS RX 6600, 8 GB VRAM, AMD (RDNA 2), Windows.
Uzaktan kontrol: AnyDesk. Kayıt: bu GitHub reposu.

> Durum notu: Wan2GP'nin Windows'ta AMD desteği yeni. Pinokio duyurusuna göre
> dedicated RDNA 2 - RDNA 4 kartlar destekleniyor ve yalnızca RDNA 2 test edilmiş.
> 8 GB'ta hangi modelin/sürenin çalıştığı doğrulanmadı; deneyerek öğreneceğiz.

## 0. Ön kontrol (arkadaşın bilgisayarında)
- [ ] Sistem RAM'i: ______ GB (Görev Yöneticisi > Performance > Memory)
- [ ] Boş disk alanı: ______ GB (modeller büyük; kurulum ekranı gerçek boyutu gösterir)
- [ ] Güncel AMD Adrenalin sürücüsü kurulu
- [ ] Güç ayarı: uyku "Hiçbir zaman"

## 1. AnyDesk
1. Arkadaşının PC'sinde AnyDesk kur, "gözetimsiz erişim" şifresi belirle (güçlü bir şifre).
2. Numara ve şifreyi kimseyle paylaşma.
3. Mümkünse ayrı bir Windows kullanıcısı aç, onunla bağlan.

## 2. Pinokio + Wan2GP
1. pinokio.co > Windows sürümünü indir ve kur.
2. Pinokio içinde Wan2GP'yi bul, AMD sürümünü kur.
3. İlk kurulum çok dosya indirir; bitmesini bekle.
4. Kart tanınmazsa: `.\pinokio\logs\shell\system.json` içindeki GPU adını bul,
   Pinokio Discord > pinokio-support kanalına bildir.

## 3. İlk test
1. `ciktilar/bolum_1.txt` içindeki ilk satırı Wan2GP'ye yapıştır.
2. En küçük/en hafif model ve kısa süre ile dene.
3. Sonucu `kayit/test_notlari.md` dosyasına yaz (şablon aşağıda).

## 4. Kayıt (GitHub'a ne gider)
- GİDER: promptlar, ayarlar, notlar, süre/hata kayıtları (küçük metin dosyaları).
- GİTMEZ: video dosyaları (GitHub tek dosya limiti 100 MB). Videolar Drive/diskte tutulur.
- Token/şifre asla repoya yazılmaz.

### test_notlari.md şablonu
```
Tarih:
Model:
Süre / çözünürlük:
Üretim süresi:
VRAM hatası var mı:
Kalite notu (1-5):
Sonraki adım:
```

## 5. Karar noktası (2-3 hafta sonra)
- 5 bölüm kaliteli üretildi mi?
- İlk bölümler izleniyor mu?
- Evetse devam, hayırsa bulut GPU ya da hizmet satışı yoluna dön.
