class PrimeFactor:
    def of(self, number) -> []:
        factors = []
        devisor = 2
        while number % devisor == 0:
            factors.append(devisor)
            number //= devisor
        devisor += 1
        while number % devisor == 0:
            factors.append(devisor)
            number //= devisor

        return factors
# 실수로 브랜치를 안만들고 작업해버렸숩니다!