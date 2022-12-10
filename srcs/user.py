import faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / 'user.log', level=logging.WARNING)

fake = faker.Faker()

def get_user():
	"""
	Generate a user "{first_name} {last_name}" from Faker module
	Returns: str

	"""
	logging.info("Generating user.")
	return f"{fake.first_name()} {fake.last_name()}"

def get_users(n):
	"""
	Generate a list of {n} user
	Args: number of user to return
		n: int

	Returns: list

	"""
	users = []
	for i in range(n):
		users.append(get_user())
	logging.info(f"Generating a list of {n} user.")
	return users

if __name__ == "__main__":
	user = get_users(n=10)
	print(user)