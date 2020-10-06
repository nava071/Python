This script is to fetch the files pushed to artifactory after building from jenkins.

Typical Output:

```
Enter the repo (release, master, prod):release
Build created when (5minutes,10minutes,1d):1d



File1namepatternfile1   2020-10-06T09:53:43.848Z   9898989898989898989898989898989898989898
File1namepatternfile2   2020-10-06T09:57:43.848Z   9898989898989898989898989898989898989111
----------------------------------
File2namepatternfile1   2020-10-06T09:53:32.388Z   9898989898989898989898989898989898989100
File2namepatternfile2   2020-10-06T09:57:32.388Z   9898989898989898989898989898989898989233
----------------------------------

 /syn   release,File1namepatternfile2,File2namepatternfile2,None,None,None,None,None 

Press  any key to continue...
Process finished with exit code 0

```