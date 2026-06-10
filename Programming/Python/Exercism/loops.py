"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    rounded = []
    for a in student_scores:
        rounded_number = round(a)
        rounded.append(rounded_number)
    return rounded  # Returning the updating list.
    pass


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed = []
    for a in student_scores:
        if a <= 40:  # Filtering the failed students. 
            failed.append(a) # Udating them in new list.
    number = len(failed)
    return number    # Returning the number of failed students.
    pass


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_students = []
    for a in student_scores:
        if a >= threshold:
            best_students.append(a)
    return best_students        
    pass


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    grade_range = highest - 40
    inter_grade_range = grade_range // 4 
    return [41, 41 + inter_grade_range, 41 + (inter_grade_range * 2), 41 + (inter_grade_range * 3)]
    pass


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    student_rank = []
    for a in range(len(student_names)):
        score = student_scores[a]
        names = student_names[a]
        rank = a + 1  # as index start at 0
        student_ranked_string = f"{rank}. {names}: {score}"
        student_rank.append(student_ranked_string)
    return student_rank
    pass


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    
    for student in student_info:
        if student[1] == 100:
            return student 
    return []
    
    pass
