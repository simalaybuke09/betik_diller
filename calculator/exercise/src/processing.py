
def stats (rows: list[dict]) ->list[dict]:
    if not rows:
        return {"count":0, "avg_age":0,"by_city": {}}
    ages=[int(r["age"]) for r in rows if r["age"] ] 
    by_city={}
    for r in rows:
        by_city[r["city"]]=by_city.get(r["city"],0) +1
    return {"count": len(rows), "avg_age":sum(ages)/len(rows), "by_city": by_city}

def build_report(st:dict)->str:
    lines=[]
    lines.append("Rapor")
    lines.append("")
    lines.append("Geçerli kayıt sayısı:", st["count"])
    lines.append("ortalama yaş:", st["avg_age"])
    lines.append("Şehir dağılımı:")
    for c,n in st["by_city"].items():
        lines.append(c,":",n)
    return  "\n".join(lines) +"\n"
