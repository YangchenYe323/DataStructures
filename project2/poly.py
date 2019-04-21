from Linked_List import Linked_List

class Poly_Val:
 def __init__(self, coef, exp):
 	self.__coefficient = coef
 	self.__exponent = exp
 def get_coefficient(self):
 	return self.__coefficient
 def get_exponent(self):
 	return self.__exponent
 def __str__(self):
 	return str(self.__coefficient) + 'x^' + str(self.__exponent)

if __name__ == '__main__':
 p1 = Linked_List()
 p1.append_element(Poly_Val(10,1012))
 p1.append_element(Poly_Val(5,14))
 p1.append_element(Poly_Val(1,0))
 p2 = Linked_List()
 p2.append_element(Poly_Val(3,1990))
 p2.append_element(Poly_Val(-2,14))
 p2.append_element(Poly_Val(11,1))
 p2.append_element(Poly_Val(5,0))
 p3 = Linked_List()
 i = 0; j = 0
 while i < len(p1) and j < len(p2):
 	Pol1 = p1.get_element_at(i)
 	Pol2 = p2.get_element_at(j)
 	if Pol1.get_exponent() > Pol2.get_exponent():
 		p3.append_element(Poly_Val(Pol1.get_coefficient(),Pol1.get_exponent()))
 		i = i + 1
 	elif Pol1.get_exponent() < Pol2.get_exponent():
 		p3.append_element(Poly_Val(Pol2.get_coefficient(),Pol2.get_exponent()))
 		j = j + 1
 	else:
 		Pol3 = Poly_Val(Pol1.get_coefficient()+Pol2.get_coefficient(), Pol1.get_exponent())
 		p3.append_element(Pol3)
 		i = i + 1
 		j = j + 1
 while i < len(p1):
 	p3.append_element(Poly_Val(Pol1.get_coefficient(),Pol1.get_exponent()))
 	i = i + 1
 while j < len(p2):
 	p3.append_element(Poly_Val(Pol2.get_coefficient(),Pol2.get_exponent()))
 	j = j + 1
 print(p1)
 print(p2)
 print(p3)
 # TODO populate p3 with the sum of p1 and p2.
 # our solution to build p3 is 22 lines of code.