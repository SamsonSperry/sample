import random


def main(count: int = 75, low: int = 1, high: int = 100) -> None:
	"""Generate `count` random integers in [low, high] and print whether
	each is divisible by three.
	"""
	for i in range(1, count + 1):
		n = random.randint(low, high)
		if n % 3 == 0:
			result = "divisible by 3"
		else:
			result = "not divisible by 3"
		print(f"{i:2d}. {n} -> {result}")


if __name__ == "__main__":
	main()


