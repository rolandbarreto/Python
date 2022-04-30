def run():
    subjects = ['Math','Physics','Quemistry','History','Language']

    # Easy way
    # for i in subjects:
    #     x = input(f'Enter the score you got in {i}: ')
    #     print(f'You got {x} on {i}')

    scores = []
    for subject in subjects:
        score = input(f'Enter the score you got in {subject}: ')
        scores.append(score)
    for i in range(len(subjects)):
        print(f'You got {scores[i]} on {subjects[i]}')


if __name__ == '__main__':
    run()