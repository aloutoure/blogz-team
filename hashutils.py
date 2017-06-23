import hashlib, string, random

def make_salt():
	return ''.join([random.choice(string.ascii_letters) for x in range(5)])

def make_pw_hash(password, salt=None):
	if not salt:
		salt = make_salt()
	str_to_hash = password + salt
	return hashlib.sha256(str_to_hash.encode()).hexdigest() + ',' + salt

def check_pw_hash(password, hash):
	salt = hash.split(',')[1]
	pw_hash = make_pw_hash(password, salt)
	return pw_hash == hash