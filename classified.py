statement = input("What's the message to be classified?")
target_words = ["james", "london", "mi6", "classified", "paris", "midnight", "nuclear", "asset"]
returned = []
for word in statement.split():
	word2=word.lower()
	if word2 in target_words:
		redact = word2.replace(word2, "[REDACTED]")
		returned.append(redact)
	else:
		returned.append(word)
print(*returned)
