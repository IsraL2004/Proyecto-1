from modelos import *

# Ejecucion de los modelos para 50, 200 y 500 nodos

malla(7,8, True).exportar_dot("Malla-50.gv")
grafoErdosRenyi(50, 120, True).exportar_dot("Erdos-50.gv")
grafoGibert(50, 10, True).exportar_dot("Gibert-50-10.gv")
grafoGeografico(50, 0.2, True).exportar_dot("Geografico-50-02.gv")
grafoBarabasiAlbert(50, 3, True).exportar_dot("BarasiAlbert-50.gv")
grafoDorogovtsevMendes(50, True).exportar_dot("DorogovMendes-50.gv")

malla(14,15, True).exportar_dot("Malla-200.gv")
grafoErdosRenyi(200, 2000, True).exportar_dot("Erdos-200.gv")
grafoGibert(200, 10, True).exportar_dot("Gibert-200-10.gv")
grafoGeografico(200, 0.2, True).exportar_dot("Geografico-200-02.gv")
grafoBarabasiAlbert(200, 4, True).exportar_dot("BarasiAlbert-200.gv")
grafoDorogovtsevMendes(200, True).exportar_dot("DorogovMendes-200.gv")

malla(25,20, True).exportar_dot("Malla-500.gv")
grafoErdosRenyi(500, 12000, True).exportar_dot("Erdos-500.gv")
grafoGibert(500, 10, True).exportar_dot("Gibert-500-10.gv")
grafoGeografico(500, 0.2, True).exportar_dot("Geografico-500-02.gv")
grafoBarabasiAlbert(500, 5, True).exportar_dot("BarasiAlbert-500.gv")
grafoDorogovtsevMendes(500, True).exportar_dot("DorogovMendes-500.gv")


