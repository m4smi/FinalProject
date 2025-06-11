1. dyn_types.py:
Defines type annotations for different state, control, and observation variables to ensure type safety throughout the codebase. These custom types help track dimensions and maintain consistency in the code.

2. f16_gcas.py: The 16-dimensional jet aircraft model (F-16) used in Section IV.B

3. segway.py: The Segway model used in Section IV.A
quadcircle.py: The two-agent quadcopter system with obstacle avoidance from Section IV.C and V

4. doubleint_wall.py: The double integrator with obstacles (simplest test case)

5. angle_encoder.py:
Handles the encoding of angular states (like theta in the Segway) using sine/cosine representations, which improves learning for periodic states.

6. odeint.py: Provides Runge-Kutta and other ODE solvers

7. sim_cts.py: Handles continuous-time simulation of dynamical systems

8. sim_cts_pbar.py: Similar to sim_cts but with a progress bar for longer simulations

9. task.py:
Defines the abstract base class that all dynamical systems inherit from. It specifies the interface for dynamics, constraint functions, plotting, and other core functionality needed for the PNCBF approach.