import sys
#insert parent directory path
sys.path.insert(0,'../')

from codeforces.codeforces import codeforces
from codeforces.exception import exception

cd = codeforces()
ex = exception()
print cd.hacks(374).text

print cd.ratingChanges(374).text

print cd.standings(contestId=374,from=1,count=5,showUnofficial='true').url

checking working of exception API
r= cd.standings(contestId=374, count=5, showUnofficial='true')

if(r.status_code != 202):
	print ex.unwanted(cd.standings(contestId=374, count=5, showUnofficial='true').text)
else:
	print cd.standings(contestId=374, count=5, showUnofficial='true').text

