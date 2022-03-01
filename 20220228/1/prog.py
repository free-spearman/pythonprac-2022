import textdistance as txtdist
from multiprocessing import Pool,context

MESS = "Строка без пробела \n"
LEVENSHTEIN = "L"
DAMERAU_LEVENSHTEIN = "D"
TIMEOUT = 1

def dist(s1, s2, type):
	if type == LEVENSHTEIN:
		return txtdist.levenshtein(s1, s2)	
	elif type == DAMERAU_LEVENSHTEIN:
		return txtdist.damerau_levenshtein(s1, s2)
	else:
		return -1

    


if ( __name__ == '__main__'):
	#тут вызов
	str1 = input(MESS).replace(" ",'')
	str2 = input(MESS).replace(" ",'')
	str3 = input(MESS).replace(" ",'')

	process = Pool(1).apply_async(dist, (str1, str2, str3))

	try:
		res = process.get(timeout=TIMEOUT)	
	except context.TimeoutError:
		print("TIMEOUT")
		res = -1

	#Тут вывод 
	print(res)