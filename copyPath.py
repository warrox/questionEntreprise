import json
f = open("animaux_leschats_confirme.json")
json_data = f.read()
f.close()
file_unserialized = json.loads(json_data)
class JsonReader:
    def __init__(self, file):
        self.json = file

    def read_json(self, file):

        print(file[0])
        print(file[1])
        print(file[2])
        print(file[3])

print(file_unserialized["questions"][0]["titre"])
print(len(file_unserialized["questions"]))



"""
    def __init__(self, titre_questionnaire, categorie, difficulty, sum_question, question_number, titre, choix,
                 bonne_reponse):
        self.question_number = question_number
        self.sum_question = sum_question
        self.titre_questionnaire = titre_questionnaire
        self.categorie = categorie
        self.difficulty = difficulty
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse"""