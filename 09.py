class Solution:
    def checksum(self, inp: str):
        s = list(inp)
        n_s = len(s)

        r = n_s - 1
        l = 0

        checksum = 0

        block_position = 0

        while l < r:
            if (l % 2) == 0:
                block_size = int(s[l])
                l_id = l // 2
                for _ in range(block_size):
                    checksum += block_position * l_id
                    block_position += 1
                l += 1
            else:
                free_space_size = int(s[l])
                if free_space_size:
                    if (r % 2) == 0:
                        block_size = int(s[r])
                        if block_size > 0:
                            r_id = r // 2
                            capacity = min(free_space_size, block_size)
                            for _ in range(capacity):
                                checksum += block_position * r_id
                                block_position += 1
                            free_space_size -= capacity
                            block_size -= capacity
                            s[l] = str(free_space_size)
                            if free_space_size == 0:
                                l += 1
                            s[r] = str(block_size)
                            if block_size == 0:
                                r -=1
                        else:
                            r -= 1
                    else:
                        r -= 1
                else:
                    l += 1

        block_size = int(s[r])

        if block_size > 0:
            if (r % 2) == 0:
                r_id = r // 2
                for _ in range(block_size):
                    checksum += block_position * r_id
                    block_position += 1

        return checksum

    def checksum_part2(self, inp: str):
        s = list(inp)
        n_s = len(s)

        checksum = 0

        block_position = 0

        moved_blocks = {}
        empty_spaces = {}

        for r in range((r // 2) * 2, 0, -2):
            block_size = int(s[r])
            if block_size == 0:
                continue
            for free_space_i in range(1, r, 2):
                free_space_size = int(s[free_space_i])
                if free_space_size == 0:
                    continue
                if block_size > free_space_size:
                    continue
                moved_blocks.setdefault(free_space_i, [])
                moved_blocks[free_space_i].append((r // 2, block_size))
                empty_spaces.setdefault(r, block_size)
                free_space_size -= block_size
                block_size = 0
                s[free_space_i] = str(free_space_size)
                s[r] = str(block_size)
                break

        for l in range(n_s):
            if (l % 2) == 0:
                block_size = int(s[l])
                l_id = l // 2
                if l in empty_spaces:
                    for _ in range(empty_spaces[l]):
                        block_position += 1
                else:
                    for _ in range(block_size):
                        checksum += block_position * l_id
                        block_position += 1
            else:
                if l in moved_blocks:
                    moved_items = moved_blocks[l]
                    for (id, size) in moved_items:
                        for _ in range(size):
                            checksum += block_position * id
                            block_position += 1
                for _ in range(int(s[l])):
                    block_position += 1

        return checksum
