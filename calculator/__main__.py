"""
Basit sınıf içi alıştırma (tek dosya):
- Dekoratörler: timer, ensure_parent_dir
- CSV okuma, basit temizleme (yaş boşsa atla)
- JSON ve TXT rapor yazma
Çalıştırma: python exercise_simple.py
"""
from __future__ import annotations
import csv, json, time
from functools import wraps
from pathlib import Path
from statistics import mean

DATA = Path(__file__).resolve().parent  / "people.csv"
OUT_DIR = Path(__file__).resolve().parent / "out"

# --- Dekoratörler ---
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"[timer] {func.__name__}: {elapsed:.4f}s")
        return result
    return wrapper

def ensure_parent_dir(func):
    """İlk parametresi 'path' olan fonksiyonlar için klasörü otomatik oluşturur."""
    @wraps(func)
    def wrapper(path: Path, *args, **kwargs):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        return func(path, *args, **kwargs)
    return wrapper

# --- I/O yardımcıları ---
@timer
def read_csv(path: Path) -> list[dict]:
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

@ensure_parent_dir
@timer
def write_json(path: Path, obj) -> None:
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

@ensure_parent_dir
@timer
def write_text(path: Path, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")

# --- İş mantığı ---
def clean(rows: list[dict]) -> list[dict]:
    """
    age boş olan kayıtları eler; age'i int'e çevirir.
    """
    ok = []
    for r in rows:
        if not r.get("age"):
            continue
        try:
            age = int(r["age"])
        except ValueError:
            continue
        ok.append({"name": r.get("name","").strip(),
                   "age": age,
                   "city": r.get("city","").strip()})
    return ok

def stats(valid: list[dict]) -> dict:
    if not valid:
        return {"count": 0, "avg_age": None, "by_city": {}}
    ages = [r["age"] for r in valid]
    by_city = {}
    for r in valid:
        by_city[r["city"]] = by_city.get(r["city"], 0) + 1
    return {"count": len(valid), "avg_age": round(mean(ages),2), "by_city": by_city}

def build_report(st: dict) -> str:
    lines = []
    lines.append("# Basit Rapor")
    lines.append("")
    lines.append(f"- Geçerli kayıt sayısı: {st['count']}")
    lines.append(f"- Ortalama yaş: {st['avg_age']}")
    lines.append("")
    lines.append("## Şehir dağılımı")
    for c, n in sorted(st["by_city"].items()):
        lines.append(f"- {c}: {n}")
    lines.append("")
    return "\n".join(lines) + "\n"

# --- Uygulama ---
def main():
    rows = read_csv(DATA)
    valid = clean(rows)
    st = stats(valid)
    write_json(OUT_DIR / "people_clean.json", valid)
    write_json(OUT_DIR / "stats.json", st)
    report = build_report(st)
    write_text(OUT_DIR / "report.txt", report)
    print("Tamamlandı. Çıktılar 'out/' klasöründe.")

if __name__ == "__main__":
    main()
