# AI Çizgi Film Denemesi (Pofi & Mimi)

Instagram'da gördüğün sistemin güvenli, abartısız hali: Claude ile hikaye + prompt, Wan2GP ile yerel video üretimi.

> Gelir garantisi yok. YouTube, tekrarlayan ve şablon içerikleri monetizasyona almayabilir. Bunu deneme projesi olarak gör.

## Klasör
- `episodes.json`: karakterler, stil ve 5 bölümün sahne promptları
- `scripts/gen_batch.py`: promptları toplu dosyalara çevirir
- `yayin/sablonlar.md`: başlık/açıklama/özgünlük notları
- `ciktilar/`: betik çalışınca oluşur

## Adımlar
1. **Wan2GP'yi kur:** GitHub'da `deepbeepmeep/Wan2GP` reposunun README'sindeki kurulum adımlarını izle (Python ortamı, CUDA, bağımlılıklar). Ekran kartı belleğine göre model seç; düşük VRAM için küçük/uyumlu modeller kullanılır.
2. **Promptları üret:** `python scripts/gen_batch.py`
3. **Videoları üret:** `ciktilar/bolum_1.txt` içeriğini Wan2GP'ye yapıştır, kuyruğa ekle. Gece çalıştırabilirsin.
4. **Birleştir:** 3 klibi (8 sn) bir kurgu programında ya da ücretsiz araçla art arda ekle. Müzik ve sesi ekle.
5. **Yayınla:** `yayin/sablonlar.md` şablonunu kullan, yapay zeka etiketini işaretle.

## Yeni bölüm
Claude'a şunu yazabilirsin: "episodes.json formatında 6. bölümü yaz, Pofi ve Mimi ile, mesajı: sabır."
