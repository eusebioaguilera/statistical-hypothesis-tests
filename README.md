statistical-hypothesis-tests
============================

This repo contains several statistical hypothesis tests.

Wilcoxon (http://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test)

The Wilcoxon signed-rank test is used for comparing two related samples. This test is intended to compare 
two samples and test if there are significant differences between them. The assumptions for the compared
data are:

  * Data are paired and come from the same population.
  * Each pair is chosen randomly and independently.
  * The data are measured at least on an ordinal scale, but need not be normal.

The out of the script is the ranking table and the decision if the null hypothesis could be rejected. 

The file "wilcoxon_data_wikipedia.csv" contains the data of the examples that appears in the wikipedia
page. The usage is 

  python wilcoxon.py wilcoxon_data_wikipedia.csv

This example obtains the output:

The sum of the negatives ranks of the differences 18.0
p-value 0.593630591443
Null hypothesis could not be rejected!

Therefore the null hypothesis could not be rejected, and then we can not affirm that there is no 
significant differences.
