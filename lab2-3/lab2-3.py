# Pentru a reprezenta o stare a problemei, avem nevoie de de 4 liste, toate continand maxim n elemente si sa stim daca
# barca se afla pe malul stang sau cel drept:
#  1. O lista care sa contina sotii de pe malul stang
#  2. O lista care sa contina sotiile de pe malul stang
#  3. O lista care sa contina sotii de pe malul drept
#  4. O lista care sa contina sotiile de pe malul drept
#  5. O variabila booleana care sa stocheze malul unde se afla barca(TRUE - malul drept, FALSE - malul stang)
# a) Orice stare
#  Presupunem ca n=4, atunci o stare a problemei este cand pe malul stang sunt h1, h2, h3, h4(toti sotii) si
#  w2(sotia nr.2), si pe malul drept sunt restul sotiilor, iar barca este pe malul drept.

class Problem:
    def __init__(self, n, boat, husbands, wives):
        self.n = n
        self.boat = boat
        self.husbands = husbands
        self.wives = wives


class State:
    def __init__(self, leftHusbands, leftWives, rightHusbands, rightWives, shore):
        self.leftHusbands = leftHusbands
        self.leftWives = leftWives
        self.rightHusbands = rightHusbands
        self.rightWives = rightWives
        self.shore = shore


# b)
# Starea initiala este starea in care toti sunt pe malul stang si barca pe acelasi mal.
def get_initial_state(problem):
    return State(problem.husbands, problem.wives, [], [], False)

# Starea finala este starea in care toti sunt pe malul drept, si barca pe acelasi mal.
def get_final_state(problem):
    return State([], [], problem.husbands, problem.wives, True)

# Verificam daca nu e nimeni pe malul stang(sau am fi putut verifica daca toti se afla pe malul drept)
def is_final_state(state):
    return state.leftHusbands == [] and state.leftWives == []
