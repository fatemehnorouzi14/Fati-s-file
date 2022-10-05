{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "class Methanation:\n",
    "    def __init__(self , rct_enthalpy: float , ch4_frac_product: float , sigma: float):\n",
    "        self.rct_enthalpy = rct_enthalpy\n",
    "        self.ch4_frac_product= ch4_frac_product\n",
    "        self.sigma = sigma\n",
    "    def co2_frac_product(self):\n",
    "        return ((1 - self.ch4_frac_product) / self.sigma * 1/5) * 100\n",
    "    def h2_frac_product(self):\n",
    "        return  ((1 - self.ch4_frac_product) * self.sigma * 4/5) * 100\n",
    "    \n",
    "cat_methanation = {\n",
    "    \"rct_enthalpy\": -165,\n",
    "    \"ch4_frac_product\":0.95,\n",
    "    \"sigma\": 1.0}\n",
    "\n",
    "\n",
    "object = Methanation(cat_methanation[\"rct_enthalpy\"] , cat_methanation[\"ch4_frac_product\"] , cat_methanation[\"sigma\"] )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.6 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "aee8b7b246df8f9039afb4144a1f6fd8d2ca17a180786b69acc140d282b71a49"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
