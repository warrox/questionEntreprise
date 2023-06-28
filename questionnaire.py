import json
import os.path


class Question:
    def __init__(self,data):
        self.data = data
    def FromData(self,data):
        # ....
        self.data = Question("Le questionnaire porte sur la catégorie " + data["categorie"] + "titre du questionnaire " +
                     data["titre"] + "la difficulté est " + data["difficulte"] + "Nombre de questions " +
                     str(len(data["questions"]))
                     + data["questions"][0]["titre"]
                     )
        return self.data

    def poser(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i + 1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int - 1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")

        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)


class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score

w = os.listdir("/Users/warren/PycharmProjects/questionEntreprise")
for e in w:
    if e.endswith(".json"):
        f = open(e)
        json_data = f.read()
        f.close()
        file_unserialized = json.loads(json_data)
        g = Question(file_unserialized)
        g.FromData(file_unserialized)


# run the script > FromData seems to work.

"""
#chemin des json fonctionelle
Question("Le questionnaire porte sur la catégorie " + json_file["categorie"] + "titre du questionnaire " +
         json_file["titre"] + "la difficulté est " + json_file["difficulte"] + "Nombre de questions " + len(
    json_file["questions"])
         + json_file["questions"][0]["titre"]
         )


Doit afficher le titre du questionnaire 
la catégorie + la difficulté
le nombre total de questions
le numerio de la question (ex: auestions 1/20)
Qualité du code 
commit sur git
commenter le code. 
ANALYSER LA STRUCTURE DES JSONS POUR LES MANIPULER CORRECTEMENT
"""
