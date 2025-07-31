class PrimeFactor:
    def of(self, number) -> []:
        factors = []
        if number > 1:
            devisor = 2
            if number == 4:
                while number % devisor == 0:
                    factors.append(devisor)
                    number //= devisor
            elif number == 6:
                while number % devisor == 0:
                    factors.append(devisor)
                    number //= devisor
                devisor+=1
                while number % devisor == 0:
                    factors.append(devisor)
                    number //= devisor
            else:
                factors.append(number)
        return factors
