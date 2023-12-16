# DS535 Project
## Conditional Diffusion Recommender Model
Minsang Park, Ghwanghyeon Lee, Sumin Lee, Jongbok Lee

## Environment
python 3.8, CUDA 11.1

## Training

### 1. Install Packages
In first tab, there is code for installing packages with "requirements_for_cuda111.txt."

You can install packages in your environment with that code

### 2. Training Code
You can train your model with run one of this codes

  * Conditional Diffusion Recommender Model_AE.ipynb
  * Conditional Diffusion Recommender Model_AE_sig.ipynb

For VAE version,

  * Conditional Diffusion Recommender Model_VAE.ipynb
  * Conditional Diffusion Recommender Model_VAE_sig.ipynb


### 3. Modification
When you open the file, you have to modify below term
![Training](https://i.ibb.co/Z8SDXCD/image.png)

* numofcluster               
  * 5 or 10
  * change this as number of cluster that your input data have

* clustertype            
  * "1st" or "2nd"
  * change this as type of cluster that your input data have

* filename1
  * change this with input data name

After modification, you can run code

### 4. Checkpoint Save
After training step, your trained "main" checkpoint is in 
* ./trained_ckpt/model_1m_{clustertype}={numofcluster}.ckpt

Your trained Autoencoder checkpoint is in 
* ./trained_ckpt/model_1m_{clustertype}={numofcluster}_AE{key}.ckpt

For VAE version,
* ./trained_ckpt/model_1m_{clustertype}={numofcluster}.ckpt

Your trained VAE checkpoint is in 
* ./trained_ckpt/model_1m_{clustertype}={numofcluster}_VAE{key}.ckpt

## Sampling
### 0. Trained checkpoint
Because of size of file, we cannot upload checkpoint that we used.

If you want to get, contact to Minsang Park (pagemu@kaist.ac.kr)

### 1. Sampling Code
You can sample with this code

  * sampling.ipynb

For VAE version,

  * sampling_VAE.ipynb

### 2. Modification
When you open the file, you have to modify below term

![Sampling](https://i.ibb.co/pQFVGfD/2.png)
* numofcluster               
  * 5 or 10
  * change this as number of cluster that your input data have

* clustertype            
  * "1st" or "2nd"
  * change this as type of cluster that your input data have

* ckptname 
  * change this as "xxxx" when your "main" ckpt name is "xxxx.ckpt"

* mode = "sig"
  * "sig" or "nosig"
  * if your autoencoder use sigmoid layer in training step, write sig, else anything.

* filename1
  * change this with input data name

After modification, you can run code

### 3. Sample Save
After sampling step, your sample is saved in 
* ./{ckptname}_sample.csv

## Evaluation
You can evaluate your samples with

* Evaluation/metrics.py
* Evaluation/main.py
* raw_data.csv

If you want to run evaluation code, put your sample csv in 
* evaluation/test/YOURSAMPLE.csv

After that,

```.bash
python main.py
```
