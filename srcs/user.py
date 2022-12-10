import faker

fake = faker.Faker()

def get_user():
	""" Generate a single user
	:return: str: user
	"""
	return f"{fake.first_name()} {fake.last_name()}"

def get_users(n):
	"""Generate a list of users
	:param n: int: number of user to generate
	:return: list[str]: users
	"""
	users = []
	for i in range(n):
		users.append(get_user())
	return users

if __name__ == "__main__":
	user = get_users(n=10)
	print(user)