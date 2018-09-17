import hashlib

def main() :
	yahoo()
	linkedin()

def yahoo() :
	passwords = []
	f = open("yahoo/password.file")
	content = f.readlines()
	i = 0
	while content[i] != "3. email:pass dump (450k users)\n" and i < len(content):
		i += 1
	i += 1
	while content[i] != "3. email:pass dump (450k users)\n" and i < len(content):
		i += 1
	i += 7
	while len(passwords) < 100 :
		info = content[i].split(':')
		if len(info) > 2 :
			passwords.append((content[i].strip(), info[2].strip()))
		i += 1
	f.close()
	f = open("yahoo/extracted_passwords.txt", "w")
	for pas in passwords :
		f.write(pas[0] + ' ' + pas[1] + '\n')
	f.close()

def linkedin() :
	f = open("linkedin/SHA1.txt")

	hash1 = hashlib.sha1('abc123').hexdigest()
	hash2 = hashlib.sha1('password')

	content = f.readlines()

	seen = {}
	dupes = []

	for x in content :
		if x not in seen:
			seen[x] = 1
		else:
			if seen[x] == 1:
				dupes.append(x)
			seen[x] += 1

	print dupe




if __name__ == "__main__" :
	main()