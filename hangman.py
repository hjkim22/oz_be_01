# 기본 라이브러리라 파이썬 설치시 자동으로 설치됩니다!
# random 모듈은 랜덤한 숫자를 생성할 때 사용합니다.
import random

# 게임에 사용될 단어 목록
words = ["apple", "banana", "orange", "grape", "lemon"]

# 행맨 그림
hangman_pics = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---""",
]


class HangmanGame:
    # 클래스가 만들어 질 때 자동으로 호출되는 메소드
    # (생성자 메소드라고 부릅니다)
    def __init__(self):
        self.word = random.choice(words)  # 랜덤으로 단어 선택

        self.guesses = set()  # 추측된 글자 저장

        self.attempts = 6  # 시도 횟수

    def display(self):
        # 단어의 현재 상태 표시
        result = ""

        # 위에서 설정한 단어의 글자들을 하나씩 가져옵니다.
        for char in self.word:
            # 만약 추측된 글자가 설정한 단어에 포함되어 있다면
            if char in self.guesses:
                # 추측된 글자를 표시합니다.
                result += char
            else:
                # 추측된 글자가 아니라면 _를 표시합니다.
                result += "_"

        # 단어의 현재 상태를 반환합니다.
        return result

    def play(self):
        # 게임을 시작합니다.
        # 시도 횟수가 0이 될 때까지 반복합니다.
        while self.attempts > 0:
            # 행맨 그림을 표시합니다.
            print(hangman_pics[6 - self.attempts])

            # 현재 단어의 상태를 표시합니다.
            # (추측된 글자는 표시하고, 추측되지 않은 글자는 _로 표시합니다.)
            # ex)
            # 처음에는 _ _ _ _ _ _ _ _ 로 표시됩니다.
            #
            # a를 추측했다면 a _ _ _ _ _ _ _ 로 표시됩니다.
            print(self.display())

            # 현재까지 추측한 글자들을 표시합니다.
            guess = input("글자를 추측해보세요: ").lower()

            # 추측한 글자가 이미 추측한 글자 목록에 있다면
            if guess in self.guesses:
                print("이미 추측한 글자입니다.")

            # 추측한 글자가 설정한 단어에 포함되어 있지 않다면
            elif guess in self.word:
                # 추측한 글자를 추측한 글자 목록에 추가하고 "단어를 맞추셨군요. 더 힘내봐요"라고 출력해주세요
                self.guesses.add(guess)
                # 단어를 맞추셨군요. 더 힘내봐요"라고 출력해주세요
                # 만약 추측한 글자들이 설정한 단어의 모든 글자를 포함한다면
                if set(self.word).issubset(self.guesses):
                    print(f"축하합니다! 단어를 맞추셨습니다: {self.word}")
                    break
            # 추측한 글자가 설정한 단어에 포함되어 있지 않다면
            else:
                # 시도 횟수를 1 감소시킵니다.
                self.attempts -= 1
                print(f"틀렸습니다. 남은 시도 횟수: {self.attempts}")
            # 시도 횟수가 0이 되었다면
            if self.attempts == 0:
                print(hangman_pics[-1])
                print(f"게임 오버. 정답은: {self.word}")


if __name__ == "__main__":
    game = HangmanGame()
    game.play()
