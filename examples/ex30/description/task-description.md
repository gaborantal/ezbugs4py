A school's academic system (Uranus) can only export students' grades in the following
format: `Feri,2,1,3;Bela,3,2,4;Andris,1,5,3`. Unfortunately, Mari néni cannot interpret this, help her calculate the
students' averages.

Write the `average` function, which takes a string as a parameter. The text received in the parameter contains the data
of each student. The students are separated from each other by `;`, and their data by `,`. By data, we mean the
student's name and a list of their grades. The function should return a dictionary that tells us the average of each
student.

We can assume that a student has at least one grade.

If the function receives an empty string as a parameter, return with an empty dictionary.
