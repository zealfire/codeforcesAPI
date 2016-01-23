import sys
#insert parent directory path
sys.path.insert(0,'../')

from codeforces.codeforces import codeforces

cd = codeforces()
print cd.hacks(374).text

print cd.ratingChanges(374).text

print cd.standings(contestId=374,from=1,count=5,showUnofficial='true').url