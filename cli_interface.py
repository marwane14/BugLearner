# cli_interface.py
from cve_search import fetch_cve_by_criteria
from summarizer import summarize_cve

def interactive_session():
    """Start an interactive CLI session."""
    print("Bienvenue dans BugLearning !")
    print("Tapez 'exit' pour quitter.")
    while True:
        criteria = input("\nEntrez les critères de recherche (e.g., date=2024-11-27&type=network): ")
        if criteria.lower() == "exit":
            print("Merci d'avoir utilisé BugLearning. À bientôt !")
            break
        try:
            cve_data_list = fetch_cve_by_criteria(criteria)
            if cve_data_list:
                for cve in cve_data_list[:5]:  # Limitez à 5 résultats
                    summary, important_info = summarize_cve(cve['summary'])
                    print("\nCVE ID:", cve['id'])
                    print("Résumé pédagogique:", summary)
                    print("Informations importantes:", important_info)
                    print("-" * 80)
            else:
                print("Aucun CVE trouvé.")
        except Exception as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    interactive_session()