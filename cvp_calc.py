class Cvp_calc:
    def __init__(self, sls, vc, fc):
        self.sls = sls
        self.vc = vc
        self.fc = fc

    def break_even_units(self):
        """Returns break even units"""
        cm = (self.sls - self.vc)
        result = self.fc / cm
        return result

    def break_even_dollars(self):
        """Returns break even dollars"""
        cm_pct = (self.sls - self.vc) / self.sls
        result = self.fc / cm_pct
        return result

    def bev_units_ni(self, ni):
        """Returns break even units for specific net income"""
        cm = self.sls - self.vc
        break_even = (self.fc + ni) / cm
        return break_even
    
    def bev_units_ni_tx(self, ni, tx):
        """Returns break even units for specific net income including tax impact"""
        cm = self.sls - self.vc
        break_even = (self.fc + (ni / (1 - tx))) / cm
        return break_even

    def bev_dollars_ni(self, ni):
        """Returns break even dollars for specific net income"""
        cm = self.sls - self.vc
        cm_pct = cm / self.sls
        break_even = (self.fc + ni) / cm_pct
        return break_even

    def bev_dollars_ni_tx(self, ni, tx):
        """Returns break even dollars for specific net income including tax impact"""
        cm = self.sls - self.vc
        cm_pct = cm / self.sls
        break_even = (self.fc + (ni / (1 - tx))) / cm_pct
        return break_even