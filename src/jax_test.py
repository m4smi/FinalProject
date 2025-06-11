# try:
#     from pncbf.dyn.doubleint_wall import DoubleIntWall
#     print("Import successful!")
#     system = DoubleIntWall()
#     print(f"State dimension: {system.nx}")
# except Exception as e:
#     print(f"Import failed with error: {e}")

# test_jax.py
# import jax
# import jax.numpy as jnp
# try:
#     # jax.config.update("jax_platform_name", "cpu")
#     print("JAX version:", jax.__version__)
#     # Test a simple JAX operation
#     x = jnp.ones((3, 3))
#     y = jnp.ones((3, 3))
#     z = jnp.dot(x, y)
#     print("JAX matrix multiplication test passed!")
# except Exception as e:
#     print(f"Error: {e}")
import jax
import jax.numpy as jnp
import jax.random as jrd
print('JAX version:', jax.__version__); print('Available devices:', jax.devices())
rng = jrd.PRNGKey(0)
x = jrd.truncated_normal(rng, -1, 1, (100000,))
kernel = jrd.truncated_normal(rng, -1, 1, (1000, 100000))
y = jnp.matmul(kernel, x)
print(f"y is: \n{y}")