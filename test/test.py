import sys
#insert parent directory path
sys.path.insert(0,'../')

from codeforces.codeforces import codeforces

cd = codeforces()
print cd.hacks(374).text