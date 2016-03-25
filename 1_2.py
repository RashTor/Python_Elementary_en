import random

dict_tile = {'NO': '#########', 'LR': '###   ###',
             'LT': '# #  ####', 'BR': '####  # #', 'LB': '###  ## #', 'TR': '# ##  ###'}

def generate_lab():
    n_dim = n_elem = 0
    lab_gen = [[random.choice(dict_tile.keys())], [random.choice(dict_tile.keys())]]
    while n_dim < 2:
        n_elem=0
        while n_elem < 10:
            # lab_gen([n_dim][n_elem])=random.choice(dict_tile)
            lab_gen[n_dim].append(random.choice(dict_tile.keys()))
            #random.choice(dict_tile)
            n_elem += 1
        n_dim += 1
    return (lab_gen)


def create_lab(lab):
    lab_str = ""
    for dest_lab in lab:
        i = 0
        while i <= 8:
            for elem_lab in dest_lab:
                elem_tile = dict_tile[elem_lab]
                lab_str += elem_tile[i:i + 3]
            lab_str += '\n'
            i += 3
    print lab_str


def main():
    lab_default = (["NO", "BR", "LR", "LB", "NO"], ["LR", "LT", "NO", "TR", "LR"])
    var = 1
    while var != 0:
        var = input("Chose var:\n1)\tGenerate\n2)\tCreate\n0)\tExit\n")
        if var == 1:
            lab_default = generate_lab()
            # break
        elif var == 2:
            create_lab(lab_default)
            # break
        else:
            var = input("Chose another var:\n1)\tGenerate\n2)\tCreate\n0)\tExit\n")


if __name__ == "__main__":
    main()