# DS535 Project
## Conditional Diffusion Recommender Model
by Minsang Park, Ghwanghyun Lee, Sumin Lee, Jongbok Lee

## Environment
python 3.8, CUDA 11

## Training
You can train your model with run one of this codes

  * Conditional Diffusion Recommender Model.ipynb
  * Conditional Diffusion Recommender Model_sig.ipynb

When you open the file, you have to modify below term

############################### Change this term for your input dataset ###############################

numofcluster = 5               
* change this as number of cluster that your input data have : 5 or 10

clustertype = "1st"            
* change this as type of cluster that your input data have " 1st or 2nd

path = "./data/"

filename1 = path + f"ml_1m_user_mov_{clustertype}_cluster={numofcluster}.csv" 
          change this with input data name

new_data = pd.read_csv(filename1)

#######################################################################################################

after training step, your trained checkpoint is in ./trained_ckpt

## Sampling
You can sample with this code

  sampling.ipynb

When you open the file, you have to modify below term

############################### Change this term for your input dataset ###############################

numofcluster = 5               
          change this as number of cluster that your input data have : 5 or 10

clustertype = "1st"
          change this as type of cluster that your input data have " 1st or 2nd

ckptname = f"model_1m_{clustertype}={numofcluster}_sig"  
          change this as xxxx when your "main" ckpt name is xxxx.ckpt

mode = "sig"
          if your autoencoder use sigmoid layer in training step, write sig, else anything.

path = "./data/"

filename1 = path + f"ml_1m_user_mov_{clustertype}_cluster={numofcluster}.csv" 
          change with training data

new_data = pd.read_csv(filename1)

#######################################################################################################
