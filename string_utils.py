def split_before_uppercases(formula):
    parts = []
    current = ""

    for char in formula:
        if char.isupper():
            if current:
                parts.append(current)
            current = char
        else:
            current += char

    if current:
        parts.append(current)

    return parts


def split_at_digit(formula):

  prefix = ""
  digits = ""

  for char in formula:
      if char.isdigit():
          digits += char
      else:
          prefix += char

  count = int(digits) if digits else 1
  return prefix, count

def count_atoms_in_molecule(molecular_formula):
    molecules_with_counter = {}

    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        if atom_name in molecules_with_counter:
           molecules_with_counter[atom_name] += atom_count
        else:
         molecules_with_counter[atom_name] = atom_count   
        
    return molecules_with_counter



def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
