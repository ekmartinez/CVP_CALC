class Cvp_calc:
    def __init__(self, sls, vc, fc):
        self.sls = sls
        self.vc = vc
        self.fc = fc

    def break_even_dollars(self):
        cm_pct = (self.sls - self.vc) / self.sls
        result = self.fc / cm_pct
        return result

