import sys
sys.argv

# l1 = sys.argv
# print(l1)

# ---

# sentence = sys.argv[1]
# print(len(sentence))

# ---

# n1 = int(sys.argv[1])
# n2 = int(sys.argv[2])

# print(n1 * n2)

# ---

# open('test.txt', r) - read
# open('test.txt', w) - write
# open('test.txt', a) - append
# open('test.txt', t) - text (default)

outfile = open('testfile.txt', 'w', encoding='utf-8')

outfile.write('some text\n')
outfile.write('...more text\n')
outfile.close()