def run():
    subjects = ['Math','Physics','Quemistry','History','Language']

    passed = []
    for i in subjects:
        score = float(input(f'Enter the score you got in {i}: '))
        if score >=5 :
            passed.append(i)
    for i in passed:
        subjects.remove(i)
    print(f'You have to repeat on {str(subjects)}')


if __name__ == '__main__':
    run()