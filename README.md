# Secreted-Protein-Labeller
This program scrapes the UniProt online database to determine which proteins in a large set are secreted. This program was developed for use in the Svensson Lab at the Stanford School of Medicine Department of Pathology. Find more information about the research at the Svensson lab here: http://www.svenssonlabstanford.org/

# Setting up the Python Virtualenv
This program runs on Python 3.x and leverages several external libraries (Pandas, NumPy, Selenium, BeautifulSoup, etc.) that will need to be downloaded. One easy way to do so is using a virtual environment through Anaconda, which can be easily downloaded at https://www.anaconda.com/distribution. 

Once installed, download this repository and unzip its contents. Open up your command-line interface (e.g. Terminal) and navigate to the unzipped directory using **cd** (*If you would like an overview for navigating the file system in Terminal, check out this article on https://macpaw.com/how-to/use-terminal-on-mac*). Run the following commands to create the virtualenv and install all dependencies:

> conda env create -f environment.yml
>
> conda activate secreted-labeller

To ensure that everything was installed properly, run the following command:

> ./configure.sh

# Running the Program
Once all the dependencies are installed, you can run the program by first changing to the src directory and then running the main program. Use the following commands to execute this from within the repository directory:

> cd src
> python secreted.py

The program will ask you to input the necessary information, such as excel filenames and sheet names. The program currently takes around one minute to retrieve the proper annotation for 50 proteins.
