from src.dosya_islemleri import read_csv, write_json,write_text
from src.processing import stats,build_report
def main():
    read_doc="/Users/elifcanbakkal/Desktop/workspace/betik-diller/calculator/exercise/data/people.csv"
    write_doc="/Users/elifcanbakkal/Desktop/workspace/betik-diller/calculator/exercise/data/stats.json"
    write_txt="/Users/elifcanbakkal/Desktop/workspace/betik-diller/calculator/exercise/data/stats_txt.txt"

    #Oku
    rows=read_csv(read_doc)
    st=stats(rows)

    write_json(write_doc,st)
    write_text(write_txt,build_report(st))
    print("bitti")

if __name__=="__main__":
    main()