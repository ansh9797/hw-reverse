class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]

if __name__ == "__main__":
        s = input("Enter a word: ")
        reverse_instance = Reverse(s)
        print("Reversed string:", reverse_instance.reverse_string())
