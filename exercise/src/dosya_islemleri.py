from pathlib import Path
from dekorator import timer
import csv,json


@timer
def read_csv(path):
    with Path(path).open("r", encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f)) # her satırı bir listeye atar


@timer
def write_json(path, obj):
    with Path(path).open("w",encoding="utf-8") as f:
        # Türkçe karakter sorunu
        json.dump(obj, f, indent=4, ensure_ascii=False) 


@timer
def write_text(path,text):
    Path(path).write_text(text,encoding="utf-8")