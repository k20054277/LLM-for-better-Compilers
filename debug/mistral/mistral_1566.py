
import asyncio

class ComplexNumber:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imag + other.imag
        )

async def get_complex_number():
    try:
        real = float(input("Enter the real part: "))
        imag = float(input("Enter the imaginary part: "))
        return ComplexNumber(real, imag)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        await asyncio.sleep(2)
        return get_complex_number()

async def main():
    num1 = await get_complex_number()
    num2 = await get_complex_number()

    complex_sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {complex_sum}")

if __name__ == "__main__":
    asyncio.run(main())
