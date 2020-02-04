# SiPM Testing Chroma
This repository contas all of the Python scripts necessary to run Chroma simulations for our UMass Amherst set up. All of thee scripts are written in Python 2 and therefore need to be run in a Python 2 environment. Below are the instructions for running these Chroma simulations and editing the scripts on the Chichen-Itza2 computer in the lab.

If you are unfamiliar with using GitHub, please read over the latest version of the "How to Use GitHub" document found within the Chroma folder in the Box.


## Using the SiPM Testing Chroma GitHub Repository
The master branch as well as a branch for each user of the sipm-testing-chroma repository exists on Chichen-Itza2 within the file path "Desktop/github-chroma". The master branch is found in the folder "sipm-testing-chroma-master", and the personal branches are found within named folders (i.e. "michelle/sipm-tesing-chroma"). Changes made to the files in the master branch or a personal branch should be committed to the repository. Please follow the instructions below before and after making changes to the scripts.

### Before Editing
1. Make sure you're in your branch by checking that the blue text in the terminal leads to your folder within "Desktop/github-chroma". If you're still unsure, you can check which branch you are currently working in by entering in the terminal\
```git branch```\
The name of your branch should appear in green text in the terminal.
2. Enter in the terminal:\
```git pull```\
This ensures that you are working with the latest version of your branch.\
Even if you're certain that you are working with the latest version, it is still good practice to be in the habit of pulling before working with code in a repository.

### After Editing
1. Enter in the terminal:\
```git add .```\
This adds all of the files in the branch to the commit. If you don't want to add all of the files you have changed to the commit you can enter:
```git add <name of the files you want to add>```\
As shown, the names of the files you do want to add to the commit replace the period in the original command.
2. Enter in the terminal:\
```git commit -m "summary of changes"```\
The summary of the changes you made should be kept to 1 - 2 sentences and should be included in every commit.
3. Enter in the terminal:\
```git push```\
After entering this command, you should be prompted to enter your GitHub username and password. Once you enter your username and password, the changes you made have been pushed to the repository.


## Running Simulations on Chichen-Itza2
To run a simultation on Chichen-Itza2, simply run the terminal command:\
```
singularity exec --nv ~/Desktop/Chroma.img python ~/Desktop/github-chroma/sipm-testing-chroma-master/NewXenon_cell_simulation_13_7_18.py -a -d sipm -n 1000 -s 1
```

This is the command that runs the main script of the simulation. The file pathway "~/Desktop/github-chroma/sipm-testing-chroma-master" is the folder that contains the main script of the master branch of the repository. The file pathway you enter in the terminal should be changed depending on which branch you wat to be running the main script from. An example of a pathway for a user's personal branch would be "~Desktop/github-chroma/michelle/sipm-testing-chroma".

The name of the main script is "NewXenon_cell_simulation_13_7_18.py", and is entered immediately after the pathway of the folder that it's in. The name of this file is given a new date at the end after each major update. Normally this filename is the same for every branch.

After the file pathway are the characters "-a", "-d", "-n", "-s". These are known as arguments and perform the following actions:
- The argument "-a" simply tells theprogram to do an analysis of the simulation. This should be entered every time in order to see data from the simulation.
- The argument "-d" indicates the detector we want to use in the simulation. Currently we are using a SiPM detector so "-d" should be followed by "sipm" as shown in the example.
- The argument "-n" indicates the number of photons we want to simulate over each run. In the example, "-n" is followed by "1000" which will tell the program to simulate 1000 photons per run. The program can simulate a maximum of 1000000 photons per run.
- The argument "-s" indicates the seed number we want the program to use. The seed number represents a set of initial conditins for the simulaion (an approximate starting point for each photon). In the example, "-s" is followed by "1" which will tell the program to use seed 1. If two simulations are run with the exact same conditions and the same seed number, we should see the exact same results. 

Summary of Useful GitHub Commands:\
`git pull`\
`git add .`\
`git status`\
`git commit -m "summary of what you changed"`\
`git push`\
`git branch`\
