1. fourier_emb.py:
This file implements Fourier feature embeddings, which can help neural networks better represent high-frequency functions. While not explicitly mentioned in the paper, this technique can improve the approximation capabilities of neural networks for complex value functions.
2. mlp.py:
Implements the standard multilayer perceptron (MLP) architecture that forms the backbone of the neural networks used in the paper. The paper mentions on page 5 that they use "3 layers of 256 neurons with tanh activations" for all neural networks, which is configured through this implementation.
3. ncbf.py:
Provides different value function representations, including MultiValueFn which is used in the PNCBF implementation to output values for multiple safety constraints simultaneously (handling the nh dimension mentioned in the paper). This supports the multi-constraint capabilities discussed in the experiments.
4. network_utils.py:
Contains utility functions for neural networks, including activation function selection. The paper mentions using tanh activations, which is supported through the get_act_from_str function here.
5. optim.py:
Implements the optimizer configuration, using AdamW with weight decay. While not detailed in the paper, this is a standard choice for training neural networks and supports the gradient-based learning approach mentioned in Section III.
6. pol_det.py:
Implements a deterministic policy network with tanh outputs (constrained between -1 and 1). This could be used for representing the nominal policy in the PNCBF framework.
7. train_state.py:
Provides a state management class for training neural networks, tracking parameters, optimizer state, and learning rates. This supports the training process described in Algorithm 1 of the paper.
8. block.py:
Implements neural network block architectures including residual connections. The TmpNet class mentioned in the PNCBF code uses these blocks, providing an alternate network architecture option that's not explicitly described in the paper.
9. ensemble.py:
Implements ensemble methods for neural networks, creating multiple network instances and aggregating their outputs. The paper uses ensembles implicitly when it mentions using "target networks" in the training process, particularly for stabilizing learning.