class animaux:

	def__init__(self,name,nourriture):
	
		self.name = name
		self.nourriture = nourriture
		
	def__str__(self):
		return "Cet animal est un" + self.name
	

class mammif�re(animaux):

  	def__init__(self,name,nb_pattes,regime_alimentaire,domestique):
	
		self.name = name
		self.nombres_de_pattes = nb_pattes 
		self.regime_alimentaire = regime_alimentaire
		self.domestique = domestique		
	
	def__str__(self):

		return "ce mammif�re a" + str(self.nb_pattes) + "pattes, son regime alimentaire est de" + str(self.regime_alimentaire) + "est-ce un animal domestique ?" +str(self.domestique) + "et est un(e)" + self.name


class animal_marin(animaux):

	def__init__(self,name,r�gime_alimentaire,domestique):
	
		self.name = name
		self.regime_alimentaire = regime_alimentaire
		self.domestique = domestique

	def__str__(self):

		return "Cet animal marin a" + str(self.regime_alimentaire) + " son regime alimentaire est de " +str(self.regime_alimentaire) + "est-ce un animal domestique ?" +str(self.domestique) + "et est un(e)" + self.name


if__name__=="__main__":

	animal_marin_1 = animal_marin("pieuvre")
	animal_marin_1.nourriture = 200g
	animal_marin_1.domestique = non
	
	mammif�re_1 = mammif�re ("humain")
	mammif�re_1.nourriture = 600g
	mammif�re_1.domestique = non
	mammif�re_1.nb_pattes = 2

	mammif�re_2 = mammif�re ("lion")
	mammif�re_2.nourriture = 3kg 
	mammif�re_2.domestique = non
	mammif�re_2.nb_pattes = 4

	mammif�re_3 = mammif�re ("lapin")
	mammif�re_3.nourriture = 100g
	mammif�re_3.domestique = oui
	mammif�re_3.nb_pattes = 4

	mammif�re_4 = mammif�re ("mouton")
	mammif�re_4.nourriture = 500g
	mammif�re_4.domestique = oui	
	mammif�re_4.nb_pattes = 4

	mammif�re_5 = mammif�re ("chien")
	mammif�re_5.nourriture = 500g
	mammif�re_5.domestique = oui
	mammif�re_5.nb_pattes = 4	

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
	print(mammif�re_1)
	print(mammif�re_2)
	print(mammif�re_3)
	print(mammif�re_4)
	print(mammif�re_5)
	print(animaux_1)
	print(animaux_2)
	print(animaux_3)
