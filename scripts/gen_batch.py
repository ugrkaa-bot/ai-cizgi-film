#!/usr/bin/env python3
"""episodes.json -> ciktilar/ klasorune toplu prompt dosyalari uretir.

Kullanim:  python scripts/gen_batch.py
Cikti:
  ciktilar/bolum_N.txt      bir bolumun sahneleri (her satir = bir video)
  ciktilar/tum_bolumler.txt hepsi tek dosyada
Wan2GP prompt kutusuna yapistirabilirsin; satir basina bir uretim yapilir
(guncel davranisi Wan2GP README'sinden dogrula).
"""
import json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "episodes.json").read_text(encoding="utf-8"))
out = root / "ciktilar"
out.mkdir(exist_ok=True)

style = data["style"]
all_lines = []
for ep in data["episodes"]:
    lines = [f"{scene}, {style}" for scene in ep["scenes"]]
    (out / f"bolum_{ep['no']}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    all_lines += [f"# Bolum {ep['no']} - {ep['title']}"] + lines + [""]

(out / "tum_bolumler.txt").write_text("\n".join(all_lines), encoding="utf-8")
print(f"{len(data['episodes'])} bolum yazildi -> {out}")
