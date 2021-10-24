from lab4.variables import Unassigned


class Solver(object):
    def __init__(self):
        self.counter = 0

    def get_description(self):
        msg = "%s is an abstract class" % self.__class__.__name__
        raise NotImplementedError(msg)

    def get_solution(self, domains, constraints, vconstraints):
        msg = "%s is an abstract class" % self.__class__.__name__
        raise NotImplementedError(msg)


class BacktrackingForwardCheckingMRV(Solver):
    def __init__(self, forwardcheck=True, mrv=True):
        super().__init__()
        self._forward_check = forwardcheck
        self._mrv = mrv

    def get_description(self):
        return "Backtracking Algorithm with Forward check and Minimum remaining values "

    def FC_MRV(self, solutions, domains, vconstraints, assignments, single):
        # Minimum Remaining Values (MRV) heuristics
        lst = [(len(domains[variable]), variable) for variable in domains]
        mrv = self._mrv
        if mrv:
            lst.sort()
        for item in lst:
            if item[-1] not in assignments:
                # Found an unassigned variable. Let's go.
                break
        else:
            # No unassigned variables. We've got a solution.
            solutions.append(assignments.copy())
            return solutions

        variable = item[-1]
        assignments[variable] = Unassigned

        forwardcheck = self._forward_check
        if forwardcheck:
            pushdomains = [domains[x] for x in domains if x not in assignments]
        else:
            pushdomains = None

        for value in domains[variable]:
            assignments[variable] = value
            if pushdomains:
                for domain in pushdomains:
                    domain.push_state()
            for constraint, variables in vconstraints[variable]:
                self.counter = self.counter + 1
                if not constraint(variables, domains, assignments, pushdomains):
                    # Value is not good.
                    break
            else:
                # Value is good. Recurse and get next variable.
                self.FC_MRV(solutions, domains, vconstraints, assignments, single)
                if solutions and single:
                    return solutions
            if pushdomains:
                for domain in pushdomains:
                    domain.pop_state()
        del assignments[variable]
        return solutions

    def get_solution(self, domains, constraints, vconstraints):
        self.counter = 0
        solutions = self.FC_MRV([], domains, vconstraints, {}, False)
        return solutions and solutions[0] or None


class BacktrackingMinimumRemainingValues(Solver):
    def __init__(self, forwardcheck=False, mrv=True):
        super().__init__()
        self._forward_check = forwardcheck
        self._mrv = mrv

    def get_description(self):
        return "Backtracking Algorithm with Minimum remaining values "

    def MRV(self, solutions, domains, vconstraints, assignments, single):
        # Minimum Remaining Values (MRV) heuristics
        lst = [(len(domains[variable]), variable) for variable in domains]
        mrv = self._mrv
        if mrv:
            lst.sort()
        for item in lst:
            if item[-1] not in assignments:
                # Found an unassigned variable. Let's go.
                break
        else:
            # No unassigned variables. We've got a solution.
            solutions.append(assignments.copy())
            return solutions

        variable = item[-1]
        assignments[variable] = Unassigned

        forwardcheck = self._forward_check
        if forwardcheck:
            pushdomains = [domains[x] for x in domains if x not in assignments]
        else:
            pushdomains = None

        for value in domains[variable]:
            assignments[variable] = value
            if pushdomains:
                for domain in pushdomains:
                    domain.push_state()
            for constraint, variables in vconstraints[variable]:
                self.counter = self.counter + 1
                if not constraint(variables, domains, assignments, pushdomains):
                    # Value is not good.
                    break
            else:
                # Value is good. Recurse and get next variable.
                self.MRV(solutions, domains, vconstraints, assignments, single)
                if solutions and single:
                    return solutions
            if pushdomains:
                for domain in pushdomains:
                    domain.pop_state()
        del assignments[variable]
        return solutions

    def get_solution(self, domains, constraints, vconstraints):
        self.counter = 0
        solutions = self.MRV([], domains, vconstraints, {}, False)
        return solutions and solutions[0] or None


class BacktrackingForwardCheck(Solver):
    def __init__(self, forwardcheck=True, mrv=True):
        super().__init__()
        self._forward_check = forwardcheck
        self._mrv = mrv

    def get_description(self):
        return "Backtracking Algorithm with Forward check "

    def FC(self, solutions, domains, vconstraints, assignments, single):
        # Minimum Remaining Values (MRV) heuristics
        lst = [(len(domains[variable]), variable) for variable in domains]
        mrv = self._mrv
        if mrv:
            lst.sort()
        for item in lst:
            if item[-1] not in assignments:
                # Found an unassigned variable. Let's go.
                break
        else:
            # No unassigned variables. We've got a solution.
            solutions.append(assignments.copy())
            return solutions

        variable = item[-1]
        assignments[variable] = Unassigned

        forwardcheck = self._forward_check
        if forwardcheck:
            pushdomains = [domains[x] for x in domains if x not in assignments]
        else:
            pushdomains = None

        for value in domains[variable]:
            assignments[variable] = value
            if pushdomains:
                for domain in pushdomains:
                    domain.push_state()
            for constraint, variables in vconstraints[variable]:
                self.counter = self.counter + 1
                if not constraint(variables, domains, assignments, pushdomains):
                    # Value is not good.
                    break
            else:
                # Value is good. Recurse and get next variable.
                self.FC(solutions, domains, vconstraints, assignments, single)
                if solutions and single:
                    return solutions
            if pushdomains:
                for domain in pushdomains:
                    domain.pop_state()
        del assignments[variable]
        return solutions

    def get_solution(self, domains, constraints, vconstraints):
        self.counter = 0
        solutions = self.FC([], domains, vconstraints, {}, False)
        return solutions and solutions[0] or None
