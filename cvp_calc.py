class Cvp_calc:
    def __init__(self, sls, vc, fc):
        self.sls = sls
        self.vc = vc
        self.fc = fc

    def break_even_dollars(self):
        cm_pct = (self.sls - self.vc) / self.sls
        result = self.fc / cm_pct
        return result

    def bev_units_ni(self, ni):
        """Returns break even units for specific net income"""
        cm = self.sls - self.vc
        break_even = (self.fc + ni) / cm
        return break_even

bv = Cvp_calc(16, 10, 48000)
print(bv.bev_units_ni(24000))

