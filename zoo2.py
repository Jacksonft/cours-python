class animaux:

	def__init__(self,name,nourriture):
	
		self.name = name
		self.nourriture = nourriture
		
	def__str__(self):
		return "Cet animal est un" + self.name
	

class mammifère(animaux):

  	def__init__(self,name,nb_pattes,regime_alimentaire,domestique):
	
		self.name = name
		self.nombres_de_pattes = nb_pattes 
		self.regime_alimentaire = regime_alimentaire
		self.domestique = domestique		
	
	def__str__(self):

		return "ce mammifère a" + str(self.nb_pattes) + "pattes, son regime alimentaire est de" + str(self.regime_alimentaire) + "est-ce un animal domestique ?" +str(self.domestique) + "et est un(e)" + self.name


class animal_marin(animaux):

	def__init__(self,name,régime_alimentaire,domestique):
	
		self.name = name
		self.regime_alimentaire = regime_alimentaire
		self.domestique = domestique

	def__str__(self):

		return "Cet animal marin a" + str(self.regime_alimentaire) + " son regime alimentaire est de " +str(self.regime_alimentaire) + "est-ce un animal domestique ?" +str(self.domestique) + "et est un(e)" + self.name


if__name__=="__main__":

	animal_marin_1 = animal_marin("pieuvre")
	animal_marin_1.nourriture = 200g
	animal_marin_1.domestique = non
	
	mammifère_1 = mammifère ("humain")
	mammifère_1.nourriture = 600g
	mammifère_1.domestique = non
	mammifère_1.nb_pattes = 2

	mammifère_2 = mammifère ("lion")
	mammifère_2.nourriture = 3kg 
	mammifère_2.domestique = non
	mammifère_2.nb_pattes = 4

	mammifère_3 = mammifère ("lapin")
	mammifère_3.nourriture = 100g
	mammifère_3.domestique = oui
	mammifère_3.nb_pattes = 4

	mammifère_4 = mammifère ("mouton")
	mammifère_4.nourriture = 500g
	mammifère_4.domestique = oui	
	mammifère_4.nb_pattes = 4

	mammifère_5 = mammifère ("chien")
	mammifère_5.nourriture = 500g
	mammifère_5.domestique = oui
	mammifère_5.nb_pattes = 4	

	animaux_1 = animaux ("serpent")
	animaux_1.nourriture = 200g
	animaux_1.domestique = non

	animaux_2 = animaux ("autruche")
	animaux_2.nourriture = 1kg
	animaux_2.domestique = oui
	animaux_2.nb_pattes = 2

	animaux_3 = animaux ("poule")
	animaux_3.nourriture = 200g
	animaux_3.domestique = oui
	animaux_3.nb_pattes = 2

	print(animal_1)
	print(mammifère_1)
	print(mammifère_2)
	print(mammifère_3)
	print(mammifère_4)
	print(mammifère_5)
	print(animaux_1)
	print(animaux_2)
	print(animaux_3)
