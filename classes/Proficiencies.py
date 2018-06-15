from Subject import Subject


class Proficiencies(object):
    def __init__(self):
        """
        The proficiency of a student or teacher at a certain subject
        """

    def determine_teacher_subject_proficiency(self):
        """
        Determine how well each teacher can teach each subject
        """
        subject = Subject()
        available_subjects = subject.subjects
        subject_proficiencies = dict()
        while len(available_subjects) > 0:
            this_subject = subject.get_subject(available_subjects)
            proficiency = subject.get_subject_proficiency()
            subject_proficiencies[this_subject] = proficiency

        return subject_proficiencies
