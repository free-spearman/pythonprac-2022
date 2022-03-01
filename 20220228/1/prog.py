import textdistance as txtdist

def dist(s1, s2):
    return txtdist.levenshtein(s1, s2)
 
