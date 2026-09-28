amount_due = 50
def ask(amount_d):
	give = input()
	amount_given = int(give)
	test(amount_given,amount_d)



def test(g,d):
	if g<d:
		d -= g
		due = str(d)
		print("Remaining cost:"+due)
		amount_d = d
		ask(amount_d)
	elif g>d:
		d -= g
		change = abs(d)
		change2 = str(change)
		print("change due:"+change2)
	else:
		print("enjoy your coke")
	return

ask(amount_due)
