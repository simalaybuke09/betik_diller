from dosya_islemleri import read_csv, write_json,write_text
from processing import stats_and_clean, build_report

def main():
    
    read_doc="C:\\Users\\oyunc\\OneDrive\\Belgeler\\betik_diller\\exercise\\data\\people.csv"
    write_doc_stats="C:\\Users\\oyunc\\OneDrive\\Belgeler\\betik_diller\\exercise\\data\\stats.json"
    write_doc_cleaned="C:\\Users\\oyunc\\OneDrive\\Belgeler\\betik_diller\\exercise\\data\\cleaned_data.json" # temizlenmiş verilerin olduğu dosya yolu
    write_txt="C:\\Users\\oyunc\\OneDrive\\Belgeler\\betik_diller\\exercise\\data\\stats_txt.txt"

    
    rows = read_csv(read_doc)
    
    try:
        st = stats_and_clean(rows) 
    except ValueError as e:
        print(f"Hata: {e}")
        return 


    
    # temizlenmiş kayıtları JSON dosyasına yazma
    write_json(write_doc_cleaned, st["cleaned_rows"]) 
    

    # cleaned_rows alanını istatistik JSON'una yazmamak için bir kopyasını alma ve sonrasında kaydetme
    stats_only = {k: v for k, v in st.items() if k != "cleaned_rows"}
    write_json(write_doc_stats, stats_only)
    
    # raporu .txt dosyasına yaz
    write_text(write_txt, build_report(stats_only))
    
    print("bitti")

if __name__=="__main__":
    main()