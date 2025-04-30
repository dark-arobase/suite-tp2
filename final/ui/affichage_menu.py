def afficher_tout(forums):
    print("\n--- AFFICHAGE DU CONTENU ---")
    if not forums:
        print("Aucun forum disponible.")
        return

    for forum in forums:
        print(f"\n🧵 Forum : {forum.nom} - {forum.description}")
        if not forum.publications:
            print("  Aucune publication.")
        else:
            for pub in forum.publications:
                print(f"  📄 {pub.titre} (par {pub.auteur.nom})")
                print(f"     {pub.contenu}")
                for com in pub.commentaires:
                    print(f"    💬 {com.auteur.nom} : {com.contenu}")
