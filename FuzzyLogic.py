# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:04:39 2023

@author: jgutierr2
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Generate universe variables
#   * Quality and Service on subjective ranges [0, 10]
#   * Tip has a range of [0, 25] in units of percentage points
# New Antecedent/Consequent objects hold universe variables and membership
# functions
phoneRespTime = ctrl.Antecedent(np.arange(0, 11, 1), 'phoneRespTime')
operAttention = ctrl.Antecedent(np.arange(0, 11, 1), 'operAttention')
#waitTime = ctrl.Antecedent(np.arange(0, 11, 1), 'waitTime')
qualService = ctrl.Consequent(np.arange(0, 101, 10), 'qualService')

# Auto-membership function population is possible with .automf(3, 5, or 7)
phoneRespTime.automf(3)
operAttention.automf(3)
#waitTime.automf(3)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
qualService['low'] = fuzz.trimf(qualService.universe, [0, 0, 40])
qualService['medium'] = fuzz.trimf(qualService.universe, [30, 60, 80])
qualService['high'] = fuzz.trimf(qualService.universe, [70, 90, 100])

"""
To help understand what the membership looks like, use the ``view`` methods.
"""

# You can see how these look with .view()
phoneRespTime['average'].view()
"""
.. image:: PLOT2RST.current_figure
"""
operAttention.view()

#waitTime.view()
"""
.. image:: PLOT2RST.current_figure
"""
qualService.view()
"""
.. image:: PLOT2RST.current_figure


Fuzzy rules
-----------

Now, to make these triangles useful, we define the *fuzzy relationship*
between input and output variables. For the purposes of our example, consider
three simple rules:

1. If the food is poor OR the service is poor, then the tip will be low
2. If the service is average, then the tip will be medium
3. If the food is good OR the service is good, then the tip will be high.

Most people would agree on these rules, but the rules are fuzzy. Mapping the
imprecise rules into a defined, actionable tip is a challenge. This is the
kind of task at which fuzzy logic excels.
"""

rule1 = ctrl.Rule(phoneRespTime['poor'] | operAttention['poor'], qualService['low'])
rule2 = ctrl.Rule(phoneRespTime['average'], qualService['medium'])
rule3 = ctrl.Rule(phoneRespTime['good'] & operAttention['good'], qualService['high'])

rule1.view()

"""
.. image:: PLOT2RST.current_figure

Control System Creation and Simulation
---------------------------------------

Now that we have our rules defined, we can simply create a control system
via:
"""

qualService_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

"""
In order to simulate this control system, we will create a
``ControlSystemSimulation``.  Think of this object representing our controller
applied to a specific set of cirucmstances.  For tipping, this might be tipping
Sharon at the local brew-pub.  We would create another
``ControlSystemSimulation`` when we're trying to apply our ``tipping_ctrl``
for Travis at the cafe because the inputs would be different.
"""

qservice = ctrl.ControlSystemSimulation(qualService_ctrl)


qservice.input['phoneRespTime'] = 8
qservice.input['operAttention'] = 8
#qservice.input['waitTime'] = 2

# Crunch the numbers
qservice.compute()
plt.show()
"""
Once computed, we can view the result as well as visualize it.
"""
print(qservice.output['qualService'])
qualService.view(sim=qservice)

