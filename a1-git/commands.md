# Git Assignments (Assignment 1 PDF + Assignment 2 Q1-3 + Self 10-11)

## Setup (once)
```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

## A1: Local Git
```bash
mkdir git-demo && cd git-demo && git init
cp ../calculator.py . && git add calculator.py && git commit -m "Add calculator with add()"
cp ../Greeting.java . && git add Greeting.java && git commit -m "Add Greeting.java personalised hello"
git log --oneline
```

## A2: Branch workflow
```bash
git branch -m master main
git checkout -b feature-subtract
cat >> calculator.py <<'PY'

def subtract(a, b):
    return a - b
PY
git add calculator.py && git commit -m "Add subtract()"
git checkout main
cat calculator.py          # subtract() is gone
git merge feature-subtract
git log --oneline --graph
```

## A3: Merge conflict
```bash
# main: Greeting prints "Hello, yourname!"
git checkout -b dev-a
sed -i 's/Hello, " + name + "!/Good morning, " + name + "./' Greeting.java
git commit -am "Dev A: good morning"
git checkout main
sed -i 's/Hello, " + name + "!/Hey there, Friend!/' Greeting.java
git commit -am "Dev B: hey there"
git merge dev-a            # CONFLICT
cat Greeting.java          # see <<<<<<< ======= >>>>>>> markers
nano Greeting.java         # keep the line you want, delete markers
git add Greeting.java && git commit -m "Resolve merge conflict"
```

## A4: Push to GitHub (create EMPTY repo on github.com first)
```bash
git remote add origin https://github.com/<user>/git-demo.git
git push -u origin main
```
Use a Personal Access Token as the password (GitHub -> Settings -> Developer settings -> Tokens).

## A5: Collaboration + Pull Request
1. A: repo -> Settings -> Collaborators -> Add people -> invite B.
2. B: `git clone https://github.com/<A>/git-demo.git && cd git-demo`
3. B: `git checkout -b feature-b` -> edit file -> `git add . && git commit -m "B's change"` -> `git push -u origin feature-b`
4. B: GitHub -> "Compare & pull request" -> title + description -> Create pull request.
5. A: Pull requests tab -> Files changed -> Merge pull request -> Confirm -> Delete branch.
6. Both: `git checkout main && git pull`

## Self-Assignment 11: stash and revert
```bash
git checkout -b feat-x && echo "x" > x.txt && git add x.txt && git commit -m "add x"
git checkout main && git merge feat-x
echo "wip" >> calculator.py
git stash            # saves uncommitted work
git stash list
git stash pop        # brings it back
git commit -am "wip change"
git revert HEAD      # creates a new commit undoing the last one
git log --oneline
```
