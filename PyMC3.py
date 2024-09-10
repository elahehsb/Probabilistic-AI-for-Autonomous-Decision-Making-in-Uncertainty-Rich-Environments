import pymc3 as pm
import numpy as np

# Simulating decision-making under uncertainty using MCMC
with pm.Model() as model:
    # Define priors
    success_rate = pm.Beta("success_rate", alpha=1, beta=1)
    
    # Likelihood (observations)
    observed_success = pm.Bernoulli("obs", p=success_rate, observed=[1, 0, 1, 1, 0, 1, 1, 0, 0, 1])
    
    # Posterior sampling using MCMC
    trace = pm.sample(2000, return_inferencedata=False)
    
# Summary of the posterior estimates
pm.summary(trace)
