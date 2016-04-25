Some basic git commands I used today to set this up:


`git init` initialises a local repository 


`git add` stages the work to Index

`git commit -m "comment"` saves the work to the repository


Now the locally saved work can be added to the remote repository.

First you want to connect to the remote server:
`git remote add origin git@github.com:SophMC/notechain`


`git push -u origin master` -u is added the first time, after that you just 
need to be inside the local repo that you want to push and type
`git push`
