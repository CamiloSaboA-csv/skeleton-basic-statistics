# utilities or parameters for the correct operation or solution of the problem

MAX_VALUE: int = 999

def validate_int(x: int) -> int:
	try:
		return int(x)
	except:
		raise ValueError(
                f"The value {x} is not an integer and cannot be transformed to one either, please use a integer")
