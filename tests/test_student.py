from school_schedule.student import Student

# Write your tests here!
def test_get_num_classes_nominal(self):
    
        student = Student("Claire", "freshmen", ["Gym", "Art", "Science"])
    
        count = student.get_num_classes()
        # Assert
        self.assertEqual(count, 3)