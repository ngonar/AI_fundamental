import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#antecedent
quality = ctrl.Antecedent(np.arange(0,11,1), 'quality')
service = ctrl.Antecedent(np.arange(0,11,1), 'service')
tip = ctrl.Antecedent(np.arange(0,26,1), 'tip')

#membership function
quality.automf(3)
service.automf(3)

#custom membership function
tip['low'] = fuzz.trimf(tip.universe, [0,0,13])
tip['medium'] = fuzz.trimf(tip.universe, [0,13,25])
tip['high'] = fuzz.trimf(tip.universe, [13,25,25])
