
class Methanation:
    def __init__(self , rct_enthalpy: float , ch4_frac_product: float , sigma: float):
        self.rct_enthalpy = rct_enthalpy
        self.ch4_frac_product= ch4_frac_product
        self.sigma = sigma
    def co2_frac_product(self):
        return ((1 - self.ch4_frac_product) / self.sigma * 1/5) * 100
    def h2_frac_product(self):
        return  ((1 - self.ch4_frac_product) * self.sigma * 4/5) * 100
        ""
        h2 
        ""
    
cat_methanation = {
    "rct_enthalpy": -165,
    "ch4_frac_product":0.95,
    "sigma": 1.0}


object = Methanation(cat_methanation["rct_enthalpy"] , cat_methanation["ch4_frac_product"] , cat_methanation["sigma"] )