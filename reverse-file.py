import argparse

# Build the parser using argparse class/functions
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v' action=version, version='%(prog)s 1.0')

# Parse agrs to variable 'args'
args = parser.parse_args()

# Opens filename.txt, reads and reverses lines & strings (if --limit arg provided also)
with open(args.filename) as f:
	line = f.readlines()
	lines.reverse()

	if args.limit:
		lines = lines[:args.limit]

	for line in lines:
		print(line.strip()[::-1])
