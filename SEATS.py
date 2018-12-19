N = input()


def TypeFunction():
	seatTypes = []
	
	for i in range(1, 18):
		seatTypes.append("WS")
		seatTypes.append("MS")
		seatTypes.append("AS")
		seatTypes.append("AS")
		seatTypes.append("MS")
		seatTypes.append("WS")
	return seatTypes

def PosiFunction():
	seatPosi = []
	for i in range(1, 10):
		
		for i in range(1, 13):
			seatPosi.append(i)

	
	return seatPosi	


def oppositeFunction():
	OppositesArray = [""] * 108
	seatPosi = PosiFunction()



	for i in range(0, 108):
		if seatPosi[i] <= 6:
			for j in range(1, 7):
				if seatPosi[i] == j:
					OppositesArray[i]  = i + 14 - (j*2)
		else:	
			for j in range(0, 6):
				if seatPosi[i] == j+7:
					OppositesArray[i]  = i - (j*2)
			
	return OppositesArray		



SeatsArray = TypeFunction()
PosiArray = PosiFunction()
OppositesArray = oppositeFunction()



for i in range(0, int(N)):
	seatNr = input()

	print ( str(OppositesArray[int(seatNr)-1]) + " " + str(SeatsArray[int(seatNr)-1]) )
			