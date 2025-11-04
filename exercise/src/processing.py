from dekorator import required_column

# zorunlu kolonları tanımlama
REQUIRED_COLUMNS = {"name", "age", "city"}


def clean_data(rows: list[dict]) -> list[dict]:

    cleaned_rows = []
    for r in rows:
        # name ve city de boşlukları temizleme
        name = r.get("name", "").strip()
        city = r.get("city", "").strip()
        age_str = r.get("age", "").strip()

        # age de boş veya sayısal değilse atlar listeye almaz
        try:
            age = int(age_str)
        except ValueError:
            continue
        
        # Temizlenmiş ve dönüştürülmüş kaydı eklemek için
        cleaned_rows.append({
            "name": name,
            "age": age, 
            "city": city
        })
    return cleaned_rows


@required_column(REQUIRED_COLUMNS) # Şema kontrolü
def stats_and_clean(rows: list[dict]) -> dict:
    # Kayıtları temizleme
    cleaned_rows = clean_data(rows)

    if not cleaned_rows:
        return {"count": 0, "avg_age": 0, "by_city": {}, "cleaned_rows": []}

    # İstatistik üretme
    ages = [r["age"] for r in cleaned_rows]
    by_city = {}
    for r in cleaned_rows:
        # Şehirleri sayma
        by_city[r["city"]] = by_city.get(r["city"], 0) + 1
        
    avg_age = sum(ages) / len(ages) if ages else 0 # Yaş listesi boşsa 0 döndürür

    return {
        "count": len(cleaned_rows), 
        "avg_age": avg_age, 
        "by_city": by_city,
        "cleaned_rows": cleaned_rows # temizlenmiş satırları jsona yazma
    }

def build_report(st:dict)->str:
    lines=[]
    lines.append("Rapor")
    lines.append("-" * 30) 
    
    # String birleştirme hatası
    lines.append(f"Geçerli kayıt sayısı: {st['count']}")
    lines.append(f"Ortalama yaş: {st['avg_age']:.2f}") # Ortalama yaş formatı 
    lines.append("Şehir dağılımı:")
    
    for c, n in st["by_city"].items():
        # String birleştirme hatası 
        lines.append(f"- {c}: {n}")
        
    return  "\n".join(lines) + "\n"