/* Sample SAS Program */

/* Step 1: Create a sample dataset */
data students;
    input Name $ Age Score;
    datalines;
Alice 20 85
Bob 22 90
Charlie 21 78
Diana 23 88
;
run;

/* Step 2: Print the dataset */
proc print data=students;
run;

/* Step 3: Calculate summary statistics */
proc means data=students;
    var Score;
run;