# Locality Sensitive Hashing (LSH)

An improved README writeup coming soon. For now, keep in mind that:

lsh.py  -  a standalone proof of concept of LSH (slow, but scores well even with dirty data)

spark_lsh.py - rewrite of lsh.py for use on a Spark cluster; at the moment it's mostly non-functional, but it's a work in progress.

Note: evaluate.py, test.py, text_helpers.py will be used by spark_lsh.py


To learn more about LSH start with these slides: http://web.stanford.edu/class/cs246/slides/03-lsh.pdf

For a more in-depth read on LSH checkout chapter three of the "Mining of Massive Datasets" book: http://infolab.stanford.edu/~ullman/mmds/book.pdf
