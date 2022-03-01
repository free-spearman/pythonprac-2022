import textdistance as txtdist
MESS = "Строка без пробела \n"

def dist(s1, s2):
    return txtdist.levenshtein(s1, s2)


if ( __name__ == '__main__'):
	
	str1 = input(MESS).replace(" ",'')
	str2 = input(MESS).replace(" ",'')

	res = dist(str1, str2)

	print(res)