Some basic git commands I used today to set this up:


`git init` initialises a local repository 

```
git add

git commit -m "comment"

```
git add "stages" the work to the Index, then git commit saves the work to the 
repository and it becomes the HEAD. Now it is ready to be added to the remote 
repository.

First you want to connect to the remote server:
`git remote add origin git@github.com:SophMC/notechain`

 -u only needs to be used the first time
`git push -u origin master`
