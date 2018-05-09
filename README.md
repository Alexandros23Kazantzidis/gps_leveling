# gps_leveling


A software - GUI that we build along with the other students at the Geoinformatics Msc of Aristotle University of Thessaloniki

*How to run*

1. Install Python 3.5
2. Install git
3. git clone https://github.com/Alexandros23Kazantzidis/gps_leveling.git
4. open terminal/cmd and cd to your local - cloned repo
5. pip install -r requirements.txt
6. run python3 main.py

*How to use the GUI*

First, you have to input the 4 data sets we need which are
φ,λ - H,σΗ - h,σh - N,σN (where σ means the accuracy - covariance matrix of the data)
You can also input the cutoff error for the gravity model you have used for N data

Then, you continue by choosing one of the 4 models supported by the current program

Finally, press the Calculate Estimation button and the program will run and output
i) The parameters of the model
ii) One graph displaying the correction surface produced by the model
iii) One graph showing the initial differences (h-H-N) and the estimation errors after
a cross validation process
iv) A results.csv file containing the Model parameters, Initial and After Least Squares
Differences and Statistics for these Differences



[![Build Status](https://travis-ci.org/Alexandros23Kazantzidis/gps_leveling.svg?branch=master)](https://travis-ci.org/Alexandros23Kazantzidis/gps_leveling)
