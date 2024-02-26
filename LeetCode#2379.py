class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k
        op = 0
        min_ops = k
        while r <= len(blocks):
            block = blocks[l:r]
            op = block.count('W')
            min_ops = min(op, min_ops)
            l += 1
            r += 1
        return min_ops
