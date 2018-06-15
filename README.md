## Python OOP Test

Written in Python 2.7

- There are teachers
- There are students
- Teachers teach the students in multiple classes
- Teachers can assign quizzes to students
- Students must complete each quiz, although partial completion is acceptable
- Quizzes must be graded (only upon completion, I'm assuming, although it seems possible that students are graded on partial quiz completion)
- Each student's total grade must be calculated

### Classes

- Classes

  - Properties
    - Length of class
    - Teacher teaching this class
    - Number of students in class (variable)
    - Subject of class (math, science, reading, computer science, and philosophy)

- Person

  - Teachers - Inherit from person

    - Properties
      - Class subject
      - Quality of teaching
      <!-- - Length of time to create the quiz -->
      - Number of students that the teacher can handle

    - Methods
      - Begin class
      - End class
      - Teach students
      - Plan date of quizzes
      - Create quizzes
      - Administer tests
      - Grade quizzes
      - Calculate total grade for each student based on quiz score
      <!-- - Remove student from that class for the day when patient hits 0 -->
      <!-- - Teach individual student -->

  - Student - Inherit from person

    - Properties
      - Responsibility (how likely to go to class, affects how quickly quiz answers will be com
      - Intelligence
      - Proficiency in each subject
      <!-- - Attitude (how well the student reacts to a good/poor grade, affects future responsibility) -->

    - Methods:
      - Go to class
      - Listen to teacher
      - Take notes
      - Take quiz (the amount of quiz completed is a function of quiz difficulty and student intelligence)
      - Receive grade
      - React to grade

- Quizzes

  - Properties:
    - Subject
    - Number of questions
    - Amount of time available to take the quiz
    - Difficulty

## Functionality

Five teachers will be generated, each assigned one of the available subjects. No two teachers can be assigned the same subject. Each teacher will only be able to handle a specified number of students, and if more students are in a class than a teacher can handle, their effectiveness at teaching decreases.

One hundred students will be generated. Each student will be assigned a proficiency in each subject, which will act as a modifier for how well they do on each subject. Additionally, each student will be assigned a proficiency coefficient for each subject, which also affects their ability to learn that subject. Finally, each student is assigned an intelligence coefficient, as well as a responsibility coefficient. These three characteristics will be used to calculate a students grade as a function of the teachers' effectiveness at teaching a subject and the amount of time that the teacher has to teach each subject.

Five classes will be randomly generated and assigned one of the subjects. Each class will be assigned a single teacher, and then randomly assigned a number of students (with a cap of no more than half of the total number of students). Each class will be assigned a length, which can never exceed more than one third of the total school day.

The attributes of the class and student will be used to calculate student performance on each quiz, for which there will be three per class.

Finally, a chart of each students' performance will be displayed for each of the quizzes the student take, as well as each students' final grade.