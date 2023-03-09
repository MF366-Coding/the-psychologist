from clsCmd import clear

ErrorType = 'NULL'
ErrorString = 'NULL'
ErrorNumber = 'NULL'
FunctionToRun = 'NULL'

dev_only_data={
    # Only useful for devs or people interested in the actual code
	ErrorType:"Wrong Input",
	ErrorNumber:1,
	FunctionToRun:"function run() with no arguments",
	ErrorString:"Collected info on Operation Error Number #001:\
				App quitted with wrong input.\
				A bad input was given.\
				Couldn't load functions at next phase.\
    			Error: WrongInputCouldNotFindCorrectInput\
				Solution: AppQuittedWithCommandOrWrongCommand"
}

def run():
    clear()
    print("Collected info on Operation Error Number #001\n\
	App quitted with wrong input.\n\
	A bad input was given.\n\
	Couldn't load functions at next phase.")
    quit()
        