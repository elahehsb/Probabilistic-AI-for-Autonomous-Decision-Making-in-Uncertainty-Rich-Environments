import pyro
import pyro.distributions as dist
from pyro.infer import SVI, Trace_ELBO
from pyro.optim import Adam
import torch

# Simple probabilistic model for decision-making under uncertainty
def probabilistic_model():
    # Prior belief about a parameter (e.g., the success rate of an action)
    success_rate = pyro.sample("success_rate", dist.Beta(1, 1))  # Beta distribution

    # Likelihood of observing a success based on the true success rate
    with pyro.plate("observations", 10):  # Assume we have 10 observations
        observed_success = pyro.sample("obs", dist.Bernoulli(success_rate), obs=torch.tensor([1., 0., 1., 1., 0., 1., 1., 1., 0., 1.]))
    
    return success_rate

# Guide (variational approximation to the posterior)
def guide():
    alpha_q = pyro.param("alpha_q", torch.tensor(1.0), constraint=dist.constraints.positive)
    beta_q = pyro.param("beta_q", torch.tensor(1.0), constraint=dist.constraints.positive)
    pyro.sample("success_rate", dist.Beta(alpha_q, beta_q))

# Variational inference using SVI (Stochastic Variational Inference)
optimizer = Adam({"lr": 0.01})
svi = SVI(probabilistic_model, guide, optimizer, loss=Trace_ELBO())

# Training loop
for step in range(1000):
    loss = svi.step()
    if step % 100 == 0:
        print(f"Step {step} : Loss = {loss}")

# Estimated success rate
alpha_q = pyro.param("alpha_q").item()
beta_q = pyro.param("beta_q").item()
print(f"Estimated success rate: {alpha_q / (alpha_q + beta_q)}")
