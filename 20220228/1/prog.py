import textdistance as txtdist
MESS = "Строка без пробела \n"
LEVENSHTEIN = "L"
DAMERAU_LEVENSHTEIN = "D"

def dist(s1, s2, type):
	if type == LEVENSHTEIN:
		return txtdist.levenshtein(s1, s2)	
	elif type == DAMERAU_LEVENSHTEIN:
		return txtdist.damerau_levenshtein(s1, s2)
	else:
		return -1

    


if ( __name__ == '__main__'):
	
	str1 = input(MESS).replace(" ",'')
	str2 = input(MESS).replace(" ",'')
	str3 = input(MESS).replace(" ",'')

	res = dist(str1, str2, str3)
