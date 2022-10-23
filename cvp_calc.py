class Cvp_calc:
    def __init__(self, sls, vc, fc):
        self.sls = sls
        self.vc = vc
        self.fc = fc

    def break_even_units(self):
        cm = (self.sls - self.vc)
        result = self.fc / cm
        return result

    def break_even_dollars(self):
        cm_pct = (self.sls - self.vc) / self.sls
        result = self.fc / cm_pct
        return result

    def bev_units_ni(self, ni):
        """Returns break even units for specific net income"""
        cm = self.sls - self.vc
        break_even = (self.fc + ni) / cm
        return break_even

    def bev_units_ni(self, ni):
        """Returns break even dollars for specific net income"""
        cm = self.sls - self.vc
        cm_pct = cm / self.sls
        break_even = (self.fc + ni) / cm_pct
        return break_even
