class Solution:
    def quadraticRoots(self, a, b, c):
        # code here
        d = b*b - 4*a*c

        if d < 0:
            return [-1]

        sqrt_val = math.sqrt(d)
        root1 = (-b + sqrt_val) / (2*a)
        root2 = (-b - sqrt_val) / (2*a)

        root1 = math.floor(root1)
        root2 = math.floor(root2)

        if root1 >= root2:
            return [root1, root2]
        else:
            return [root2, root1]
        