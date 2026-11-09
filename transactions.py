import json

with open("transactions.csv","r") as file:
    lecteur = file.readlines()
    lignes_valides,lignes_invalides = [],[]
    transactions = {}
    suspects = []
    for l in lecteur:
        l = l.strip().split(";")
        if len(l) < 6:
            continue
        if l[4].isdigit():
            lignes_valides.append(l)
            if int(l[4]) > 500000 :
                suspects.append({
                    "id": l[0],
                    "date": l[1],
                    "expediteur": l[2],
                    "destinataire": l[3],
                    "montant": l[4],
                    "type": l[5]
                })
            if l[2] not in transactions :
                transactions [l[2]] = {"recu":0,"envoye":0}
            if l[3] not in transactions:
                transactions [l[3]] = {"recu":0,"envoye":0}
            if l[2] and l[5] == "transfert" :
                transactions [l[2]]["envoye"] += int(l[4])
            if l[3] and l[5] == "transfert" :
                print(l[5],l[5][:-1])
                transactions [l[3]]["recu"] += int(l[4])
        else:
            lignes_invalides.append(l)
            print(f"Cette ligne n'est pas valide {l}")
    rapport_final = {
        "statistiques_transactions": transactions,
        "transactions_suspectes": suspects
    }
    

    with open("rapport.json", "w", encoding="utf-8") as f:
        json.dump(rapport_final, f, ensure_ascii=False, indent=4)


        
