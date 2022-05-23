import sys
import ast
import re
import textdistance
import difflib

def tree(item):
	txt = ast.parse(ast.unparse(ast.parse(item)))
	dump = ast.dump(txt, annotate_fields = False)[8:-6]
	dump = re.sub(r"([A-Z][a-z]+)+", r"@", dump)
	dump = re.sub(r"[^\(\),'@]", r"", dump)
	dump = re.sub(r"('@'|'')", r"", dump)
	dump = re.sub(r"@(,|\)|@)", r"\1", dump) 
	return dump

with open(sys.argv[1]) as f:
	prog1 = f.read()
with open(sys.argv[2]) as f:
	prog2 = f.read()


dump1 = tree(prog1)
dump2 = tree(prog2)

dst = textdistance.damerau_levenshtein.normalized_distance(dump1, dump2)
print(dst)
if len(sys.argv) == 3:
	if dst <= 0.1:
		dif = difflib.HtmlDiff().make_file(prog1, prog2)
		sys.stdout.writelines(dif)
	else:
		print("Plagiat is not detected")
else:
	print("Wrong input")
