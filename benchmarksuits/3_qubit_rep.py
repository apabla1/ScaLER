from scalerqec.QEC.qeccircuit import QECStab
from scalerqec.Monte.monteLER import stimLERcalc
from scalerqec.Stratified.stratifiedScurveLER import stratified_Scurve_LERcalc
from scalerqec.Symbolic.symbolicLER import symbolicLER
from scalerqec.QEC.noisemodel import NoiseModel

n = 3
k = 1
d = 3
qeccirc= QECStab(n=n,k=k,d=d)

# Repetition code stabilizers
qeccirc.add_stab("ZZI")
qeccirc.add_stab("IZZ")

# Logical operators
qeccirc.set_logical_Z(0, "ZZZ")

# Stabilizer parity measurement scheme & round of repetition
qeccirc.scheme="Standard"
qeccirc.rounds=2

qeccirc.construct_circuit()
#qeccirc.show_IR()

# Export to temporary stim file
import tempfile
stim_circuit = qeccirc.stimcirc
stim_str = str(stim_circuit)
tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".stim", delete=False)
tmp.write(stim_str)
tmp.flush()
stim_path = tmp.name
tmp.close()

# Error model
p = 0.001
noise_model = NoiseModel(p)

### (1) MC
print("---------Monte-Carlo Logical-Z LER---------")
calc = stimLERcalc(MIN_NUM_LE_EVENT=100)
calc.calculate_LER_from_QECircuit(qeccirc, noise_model, repeat=3)

# ### (2) Stratified
# print("---------Stratified Logical-Z LER---------")
# t = (d - 1) // 2
# samplebudget = 100_000
# est = stratified_Scurve_LERcalc(error_rate=p, sampleBudget=samplebudget, k_range=5, num_subspace=6, beta=4)
# est.set_t(t)
# est.set_sample_bound(MIN_NUM_LE_EVENT=100, SAMPLE_GAP=100, MAX_SAMPLE_GAP=5000, MAX_SUBSPACE_SAMPLE=50_000)
# est.calculate_LER_from_file(stim_path, p, codedistance=3, figname="5q", titlename="5-qubit", repeat=1)

### (3) Symbolic
print("---------Symbolic Logical-Z LER---------")
sym = symbolicLER()        
ler = sym.calc_LER_of_QECircuit(qeccirc, noise_model)
print("Symbolic Logical-Z LER =", ler)