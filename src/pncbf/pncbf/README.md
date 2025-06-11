1. pncbf.py
    +   main implementation
2. compute_disc_avoid.py
    +   discounted policy value function calculation described in 
        Section III.C of the paper. It handles the computation of the 
        maximum-over-time cost function with discounting (λ).
    +   This addresses the "Discounting and Contraction" aspect mentioned 
        in the paper, which helps prevent undesirable trivial solutions 
        during training.
3. min_norm_cbf.py
    +   implements the quadratic program (QP) for the safety filter described in 
        equation (5) of the paper. It creates the safety filter that minimally 
        modifies the nominal control input to ensure safety.
4. stateful_dset_buffer.py
    +   this represents the implementation of the data collection process 
        mentioned in Algorithm 1 of the paper, where tuples of states and maximum 
        constraint values are collected.