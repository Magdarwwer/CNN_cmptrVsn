import numpy as np
from scipy import stats

# Test t dla dwóch grup
group1 = np.random.normal(5, 1, 100)
group2 = np.random.normal(5.5, 1, 100)

t_stat, p_val = stats.ttest_ind(group1, group2)
print("p-value:", p_val)  # czy różnica jest istotna?
#