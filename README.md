This repo is for ECE 228 Final Project (2025)

The PNCBF paper use a complex setup with JAX/CUDA dependencies and ROS-related packages. 

For this project reproducibility, I recommend using a Linux distro and install the exact environment that was used to produce this project via Conda (cbf310_linux.yml).\
I also included a Windows version and a requirements.txt (but this is not guarantee to work).

#-----------------Environment \
CondaEnv: Contains the environment setup required to run the project. \
\
#-----------------src (.ipynb files)
1. data_collection_segway: generate dataset.
2. mlp_train: original MLP architecture.
3. attention_train: multi-head attention model.
4. model_comparison: systematic comparison between MLP vs. Attention.