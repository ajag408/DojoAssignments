import re
def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
 matches = []
 for word in words:
 	if re.search(regex,word):
 		matches.append(word)
 return matches

output = get_matching_words("v")
print output

output = get_matching_words("ss")
print output

output = get_matching_words("e$")
print output

output = get_matching_words("b.b")
print output

output = get_matching_words("b.*b")
print output

output = get_matching_words("b*b")
print output

output = get_matching_words("a.*e.*i.*o.*u")
print output

output = get_matching_words("^[regulaxpsion]+$")
print output

output = get_matching_words("(.)\\1")
print output
