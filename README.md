# NEU-365P-385L-Spring-2022
Programming and Data Analysis for Modern Neuroscience, Spring 2022

:warning: **!!! THINGS TO DO PRIOR TO THE FIRST CLASS**.

## Course Objective

*The ability to read and write are obvious fundamental skills critical to all academic and quantitative pursuits.* **Fast approaching this level of fundamental importance is the ability to write computer programs to analyze and manipulate data sets ever increasing in richness and size.** This skillset is necessary to work with a wide array of systems whose models and behavior are sufficiently complex to make analysis by hand intractable.

**In this course you will translate problems into code applying modern approaches for data analysis, statistical inference and modeling to various levels of neural systems and their component behavior.** We will use Python as a coding environment, and you will be exposed to resources and options for scientific computing.
 
 *Although geared for neuroscience, the approaches covered in this course are highly salient for a wide array of applications.*
 
 ## Breadth over Depth
 
We will cover a wide array of topics rather than explore any one topic in great detail. Topics will be introduced at a level where you should be able to understand each concept and put them to use. However, realize up front that we may have only scratched the surface.

*The goal of the course is to give you enough of a basic toolset that you will have the necessary foundation to develop programs for any concept that you understand.*

## Course Prerequisites

There are no prerequisites for the course. *However, you are expected to be familiar with basic mathematical functions and concepts, and you will be asked to perform quantitative calcualtions.*

## Requirements

* You must bring a laptop to class for hands on participation. If you do not own a laptop, contact your department or the College of Natural Sciences to obtain a loaner for the duration of the course.
* Install Python on the laptop you will bring to class (see instructions below).
* Attend class both motivated and prepared to work hard!
* Conduct yourself in a respectful manner at all times.
* Have fun!

## Course Details

* Time: TBA
* Location: TBA
* Instructor: Marcel Goldschen-Ohm
    * Office hours (zoom only): TBA (see Canvas announcement for Zoom link)
    * Email: goldschen-ohm@utexas.edu (**!!! Please include `neu365-2022` or `neu385-2022` in the subject line**)
* TA: TBA
    * Office hours (zoom only): TBA (see Canvas announcement for Zoom link)
    * Email: TBA (**!!! Please include `neu365-2022` or `neu385-2022` in the subject line**)
 
## I'm confused, but my schedule makes attending office hours difficult. What do I do?

**!!! POST YOUR QUESTIONS ON CANVAS** where either myself or your fellow students can help. I may not reply immediately as advice from fellow students can often be the most illuminating.

## Academic Integrity

It is perfectly fine to work with your fellow students or anyone else on the homework assignments. If you do so, please include a note on your assignment indicating with whom you collaborated. Any academic dishonesty such as copying a fellow students assignment without collaborating in its completion will be severly punished as outlined by the University. **Most importantly, the ability to solve problems such as those in the homeworks is exactly the skillset you are here to obtain.** By not practicing these skills, you are primarily hurting yourself.

## Inclusion

Along with the entire Department of Neuroscience, this course embraces a notion of an intellectual community enriched and enhanced by diversity along a number of dimensions, including race, ethnicity and national origins, gender and gender identity, sexuality, class, ability level, and religion. We are especially committed to fostering an environment where you feel heard and respected in your courses.

## Policies

* Students with disabilities may request appropriate academic accommodations from the Division of Diversity and Community Engagement, [Services for Students with Disabilities](http://www.utexas.edu/diversity/ddce/ssd/) (471-6259).

## Grading

TBA

## Homework

Most homework will be in the form of Jupyter notebooks. Homework assignments will be posted on Canvas where you will be required to upload the completed notebook file. :warning: **Be sure to name the file `your_full_name.ipynb`.** :warning: **All homework is due by midnight on the due date**. Note that uploading to Canvas can sometimes be less than instantaneous, so DON'T WAIT UNTIL ONE MINUTE BEFORE MIDNIGHT ON THE DEADLINE TO SUBMIT. Late homework is NOT acceptable.

* Python basics
* NumPy arrays and plotting
* Random walks
* Pseudocode and algorithm
* Bootstrap
* Permutation test
* Maximum Likelihood Estimation
* Time series and filtering
* Hidden Markov Model
* Linear regression
* Ridge or lasso regression
* Nonlinear regression
* Classification and clustering
* Principal Component Analysis
* Neural Network

## Syllabus

* Course overview and introduction to the Python and Jupyter notebook ecosystem
* Python basics
* NumPy data arrays
* Visualizing data and Pandas data tables
* Random walk lab
* Random walk lab 2
* Functions, classes and modules
* Pseudocode and optimization with Numba
* Probability distributions of random variables and the Central Limit Theorem
* Hypothesis testing, p-values and Bootstrap confidence intervals
* Permutation test
* Maximum Likelihood Estimation
* Curve fitting
* Time series, Fourier transform and filtering
* Convolution and filtering
* Hidden Markov Models
* Hidden Markov Model lab
* Midterm Exam
* Linear regression
* Ridge and lasso regression
* Cross validation
* Nonlinear regression
* General Linear Models
* Regression lab
* Classification and clustering
* Principal Component Analysis
* Principal Component Analysis lab
* Neural Networks
* Neural Network lab
* Deep Learning
* Final Exam

## Install Python (required)
1. Get the Anaconda Python distribution (**latest version 3.x**) from https://www.anaconda.com/download and just follow the install steps. Anaconda comes with a bunch of useful scientific libraries such as Numpy and Scipy that you would otherwise have to install yourself.
2. **[Hopefully this step is no longer necessary, but I'll leave these instructions just in case.]** !!! MacOS Catalina ONLY !!! If you are running MacOS Catalina, you might run into this problem: Anaconda creates a `.bash_profile` file in your home directory that needs to be renamed to `.zprofile` in Catalina (does NOT apply to older versions of MacOS).
3. Launch Anaconda Navigator. Install JupyterLab and Spyder via the widgets in the Home tab. JupyterLab is a web-based python notebook and Spyder is an environment for running Python that is similar to MATLAB.

## Install R (optional)
1. Get R from https://cran.revolutionanalytics.com/index.html and run the installer.
2. Get RStuio Desktop from https://www.rstudio.com/. This is an environment for running R that is similar to MATLAB.

## Install Julia (optional)
I recommend just following the instructions at https://docs.junolab.org/latest/man/installation/. Get the latest stable release. I also recommend installing the Atom editor and Juno IDE.

## Install MATLAB (optional)
UT students have free access to MATLAB.

1. Go to www.mathworks.com and create a user account. **Your username MUST be your UT email address!**
2. Go to [UT Service Now](https://ut.service-now.com/utss/catalogoverview.do?sysparam_citems_id=f9d65c7c4ff9d200f6897bcd0210c77d&sysparam_cat_id=e0d08b13c3330100c8b837659bba8fb4,Information%20Technology&sys_click_name=features&sys_features=1) and request MATLAB. **Click the Request button in the MATLAB for Students Only box near the bottom of the page.** Your request may take a day or two to process, so don't delay.
3. Sign in to your mathworks account and you should see a license from UT is available to you. Use that license to download MATLAB (latest version). Then run the installer. If you can afford the space (>20 GB) *get all the toolboxes that you can*. If not, *get at least those toolboxes listed at https://www.mathworks.com/products.html under the MATLAB product family sections 'Math, Statistics, and Optimization', 'Signal Processing', 'Image Processing' and 'Computational Biology'.*

Note, once you've registered you can also use MATLAB via an online interface that mimicks the application environment at https://matlab.mathworks.com.

## Install GitHub Desktop (optional)
1. Go to https://github.com and create an account if you don't already have one.
2. Go to https://desktop.github.com and download the GitHub Desktop app.
3. Open the app and select File->Clone Repository. Select URL and enter the URL of this repository (https://github.com/marcel-goldschen-ohm/NEU-365P-385L-Spring-2021), then click 'Clone'. This will download all of the files in this repository to a folder on your computer. To navigate to the folder from GitHub Desktop select Repository->Show in Finder (that's for MacOS, wording may differ on Windows machines).
4. Whenever you want to make sure that you have the latest version of all files in the repository, select Repository->Pull to download ONLY what has changed since the last time you downloaded the repository.
5. *To make sure you do not overwrite any homework assignment files, I recommend copying all of the homeworks into a separate folder on your computer rather than editing the files directly in the GitHub repository folder.*

## Resources
* [Python Challenges](http://www.pythonchallenge.com): Fun! Will test your Python skills.
* [Computational and Inferential Thinking](https://www.inferentialthinking.com): Quick course on statistics and Python with examples. **This is a good place to start.**
* [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook): Explanations and examples. **This is also a good first learning tool.**
* [Computational Statistics in Python](http://people.duke.edu/~ccc14/sta-663-2017): Great collection of references with examples. Highly recommend! **Mostly for reference and code examples, but they're very useful.**
* [Statistics Done Wrong](https://www.statisticsdonewrong.com): **MUST READ!!!**
* [Modern Machine Learning Algorithms: Strengths and Weaknesses](https://elitedatascience.com/machine-learning-algorithms) Breif overview of some machine learning algorithms with strengths and weaknesses to put them in context.
* [An Introduction to Statistical Learning](https://www-bcf.usc.edu/~gareth/ISL/ISLR%20First%20Printing.pdf): Nice intro to fairly complex statistical methods with very little math. **Highly recommend!** Example code is in R, but explanations are helpful in general. Note that this is a bit longer and more indepth than the options above. **This is more about understanding statistical methods than coding.**
