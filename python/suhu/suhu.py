#Program memcari °C
	
def R_to_C (nilai:int):
	c = 5 / 4 * nilai
	return c
		
def F_to_C (nilai:int):
	c = 5 / 9 * (nilai - 32)
	return c
	
def K_to_C (nilai:int):
	c = nilai - 273
	return c
				
#Program mencari °F

def C_to_F (nilai:int):
	f = 9 / 5 * nilai + 32
	return f
			
def R_to_F (nilai:int):
	f = 9 / 4 * nilai + 32
	return f
			
def K_to_F (nilai:int):
	f = 9 / 5 * (nilai - 273) + 32
	return f
						
#Program mencari °R

def C_to_R (nilai:int):
	r = 4 / 5 * nilai
	return r

def F_to_R (nilai:int):
	r = 4 / 9 * (nilai - 32)
	return r

def K_to_R (nilai:int):
	r = 4 / 5 * (nilai - 273)
	return r

#Peogram manecari Kelvin
       
def C_to_K (nilai:int):
	k = nilai + 273
	return k
	
def R_to_K (nilai:int):
	k = 5 / 4 * nilai + 273
	return k

def F_to_K (nilai:int):
	k = 5 / 9 * (nilai - 32) + 273
	return k
	