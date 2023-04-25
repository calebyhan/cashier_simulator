import cashier


class Sim:
    def __init__(self, num_cashiers, rate):
        self.num_cashiers = num_cashiers
        self.rate = rate
        self.min = 0
        self.stats = {"total_queue": []}
        self.total_queue = 0

        self.cashiers = []
        for _ in self.num_cashiers:
            self.cashiers.append(cashier.Cashier())

    def run(self):
        self.min += 1
