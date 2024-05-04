import re

text = "_a_axc.adwe-Acas_d_asabbbxw-afeAcasabbxAqw_das,eaabfabbbbcwe,g4tr"
#1
pat_abbb = r'a[b]*'
matching = re.findall(pat_abbb, text)
#print(matching)


#2
pat_ab_abb = r'(abbb|abb)[^b]'
matching = re.findall(pat_ab_abb, text)
#print(matching)


#3
pat_a_b = r'([a-z](_[a-z])+)'
matching = re.findall(pat_a_b, text)
#print(matching)


#4
pat_Aabb = r'([A-Z]{1,1}[a-z]+)'   #([A-Z]{1,1}[a-z]{2,})*  2 or more letters
matching = re.findall(pat_Aabb, text)
#print(matching)

#5
pat_acdb = r'a[a-z]*b'   #(a[a-z]*?b) - nearest b
matching = re.findall(pat_acdb, text)
#print(matching)


#6
pat_dot_comma_space = r'[\s,.]'
matching = re.sub(pat_dot_comma_space, ':', text)
#print(matching)


#7
pat_snakeTOcamel = r'_([a-z])'
matching = re.sub(pat_snakeTOcamel, lambda match: match.group(1).upper(), text)
#print(matching)

#8
pat_splitA = r'[A-Z][^A-Z]*'
matching = re.findall(pat_splitA, text)
#print(matching)


#9
pat_spaceA = r'([a-z])([A-Z])'  #([^A-Z])([A-Z])
matching = re.sub(pat_spaceA, lambda match: match.group(1) + " "+ match.group(2), text)
#print(matching)


#10
pat_camelTOsnake = r'([a-z])([A-Z])'
matching = re.sub(pat_camelTOsnake, lambda match: match.group(1) + "_"+ match.group(2).lower(), text)
#print(matching)