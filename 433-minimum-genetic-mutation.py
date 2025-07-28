class Solution:


    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        replace_map = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
        def neighbor(s, i):
            return (s[:i]+c+s[i+1:] for c in replace_map[s[i]])

        explored = {startGene: 0}

        bank = set(bank)

        q = deque([startGene])
        while q:
            gene = q.popleft()
            if gene == endGene:
                return explored[gene]
            for i in range(len(gene)):
                for nbr in neighbor(gene, i):
                    if nbr in bank and not nbr in explored:
                        explored[nbr] = explored[gene] + 1
                        q.append(nbr)
        return -1
        