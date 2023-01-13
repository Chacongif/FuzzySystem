#!/usr/bin/env python
# coding: utf-8

# In[75]:


#Librerias
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# In[76]:


#Aplicacion Minecraft
#Variables 
rendimiento = ctrl.Antecedent(np.arange(0, 24, 1), 'rendimiento')
ataque = ctrl.Antecedent(np.arange(0, 16, 1), 'ataque')
dano = ctrl.Consequent(np.arange(0, 90, 1), 'dano')

#Aplicar funciones de membresia
rendimiento["REGULAR"] = fuzz.trimf(rendimiento.universe, [0, 4, 8])
rendimiento["BUENA"] = fuzz.trimf(rendimiento.universe, [8, 12, 16])
rendimiento["EXCELENTE"] = fuzz.trimf(rendimiento.universe, [16, 20, 24])

ataque["NORMAL"] = fuzz.trimf(ataque.universe, [0, 5, 9])
ataque["CRITICO"] = fuzz.trimf(ataque.universe, [9, 13, 16])


dano['POCO'] = fuzz.trimf(dano.universe, [0, 15, 30])
dano['MEDIO'] = fuzz.trimf(dano.universe, [30, 45, 60])
dano['MUCHO'] = fuzz.trimf(dano.universe, [60, 75, 90])


# In[77]:


#Ver tabla de rendimiento
rendimiento['REGULAR'].view()


# In[78]:


#Ver tabla de ataque
ataque['NORMAL'].view()


# In[79]:


#Ver tabla de daño
dano['POCO'].view()


# In[80]:


#Aplciar las reglas del sistema
regla1 = ctrl.Rule(rendimiento["REGULAR"] & ataque["NORMAL"], dano['POCO'])
regla2 = ctrl.Rule(rendimiento["BUENA"] & ataque["NORMAL"], dano['MEDIO'])
regla3 = ctrl.Rule(rendimiento["EXCELENTE"] & ataque["NORMAL"], dano['MUCHO'])
regla4 = ctrl.Rule(rendimiento["REGULAR"]  &ataque["NORMAL"], dano['POCO'])
regla5 = ctrl.Rule(rendimiento["BUENA"] & ataque["CRITICO"], dano['MEDIO'])
regla6 = ctrl.Rule(rendimiento["EXCELENTE"] & ataque["CRITICO"], dano['MUCHO'])


# In[81]:


#Crear un control de sistema para la simulación
dano_ctrl = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6])


# In[82]:


#Crear la simulación, haciendo el fuzziness
danos = ctrl.ControlSystemSimulation(dano_ctrl)


# In[121]:


#Hacer las entradas de rendimiento y ataque
danos.input["rendimiento"] = 1
danos.input["ataque"] = 8

#Hacer los números
danos.compute()


# In[122]:


#Imprimir resultado y ver tabla
print(danos.output["dano"])
dano.view(sim=danos)




# In[103]:


#Simulador de Autoajuste
import random

print("====Iniciando Simulador de Daño Minecraft====")
print("")

#Hacer las entradas de rendimiento y ataque
#danos.input["rendimiento"] = 1
#danos.input["ataque"] = 1

#Hacer los números
#danos.compute()

danoValor = 15

#print(danos.output["dano"])

for i in range(26):
    danoAle = random.randint(1,14)
    danos.input["rendimiento"] = danoValor
    danos.compute()
    print("El daño hecho si el rendimiento es: " + str(danoValor) + " y el daño es: " + str(danoAle) + " entonces el daño hecho es " + str(danos.output["dano"]))
    print("")
    danoValor = danoValor - 1


# In[ ]:




