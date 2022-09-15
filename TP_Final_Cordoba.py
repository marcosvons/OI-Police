# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:52:43 2021

@author: Witbor
"""
import sys
import picos
import numpy as np

P=picos.Problem()

u = picos.BinaryVariable('u', 15)
p = picos.IntegerVariable('p', 15, lower=0)
a = picos.IntegerVariable('a', (7,15), lower=0)

C = [520, 514, 518, 502, 498, 460, 413, 407, 375, 497, 420, 380, 490, 478, 466]
adisp = [95, 110, 76, 86, 104, 94, 110, 96, 84, 102, 90, 108, 102, 84, 84]
adispo = [23, 38, 4, 14, 32, 22, 38, 24, 12, 30, 18, 36, 30, 12, 12] 

P.set_objective('min', picos.sum( ((u^C)*72) + (p*17000) + ((p^C)*6)))

#P.add_constraint( 72 + 6*p[0] <= adisp[0] )

#Restriccion de Area para patrulleros
P.add_constraint( 6*p <= adispo )

#Restricción de dos viajes por patrullero
P.add_constraint( picos.sum(a[:, 0]) == p[0]*2)
P.add_constraint( picos.sum(a[:, 1]) == p[1]*2)
P.add_constraint( picos.sum(a[:, 2]) == p[2]*2)
P.add_constraint( picos.sum(a[:, 3]) == p[3]*2)
P.add_constraint( picos.sum(a[:, 4]) == p[4]*2)
P.add_constraint( picos.sum(a[:, 5]) == p[5]*2)
P.add_constraint( picos.sum(a[:, 6]) == p[6]*2)
P.add_constraint( picos.sum(a[:, 7]) == p[7]*2)
P.add_constraint( picos.sum(a[:, 8]) == p[8]*2)
P.add_constraint( picos.sum(a[:, 9]) == p[9]*2)
P.add_constraint( picos.sum(a[:, 10]) == p[10]*2)
P.add_constraint( picos.sum(a[:, 11]) == p[11]*2)
P.add_constraint( picos.sum(a[:, 12]) == p[12]*2)
P.add_constraint( picos.sum(a[:, 13]) == p[13]*2)
P.add_constraint( picos.sum(a[:, 14]) == p[14]*2)

#Restriccion de demanda de delitos
P.add_constraint( picos.sum(a[0, :]) == 10)
P.add_constraint( picos.sum(a[1, :]) == 4)
P.add_constraint( picos.sum(a[2, :]) == 1)
P.add_constraint( picos.sum(a[3, :]) == 4)
P.add_constraint( picos.sum(a[4, :]) == 3)
P.add_constraint( picos.sum(a[5, :]) == 3)
P.add_constraint( picos.sum(a[6, :]) == 7)

#Restriccion de ubicacion y patrulleros en conjunto
P.add_constraint( p[0] <= 10000*u[0] )
P.add_constraint( p[1] <= 10000*u[1] )
P.add_constraint( p[2] <= 10000*u[2] )
P.add_constraint( p[3] <= 10000*u[3] )
P.add_constraint( p[4] <= 10000*u[4] )
P.add_constraint( p[5] <= 10000*u[5] )
P.add_constraint( p[6] <= 10000*u[6] )
P.add_constraint( p[7] <= 10000*u[7] )
P.add_constraint( p[8] <= 10000*u[8] )
P.add_constraint( p[9] <= 10000*u[9] )
P.add_constraint( p[10] <= 10000*u[10] )
P.add_constraint( p[11] <= 10000*u[11] )
P.add_constraint( p[12] <= 10000*u[12] )
P.add_constraint( p[13] <= 10000*u[13] )
P.add_constraint( p[14] <= 10000*u[14] )

#Prueba 12 min
P.add_constraint( a[2, 7] == 0)
P.add_constraint( a[6, 8] == 0)
P.add_constraint( a[0, 8] == 0)
P.add_constraint( a[1, 8] == 0)
P.add_constraint( a[1, 9] == 0)
P.add_constraint( a[6, 9] == 0)
P.add_constraint( a[2, 11] == 0)
P.add_constraint( a[2, 8] == 0)
P.add_constraint( a[3, 6] == 0)
P.add_constraint( a[5, 6] == 0)
P.add_constraint( a[5, 9] == 0)
P.add_constraint( a[4, 12] == 0)
P.add_constraint( a[6, 11] == 0)
P.add_constraint( a[4, 14] == 0)
P.add_constraint( a[2, 9] == 0)
P.add_constraint( a[3, 5] == 0)
P.add_constraint( a[3, 14] == 0)
P.add_constraint( a[4, 6] == 0)
P.add_constraint( a[5, 5] == 0)




P.solve(solver='glpk')
print('COSTO: ',P.value)
print('Ubicaciones = ', u)
print('Patrulleros = ', p)
print('Asignaciones Central 7: ', a[:, 6])
print('Asignaciones Central 8: ', a[:, 7])
print('Asignaciones Central 12: ', a[:, 11])