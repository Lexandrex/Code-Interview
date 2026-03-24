# Problema 1 de Array:
#Dado um array de inteiros nums e um inteiro target, retorne os índices dos dois números
# de forma que a soma deles seja igual atarget .

#Você pode assumir que cada entrada terá exatamente uma solução e que não poderá usar
# o mesmo elemento duas vezes.

# Soma de dois com IA

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}  # valor -> índice
        
        for i, num in enumerate(nums):
            complemento = target - num
            
            if complemento in mapa:
                return [mapa[complemento], i]
            
            mapa[num] = i

# Sem IA
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]