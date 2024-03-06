class ChemicalData:
	formula : str = "ASDF"
	name : str = "ㅁㄴㅇㄹ"
	components : dict = {}

	def __init__(self, formula : str, name : str, components : dict) -> None:
		self.formula = formula
		self.name = name
		self.components = components