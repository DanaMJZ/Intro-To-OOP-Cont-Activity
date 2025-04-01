from school_schedule.student import Student
import pytest
# Write your tests here!
#def test_student_class():
    #Arrange
#     name = "Quinn"
 #   grade = "Junior"
 #   classes = ["Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition"]


# def test_add_classes():

def test_get_num_classes():
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

#Act
    count_classes = student.get_num_classes()
    #Assert
    assert count_classes == 6

def test_empty_classes_list():
    student = Student(
                "Quinn", 
                "junior", [])
    count_classes = student.get_num_classes()
    assert count_classes == 0

def test_display_classes():
    student = Student(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
            )
    display_string = student.display_classes()
    expected_string = "Algebra, Writing, Contemporary Issues, Gym, Earth Science, Painting"
    assert display_string == expected_string, f"Expected '{expected_string}', but got '{display_string}'"


