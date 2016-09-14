import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import scipy.special

rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc)

#Load data
wt_lac = np.loadtxt('data/wt_lac.csv', skiprows=3, delimiter=',')
q18a_lac = np.loadtxt('data/q18a_lac.csv', skiprows=3, delimiter=',')
q18m_lac = np.loadtxt('data/q18m_lac.csv', skiprows=3, delimiter=',')

# Slice out IPTG and fold change
iptg_wt = wt_lac[:,0]
fc_wt = wt_lac[:,1]
iptg_q18a = q18a_lac[:,0]
fc_q18a = q18a_lac[:,1]
iptg_q18m = q18m_lac[:,0]
fc_q18m = q18m_lac[:,1]

# Plot fold change
plt.semilogx(iptg_wt, fc_wt, linestyle='none', marker='.', markersize=20)
plt.semilogx(iptg_q18a, fc_q18a, linestyle='none', marker='.', markersize=20)
plt.semilogx(iptg_q18m, fc_q18m, linestyle='none', marker='.', markersize=20)
plt.legend(('wt', 'q18a', 'q18m'), loc='upperright')

plt.xlabel('log[IPTG(mM)]')
plt.ylabel('GFP expression')
plt.title('Fold Change')
plt.show()
plt.close()

# Define variables for theoretical fold change
R = np.array([141.5, 16.56, 1332])
KdA = 0.017
KdI = 0.002
Kswitch = 5.8

# Theoretical fold change
def fold_change(c, R, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Compute theoretical fold change
    """
    fKdA = (1 + c/KdA)**2
    fKdI = (1 + c/KdI)**2

    y = (1 + ((R*fKdA)/(fKdA + Kswitch*fKdI)))**-1

    return y

# Using the fucking function
fc_iptg_wt = fold_change(iptg_wt, R[0])
fc_iptg_q18a = fold_change(iptg_q18a, R[1])
fc_iptg_q18m = fold_change(iptg_q18m, R[2])

# Plot fold change
plt.semilogx(iptg_wt, fc_iptg_wt, linestyle='none', marker='.', markersize=20)
plt.semilogx(iptg_q18a, fc_iptg_q18a, linestyle='none', marker='.', markersize=20)
plt.semilogx(iptg_q18m, fc_iptg_q18m, linestyle='none', marker='.', markersize=20)
plt.legend(('wt', 'q18a', 'q18m'), loc='upperright')

plt.xlabel('log[IPTG(mM)]')
plt.ylabel('GFP expression')
plt.title('Fold Change')
plt.show()
plt.close()


# Use logspace
wt_ls = np.logspace(start=-6, stop=2, 400)
fc_wt_ls = fold_change((wt_ls), R[0])
q18a_ls = np.logspace(start=-6, stop=2, 400)
fc_q18a_ls = fold_change((q18a_ls), R[0])
q18m_ls = np.logspace(start=-6, stop=2, 400)
fc_q18m_ls = fold_change((q18m_ls), R[0])

# Plot fold change
plt.plot(wt_ls, fc_wt_ls, linestyle='none', marker='.', markersize=20)
plt.plot(q18a_ls, fc_q18a_ls, linestyle='none', marker='.', markersize=20)
plt.plot(q18m_ls, fc_q18m_ls, linestyle='none', marker='.', markersize=20)
plt.legend(('wt', 'q18a', 'q18m'), loc='upperright')
plt.xlabel('log[IPTG(mM)]')
plt.ylabel('GFP expression')
plt.title('Fold Change')
plt.show()
plt.close()


# Define Bohr parameter
def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Compute Bohr parameter
    """
    w = -ln(R)-(1 + ((R*fKdA)/(fKdA + Kswitch*fKdI)))

    return w

# Using the fucking function bohr_parameter
bp_iptg_wt = fold_change(iptg_wt, R[0])
bp_iptg_q18a = fold_change(iptg_q18a, R[1])
bp_iptg_q18m = fold_change(iptg_q18m, R[2])


# Define fold change as Bohr parameter
def fold_change_bohr(bohr_parameter):
    """
    Compute the fucking fold change based on Bohr parameter
    """
    z = 1/(1+e**-w)

    return z

# Using the fucking function fold_change_bohr
fcb_iptg_wt = fold_change(bp_iptg_wt, R[0])
fcb_iptg_q18a = fold_change(bp_iptg_q18a, R[1])
fcb_iptg_q18m = fold_change(bp_iptg_q18m, R[2])

# Plot fold change
plt.semilogx(bp_iptg_wt, fcb_iptg_wt, linestyle='none', marker='.', markersize=20)
plt.semilogx(bp_iptg_q18a, fcb_iptg_q18a, linestyle='none', marker='.', markersize=20)
plt.semilogx(bp_iptg_q18m, fcb_iptg_q18m, linestyle='none', marker='.', markersize=20)
plt.legend(('wt', 'q18a', 'q18m'), loc='upperright')
plt.plot(x, cdf_high, color='gray')
plt.xlabel('log[IPTG(mM)]')
plt.ylabel('GFP expression')
plt.title('Fold Change')
plt.show()
plt.close()
