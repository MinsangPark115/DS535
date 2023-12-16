# DS535 Project
## Conditional Diffusion Recommender Model
by Minsang Park, Ghwanghyun Lee, Sumin Lee, Jongbok Lee

## Environment
python 3.8, CUDA 11.1

## Training
In first tab, there is code for installing packages with requirements_for_cuda111.txt. 
You can install packages in your environment with that code

You can train your model with run one of this codes

  * Conditional Diffusion Recommender Model.ipynb
  * Conditional Diffusion Recommender Model_sig.ipynb

When you open the file, you have to modify below term

############ Change this term for your input dataset ############

numofcluster = 5               
* 5 or 10
* change this as number of cluster that your input data have


clustertype = "1st"            
* "1st" or "2nd"
* change this as type of cluster that your input data have

path = "./data/"

filename1 = path + f"ml_1m_user_mov_{clustertype}_cluster={numofcluster}.csv" 
* change this with input data name

new_data = pd.read_csv(filename1)

#######################################################

after training step, your "main" trained checkpoint is in 
* ./trained_ckpt/model_1m_{clustertype}={numofcluster}.ckpt

Your Autoencoder or VAE trained checkpoint is in 
* ./trained_ckpt/model_1m_{clustertype}={numofcluster}_AE{key}.ckpt

## Sampling
You can sample with this code

  * sampling.ipynb

When you open the file, you have to modify below term

############ Change this term for your input dataset ############

numofcluster = 5               
* 5 or 10
* change this as number of cluster that your input data have

clustertype = "1st"
* "1st" or "2nd"
* change this as type of cluster that your input data have

ckptname = f"model_1m_{clustertype}={numofcluster}_sig"  
* change this as xxxx when your "main" ckpt name is xxxx.ckpt

mode = "sig"
* "sig" or "nosig"
* if your autoencoder use sigmoid layer in training step, write sig, else anything.

path = "./data/"

filename1 = path + f"ml_1m_user_mov_{clustertype}_cluster={numofcluster}.csv" 
* change this with input data name

new_data = pd.read_csv(filename1)

#######################################################

after sampling step, your sample is saved in 
* ./{ckptname}_sample.csv
