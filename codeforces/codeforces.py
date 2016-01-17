import requests

class codeforces:
	def __init__(self):

	#Return a list of hack during a specific contest. A list of hack object is
	#returned
	def hacks(self, Id):
		parameter = "contestId=" + str(Id)
		r = requests.get('http://codeforces.com/api/contest.hacks', params=parameter)
		return r

	#Returns information about all available contests
	def list(self, flag):
		parameter = "gym=" + flag
		r = requests.get('http://codeforces.com/api/contest.list', params=parameter)
		return r

	#Returns rating changes after the contest.
	def ratingChanges(self, Id):
		parameter = "contestId=" + str(Id)
		r = requests.get('http://codeforces.com/api/contest.ratingChanges', params=parameter)
		return r

	#Returns the description of the contest.
	def standings(self, **kwargs):
		#for key, value in kwargs.iteritems():
		r = requests.get('http://codeforces.com/api/contest.standings', **kwargs)
		return r

	#Returns submission for specified contest.
	def status(self, **kwargs):
		r = requests.get(' http://codeforces.com/api/contest.status', **kwargs)
		return r

	#Returns all problems from problemsets.
	def problems(self, tags):
		parameter = "tags=" + tags
		r = requests.get('http://codeforces.com/api/problemset.problems', params=parameter)
		return r

	#Returns recent submissions.
	def recentStatus(self, count):
		parameter = "count=" + str(count)
		r = requests.get('http://codeforces.com/api/problemset.recentStatus', params=parameter)
		return r

	#Returns information about 1 or several users.
	def handles(self, *args):
		parameter = "handles="
		for value in args:
			parameter += value + ';'
		parameter = parameter[:len(parameter)-1]
		r = requests.get('http://codeforces.com/api/user.info', params=parameter)
		return r

	#Returns the list users who have participated in 1 rated contest.
	def ratedList(self, flag):
		parameter = "activeOnly=" + str(flag)
		r = requests.get('http://codeforces.com/api/user.ratedList', params=parameter)
		return r

	#Returns rating history of specific user.
	def rating(self, handle):
		parameter = "handle=" + handle
		r = requests.get('http://codeforces.com/api/user.rating', params=parameter)
		return r

	#Returns submission of specified user.
	def status(self, **kwargs):
		r = requests.get('http://codeforces.com/api/user.status', params=kwargs)
		return r




