class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Parse real and imaginary parts from num1
        real1, imag1 = map(int, num1[:-1].split('+'))
        # Parse real and imaginary parts from num2
        real2, imag2 = map(int, num2[:-1].split('+'))
        
        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        # Since i^2 = -1, ac is real, -bd is real, ad*i and bc*i are imaginary
        res_real = (real1 * real2) - (imag1 * imag2)
        res_imag = (real1 * imag2) + (real2 * imag1)
        
        return f"{res_real}+{res_imag}i"