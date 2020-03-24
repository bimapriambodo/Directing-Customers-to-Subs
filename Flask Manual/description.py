def get_ai_grade(prob):
    d = dict()
    if prob <= 20:
        grade = 'E'
        description = 'Very Low Probabilty Will be Enrolled'
    elif prob <= 40:
        grade = 'D'
        description = 'Low Probabilty Will be Enrolled'
    elif prob <= 60:
        grade = 'C'
        description = 'Average Probabilty Will be Enrolled'
    elif prob <= 80:
        grade = 'B'
        description = 'High Probabilty Will be Enrolled'
    else:
        grade = 'A'
        description = 'Very High Probabilty Will be Enrolled'
    d['grade'] = grade
    d['description'] = description
    return d