def ap(s):
	return s + "\n" 

def create_input_file(data):

	o = ""

	#Header info
	o += ap("!FDMNES input file")
	o += ap("!Generated automatically via Python")
	o += ap(data["title_line"])

	#Output file
	o += ap("Filout")
	o += ap(data["outfile"])

	#Data range
	o += ap("Range")
	o += ap(data["range"])

	#Radius
	o += ap("Radius")
	o += ap(data["radius"])

	#Crystal parameters
	o += ap("Crystal")
	o += ap(data["crystal_dim"])

	#Atoms
	for atom in data["atoms"]:
		o += ap(atom)

	#Convolution
	o += ap("Arc")

	#Fermi Energy
	o += ap("Efermi")
	o += ap(data["fermi_energy"])

	o += ap("End")

	return o


if __name__ == "__main__":

	#Data setup
	data = {}
	
	data["title_line"] = "!Cu K-Edge"
	data["outfile"] = "outfile.txt"
	data["range"] = "-10. 0.2 0. 0.5 10. 1. 40."
	data["radius"] = "3.0"

	data["atoms"] = []
	data["atoms"].append("29 0.0 0.0 0.0")
	data["atoms"].append("29 0.5 0.5 0.0")
	data["atoms"].append("29 0.0 0.5 0.5")
	data["atoms"].append("29 0.5 0.0 0.5")

	data["crystal_dim"] = "3.610 3.610 3.610 90. 90. 90."
	data["fermi_energy"] = "-6."

	print create_input_file(data)