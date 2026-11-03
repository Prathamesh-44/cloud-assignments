# Assignment 4 - Jenkins Freestyle (Q1-10)

Install: https://www.jenkins.io/doc/book/installing/linux/#debianubuntu then open http://localhost:8080.

**Every job:** New Item -> name -> *Freestyle project* -> OK -> Build Steps -> *Add build step -> Execute shell* -> paste -> Save -> *Build Now* -> Build #1 -> *Console Output*.

| # | Job name | Execute shell content |
|---|----------|----------------------|
| 1 | hello_jenkins | `echo "Welcome to Jenkins!"` |
| 2 | py_add | `python3 -c "a=10; b=20; print('Sum =', a+b)"` |
| 3 | java_hello | see block A below |
| 4 | show_date | `echo "Current date and time: $(date)"` |
| 5 | github_fetch | Source Code Management -> Git -> repo URL (public) -> branch `*/main`; shell: `ls -l; echo "Build OK"` |
| 6 | github_python | Same SCM as 5; shell: `python3 hello.py` (hello.py must exist in that repo) |
| 7 | list_files | `ls -l` |
| 8 | even_numbers | `python3 -c "print([n for n in range(1,51) if n%2==0])"` |
| 9 | factorial | `python3 -c "import math; print(math.factorial(5))"` |
| 10 | sysinfo | see block B below |

**Block A (Q3):**
```bash
cat > HelloWorld.java <<'JAVA'
public class HelloWorld {
    public static void main(String[] a) { System.out.println("Hello from Java in Jenkins!"); }
}
JAVA
javac HelloWorld.java
java HelloWorld
```
**Block B (Q10):**
```bash
echo "OS: $(uname -s)  $(grep PRETTY_NAME /etc/os-release | cut -d= -f2)"
echo "User: $(whoami)"
echo "Disk:"; df -h /
```
Needs `sudo apt install -y default-jdk python3` on the Jenkins machine.
