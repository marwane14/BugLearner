# main.py
from cve_search import fetch_cve_by_criteria
from summarizer import summarize_cve

def main():
    criteria = "date=2024-11-27&type=network&system=linux"  # Exemple de critères supplémentaires
    try:
        cve_data_list = fetch_cve_by_criteria(criteria)
        if cve_data_list:
            for cve_data in cve_data_list:
                summary, important_info = summarize_cve(cve_data['summary'])
                print(f"CVE ID: {cve_data['id']}")
                print("Résumé de la CVE :", summary)
                print("Informations importantes :", important_info)
                print("-" * 80)
        else:
            print("Aucun CVE trouvé.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()