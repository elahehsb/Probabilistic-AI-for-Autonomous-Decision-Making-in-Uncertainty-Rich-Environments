import torch
from syft.frameworks.torch.dp import pate

# Example data
teacher_outputs = torch.Tensor([[0.6, 0.4], [0.8, 0.2], [0.55, 0.45]])
indices = torch.Tensor([0, 1, 0])

# Apply differential privacy using the PATE algorithm
student_votes, _ = pate.perform_analysis(teacher_outputs, indices, noise_eps=0.1)
print("Votes after applying differential privacy:", student_votes)
