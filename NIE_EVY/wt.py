#!/Users/adam_parrot/miniconda3/bin/python

class WaveletTree:
    def __init__(self, input_string):
        self.input_string = input_string
        self.alphabet = sorted(set(input_string))
        self.tree = self.build_tree(input_string, self.alphabet)

    def build_tree(self, string, alphabet):
        """
        Constructs a wavelet tree. Returns a dictionary of characters:bitmaps for each child.
        """
        if len(alphabet) == 1:
            return {'char': alphabet[0], 'bitmap': []} # Leaf node

        mid = len(alphabet) // 2
        left_alphabet = alphabet[:mid]
        right_alphabet = alphabet[mid:]
        
        # Create a binary bitmap for this level
        bitmap = [1 if char in right_alphabet else 0 for char in string]

        # Split the input string into left and right
        left_string = ""
        right_string = ""
        for i in range(len(string)):
            if bitmap[i] == 0:
                left_string += string[i]
            else:
                right_string += string[i]

        # Return the bitmap and continue constructing the tree unless a leaf node is reached 
        return {
            'bitmap': bitmap,
            'left': self.build_tree(left_string, left_alphabet),
            'right': self.build_tree(right_string, right_alphabet)
        }

    def rank(self, i, c):
        """
        Counts the number of occurrences of symbol c ∈ Σ from position 1 up to position i in a string.
        """
        node = self.tree
        alphabet = self.alphabet

        if c not in alphabet or i > len(self.input_string):
            return None # Invalid input

        # Traverse down the tree to find the character's rank
        while 'char' not in node:
            mid = len(alphabet) // 2
            bitmap = node['bitmap']
            rank = sum(bitmap[:i + 1])

            if c in alphabet[:mid]:
                node = node['left']
                alphabet = alphabet[:mid]
                i = i - rank
            else:
                node = node['right'] 
                alphabet = alphabet[mid:]
                i = rank - 1

        return i + 1 

    def select(self, k, c):
        """
        Finds the k-th symbol c in a string.
        """
        node = self.tree
        alphabet = self.alphabet
        path = []
        
        if c not in alphabet or k > len(self.input_string):
            return None # Invalid input

        # Traverse down the tree to find the character's path
        while 'char' not in node:
            mid = len(alphabet) // 2
            if c in alphabet[:mid]:
                path.append(('left', node['bitmap']))
                node = node['left']
                alphabet = alphabet[:mid]
            else:
                path.append(('right', node['bitmap']))
                node = node['right']
                alphabet = alphabet[mid:]

        # Traverse back up to find the select index
        current_pos = k - 1 # Begin with 0-based indexing
        for direction, bitmap in reversed(path):
            target = 0 if direction == 'left' else 1
            count = 0
            for i, bit in enumerate(bitmap):
                if bit == target:
                    count += 1
                    if count > current_pos:
                        current_pos = i
                        break

        #return current_pos + 1 # Return the 1-based index
        return current_pos # In the class, we were shown that select operates on 1-based indexing, however, the unittest was 0-based.
