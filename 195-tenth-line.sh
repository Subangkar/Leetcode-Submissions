# Read from the file file.txt and output the tenth line to stdout.
# head file.txt -n 10 | tail -n 1

# sed '10q;d'

cat file.txt | sed '10q;d'