#방법 1
def grade1():
  kor = int(input('국어점수 입력:'))
  eng = int(input('영어점수 입력:'))

  total = kor + eng
  avg = total / 2

  if avg >= 90 :
    print('성적은 A 입니다')

  elif avg >= 80 :
    print('성적은 B 입니다')

  elif avg >= 70 :
    print('성적은 C 입니다')

  elif avg >= 60 :
    print('성적은 D 입니다')

  else :
    print('낙방하였습니다')

#방법2
def grade2():
  kor = int(input('국어점수 입력:'))
  eng = int(input('영어점수 입력:'))

  total = kor + eng
  avg = total / 2
  result = 'FDCBA'[(avg >= 60) + (avg >= 70) + (avg >= 80) + (avg >= 90)]
  print(f'성적은 {result} 입니다')
























print()
print()