# Chroma
Contains all of the scripts used for the UMass Amherst version of Chroma light simulations for nEXO

## Instructions
### Add New Users:
Adding users to the organization will enable them to edit files on the repository. Everyone should have their own unique username and a password.

### Before Working With the Files:
Before editing any of the files or running a simulation, the user should enter the following command into the terminal:
`git pull`
This will ensure that they are working with the latest versions of the files in case anything has been committed remotely.

### After Making Changes to Any of the Files:
If any changes have been made to the files you work with during your session, you must push them to the repository using the following method:
Enter in the terminal:
`git add .`
This will add all files within the repository clone on the computer to the commit. If you do not wish to add all of the files in the repository clone to the commit, you can enter:
`git add "names of the files you DO want to add"`
This is generally discouraged.
Once all of the files have been added to the commit, enter in the terminal:
`git commit -m "summary of what you changed"`
This commits the changes you have made to the repository. The summary of what you changed should be kept to one or two sentences and MUST BE INCLUDED. The summary is very important because it lets others know of what has happened with the files in the repository, which is the main point of having one.
The last command to enter in the terminal is:
`git push`
which pushes the files in the commit to the repository and makes them available to all other users.

Summary of Useful Commands:
`git pull`
`git add .`
`git status`
`git commit -m "summary of what you changed"`
`git push`


