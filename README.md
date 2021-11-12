# NEU-365P-385L-Spring-2022
Programming and Data Analysis for Modern Neuroscience, Spring 2022

:warning: **!!! INSTALL Python 3.x and Jupyterlab PRIOR TO THE FIRST CLASS !!!**. See the installation instructions near the end of this document.

## Course Objective

*The ability to read and write are obvious fundamental skills critical to all academic and quantitative pursuits.* **Fast approaching this level of fundamental importance is the ability to write computer programs to analyze and manipulate data sets ever increasing in richness and size.** This skillset is necessary to work with a wide array of systems whose models and behavior are sufficiently complex to make analysis by hand intractable.

**In this course you will translate problems into code applying modern approaches for data analysis, statistical inference and modeling to various levels of neural systems and their component behavior.** We will use Python as a coding environment, and you will be exposed to resources and options for scientific computing.
 
 *Although geared for neuroscience, the approaches covered in this course are highly salient for a wide array of applications.*
 
 ## Breadth over Depth
 
We will cover a wide array of topics rather than explore any one topic in great detail. Topics will be introduced at a level where you should be able to understand each concept and put them to use. However, realize up front that we may have only scratched the surface.

*The goal of the course is to give you enough of a basic toolset that you will have the necessary foundation to develop programs for any concept that you understand.*

## Course Prerequisites

There are no prerequisites for the course. *However, you are expected to be familiar with basic mathematical functions and concepts, and you will be asked to perform quantitative calculations.*

## Requirements

* You must bring a laptop to class for hands on participation. If you do not own a laptop, contact your department or the College of Natural Sciences to obtain a loaner for the duration of the course.
* Install Python on the laptop you will bring to class (see instructions below).
* Attend class both motivated and prepared to work hard!
* Conduct yourself in a respectful manner at all times.
* Have fun!

## Course Details

* Time: TTH 2:00-3:30 PM
* Location: BUR 208
* Instructor: Marcel Goldschen-Ohm
* TA: TBA
* Office hours (Zoom only): See Canvas announcement.
* Contact: Please contact myself or the TA via Canvas. (!!! If you email me directly, please include `neu365-2022` or `neu385-2022` in the subject line)
 
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

Most homework will be in the form of Jupyter notebooks. Homework assignments will be posted on Canvas where you will be required to upload the completed notebook file. :warning: **Be sure to include your full name in the filename of each of your assignments (e.g. `assignment-your_full_name.ipynb`).** :warning: **All homework is due by midnight on the due date**. Note that uploading to Canvas can sometimes be less than instantaneous, so DON'T WAIT UNTIL ONE MINUTE BEFORE MIDNIGHT ON THE DEADLINE TO SUBMIT. Late homework is not acceptable.

* Python basics
* Random walks
* Algorithms
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

Note that the syllabus is subject to change at anytime, so check back often. This is so I can offer you a more polished experience by adjusting to your performance and feedback as we go along.

Below each topic I've listed a few links to additional information. If you happen to know of a particularly good resource that is not listed, please let me know about it and share it with your fellow students on the course's Canvas discussion board.

* Jan-18-T: Course overview and introduction to the Python and Jupyter ecosystem
    * Install [Python and Conda](https://docs.conda.io/en/latest/miniconda.html) (see instructions at bottom of page)
    * `conda install -c conda-forge jupyterlab`
    * Additional Resources: [What can I do with Python?](https://realpython.com/what-can-i-do-with-python/), [Miniconda](https://docs.conda.io/en/latest/miniconda.html), [Intro to Jupyter and JupyterLab](https://coderefinery.github.io/jupyter/)
* Jan-20-R: Python basics
    * Additional Resources: [Python beginner tutorials](https://www.tutorialsteacher.com/python), [Python basics](https://www.learnpython.org), [The Hitchhiker's Guide to Python](https://docs.python-guide.org/intro/learning/), [More Python tutorials](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers), [Python Tutor](https://pythontutor.com).
* Jan-25-T: NumPy data arrays and basic plotting
    * `conda install numpy`
    * `conda install matplotlib`
    * Additional Resources: [NumPy](https://numpy.org), :star:[A visual intro to NumPy](https://jalammar.github.io/visual-numpy/), [Matplotlib](https://matplotlib.org)
* Jan-27-R: Random walk lab
    * Additional Resources: [Diffusion and random walks](https://www.uio.no/studier/emner/matnat/fys/FYS2160/h17/simuleringsopgaver/virrevandrer_diffusjon.pdf)
* Feb-01-T: Visual data exploration and Pandas data tables
    * `conda install pandas`
    * `conda install seaborn`
    * `conda install -c conda-forge dtale`
    * `conda install -c conda-forge pandasgui`
    * Additional Resources: [Intro to Pandas](https://pandas.pydata.org/docs/getting_started/index.html), [Seaborn](https://seaborn.pydata.org), [D-Tale](https://github.com/man-group/dtale), [D-Tale tutorial](https://www.analyticsvidhya.com/blog/2021/06/exploring-pandas-dataframe-with-d-tale/), [PandasGUI](https://github.com/adamerose/PandasGUI), [PandasGUI tutorial](https://www.analyticsvidhya.com/blog/2021/07/everything-you-need-to-know-about-pandasgui/), [Kaggle database](https://www.kaggle.com)
* Feb-03-R: Exploratory data analysis lab
* Feb-08-T: Functions, classes and modules
* Feb-10-R: Algorithms, pseudocode, and optimization with Numba
     * `conda install numba`
     * Additional Resources: [Numba](http://numba.pydata.org)
* Feb-15-T: Probability distributions of random variables and the Central Limit Theorem
    * `conda install scipy`
    * Additional Resources: [SciPy](https://scipy.org)
* Feb-17-R: Minimization and Maximum Likelihood Estimation
* Feb-22-T: Hypothesis testing, p-values, confidence intervals, and bootstrapping
* Feb-24-R: Permutation test, K-S test, and QQ plots
* Mar-01-T: Time series, Fourier transform and filtering
* Mar-03-R: Convolution, filtering and image analysis
* Mar-08-T: Hidden Markov Models
* Mar-10-R: Hidden Markov Model lab
* Mar-15-T: SPRING BREAK
* Mar-17-R: SPRING BREAK
* Mar-22-T: Linear regression
* Mar-24-R: Ridge and lasso regression
* Mar-29-T: Cross validation
* Mar-31-R: Nonlinear regression
* Apr-05-T: General Linear Models
* Apr-07-R: Regression lab
* Apr-12-T: Classification
* Apr-14-R: Clustering
* Apr-19-T: Principal Component Analysis
* Apr-21-R: Principal Component Analysis lab
* Apr-26-T: Neural Networks
* Apr-28-R: Neural Network lab
* May-03-T: Deep Learning
* May-05-R: Deep Learning lab
* May-11-W: Final Exam 9:00 am-12:00 noon

## Install Python (required)

This is not the only way to install and/or manage your Python environment, but it is the method I recommend for this course.

1. Download and install Miniconda from https://docs.conda.io/en/latest/miniconda.html. Choose the latest version of Python 3. Miniconda installs the conda package manager which manages all of your Python packages. It comes with a minimal set of basic packages, but there are also additional packages that we will need for this course. I will walk you through installing most of those packages as they are needed, but there are a few that you should install right away (see next steps).
2. Install JupyterLab. After you have installed Miniconda you should now be able to use the `conda` command in a Terminal (MacOS), shell (Linux), or command prompt (Windows). Run the command `conda install -c conda-forge jupyterlab` by typing it into your command line interface and pressing Return or Enter. This will install the JupyterLab package which is the user interface environment in which we will be spending most of our time. You can test whether this worked by running the command `jupyter-lab` which should open up a page in your web browser with the JupyterLab user interface.

Here are a few more packages that we will definitely be needing.

3. Install NumPy: Run the command `conda install numpy`
4. Install Pandas: Run the command `conda install pandas`
5. Install Matplotlib: Run the command `conda install matplotlib`

We'll be installing more packages as we go, but the above are some basic packages for data analysis. 

## Resources
* [Python Beginner Basics](https://www.tutorialsteacher.com/python)
* [Python Challenges](http://www.pythonchallenge.com): Fun! Will test your Python skills.
* [Computational and Inferential Thinking](https://www.inferentialthinking.com): Quick course on statistics and Python with examples. **This is a good place to start.**
* [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook): Explanations and examples. **This is also a good first learning tool.**
* [Computational Statistics in Python](http://people.duke.edu/~ccc14/sta-663-2017): Great collection of references with examples. Highly recommend! **Mostly for reference and code examples, but they're very useful.**
* [Statistics Done Wrong](https://www.statisticsdonewrong.com): **MUST READ!!!**
* [Modern Machine Learning Algorithms: Strengths and Weaknesses](https://elitedatascience.com/machine-learning-algorithms) Breif overview of some machine learning algorithms with strengths and weaknesses to put them in context.
* [An Introduction to Statistical Learning](https://www-bcf.usc.edu/~gareth/ISL/ISLR%20First%20Printing.pdf): Nice intro to fairly complex statistical methods with very little math. **Highly recommend!** Example code is in R, but explanations are helpful in general. Note that this is a bit longer and more indepth than the options above. **This is more about understanding statistical methods than coding.**
* https://github.com/cs109/content
