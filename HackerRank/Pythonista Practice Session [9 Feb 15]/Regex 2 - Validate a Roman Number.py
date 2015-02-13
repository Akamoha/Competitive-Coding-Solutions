import re
print "True" if re.match('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',raw_input()) != None else "False"import re