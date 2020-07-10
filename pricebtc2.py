#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    pip install pycoingecko
    Powered by CoinGecko API
"""

from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def main():
    print(cg.ping())
    #    print(cg.get_price(ids='bitcoin', vs_currencies='eur'))
    string = cg.get_price(ids='bitcoin', vs_currencies='eur')
    cadena = str(string)
    
    print(cadena)
    price = cadena[20:27:]
    print (price)
    float(price)
    
    
    bitcoinstengo = input("¿Cuántos Btc tienes?: ")
    
    resultado = float(bitcoinstengo) * float(price)
    
    print("Tienes €")
    print(resultado)

if __name__ == "__main__":
    main()
