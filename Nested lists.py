def sorted_scores_final(name_scores):
    scores=[]
    for students in name_scores:
        scores.append(students[1])
    sorted_scores=sorted(set(scores))
    second_lowest_score=sorted_scores[1]
    
    names_of_secondlowest=[]
    for students in name_scores:
        if students[1]==second_lowest_score:
            names_of_secondlowest.append(students[0])
    names_of_secondlowest=sorted(names_of_secondlowest)
        
    for name in names_of_secondlowest:
        print(name)

if __name__ == '__main__':
    name_scores=[]
    for student in range(int(input())):
        name = input()
        score = float(input())
        name_scores.append([name,score])
    sorted_scores_final(name_scores)
