# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 대소문자 구분없이 "H" 또는 "HELP"일 경우 True,
          그렇지 않을 경우 False를 반환함
    Examples:
        # >>> import morsecode as mc
        # >>> mc.is_help_command("H")
        True
        # >>> mc.is_help_command("Help")
        True
        # >>> mc.is_help_command("Half")
        False
        # >>> mc.is_help_command("HeLp")
        True
        # >>> mc.is_help_command("HELLO")
        False
        # >>> mc.is_help_command("E")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    if user_input.lower() == "h" or user_input.lower() == "help":
        # 입력한 값의 소문자가 "h" 또는 "help"인 경우 True
        result = True
    else:
        # 그렇지 않을 경우 False
        result = False
    return result
    # ==================================


def is_validated_english_sentence(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) 숫자가 포함되어 있거나,
          2) _@#$%^&*()-+=[]{}"';:\|`~ 와 같은 특수문자가 포함되어 있거나
          3) 문장부호(.,!?)를 제외하면 입력값이 없거나 빈칸만 입력했을 경우
    Examples:
        # >>> import morsecode as mc
        # >>> mc.is_validated_english_sentence("Hello 123")
        False
        # >>> mc.is_validated_english_sentence("Hi!")
        True
        # >>> mc.is_validated_english_sentence(".!.")
        False
        # >>> mc.is_validated_english_sentence("!.!")
        False
        # >>> mc.is_validated_english_sentence("kkkkk... ^^;")
        False
        # >>> mc.is_validated_english_sentence("This is Gachon University.")
        True
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    user_input_tmp = user_input
    for i in list(".,!?"):
        # 문장부호(.,!?)를 제외
        user_input_tmp = user_input_tmp.replace(i,"")
    if user_input_tmp == "" or set(user_input_tmp) == set(" "): # 틀린 부분
        # 문장부호(.,!?)를 제외하고 입력값이 없거나 빈칸만 입력했을 경우, False
        result = False
        return result
    for i in list("""0123456789_@#$%^&*()-+=[]{}"';:\|`~"""):
        if i in user_input_tmp:
            # 숫자가 포함되어 있거나, _@#$%^&*()-+=[]{}"';:\|`~ 와 같은 특수문자가 포함되어 있는 경우, False
            result = False
            return result
    # 위 경우에 모두 해당하지 않으면, True
    result = True
    return result
    # ==================================


def is_validated_morse_code(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) "-","."," "외 다른 글자가 포함되어 있는 경우
          2) get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우 ex)......
    Examples:
        # >>> import morsecode as mc
        # >>> mc.is_validated_morse_code("..")
        True
        # >>> mc.is_validated_morse_code("..-")
        True
        # >>> mc.is_validated_morse_code("..-..")
        False
        # >>> mc.is_validated_morse_code(". . . .")
        True
        # >>> mc.is_validated_morse_code("-- -- -- --")
        True
        # >>> mc.is_validated_morse_code("!.1 abc --")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    user_input_split = user_input.split() # 틀린 부분
    # user_input을 공백을 기준으로 분리
    morse_code = get_morse_code_dict().values()
    # 모스 부호를 불러오기
    for i in user_input_split:
        # 모스 부호의 해당 여부만 파악하면, "-","."," "외 다른 글자가 포함되어 있는 경우는 고려하지 않아도 괜찮음
        if i not in morse_code:
            # get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우, False
            result = False
            break
        else:
            # 그렇지 않으면 True
            result = True
    return result
    # ==================================



def get_cleaned_english_sentence(raw_english_sentence):
    """
    Input:
        - raw_english_sentence : 문자열값으로 Morse Code로 변환 가능한 영어 문장
    Output:
        - 입력된 영어문장에수 4개의 문장부호를 ".,!?" 삭제하고, 양쪽끝 여백을 제거한 문자열 값 반환
    Examples:
        # >>> import morsecode as mc
        # >>> mc.get_cleaned_english_sentence("This is Gachon!!")
        'This is Gachon'
        # >>> mc.get_cleaned_english_sentence("Is this Gachon?")
        'Is this Gachon'
        # >>> mc.get_cleaned_english_sentence("How are you?")
        'How are you'
        # >>> mc.get_cleaned_english_sentence("Fine, Thank you. and you?")
        'Fine Thank you and you'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = raw_english_sentence.strip()
    # 양쪽 끝 여백을 제거
    for i in list(".,!?"):
        # 문장부호(.,!?)를 삭제
        result = result.replace(i, "")
    return result
    # ==================================


def decoding_character(morse_character):
    """
    Input:
        - morse_character : 문자열값으로 get_morse_code_dict 함수로 알파벳으로 치환이 가능한 값의 입력이 보장됨
    Output:
        - Morse Code를 알파벳으로 치환함 값
    Examples:
        # >>> import morsecode as mc
        # >>> mc.decoding_character("-")
        'T'
        # >>> mc.decoding_character(".")
        'E'
        # >>> mc.decoding_character(".-")
        'A'
        # >>> mc.decoding_character("...")
        'S'
        # >>> mc.decoding_character("....")
        'H'
        # >>> mc.decoding_character("-.-")
        'K'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    # 모스 부호를 불러오기
    morse_code_dict_reverse = {j: i for i, j in morse_code_dict.items()}
    # key와 value를 서로 바꿈
    result = morse_code_dict_reverse[morse_character]
    return result
    # ==================================


def encoding_character(english_character):
    """
    Input:
        - english_character : 문자열값으로 알파벳 한 글자의 입력이 보장됨
    Output:
        - get_morse_code_dict 함수의 반환 값으로 인해 변환된 모스부호 문자열값
    Examples:
        # >>> import morsecode as mc
        # >>> mc.encoding_character("G")
        '--.'
        # >>> mc.encoding_character("A")
        '.-'
        # >>> mc.encoding_character("C")
        '-.-.'
        # >>> mc.encoding_character("H")
        '....'
        # >>> mc.encoding_character("O")
        '---'
        # >>> mc.encoding_character("N")
        '-.'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    # 모스 부호를 불러오기
    result = morse_code_dict[english_character.upper()]
    return result
    # ==================================


def decoding_sentence(morse_sentence):
    """
    Input:
        - morse_sentence : 문자열 값으로 모스 부호를 표현하는 문자열
    Output:
        - 모스부호를 알파벳으로 변환한 문자열
    Examples:
        # >>> import morsecode as mc
        # >>> mc.decoding_sentence("... --- ...")
        'SOS'
        # >>> mc.decoding_sentence("--. .- -.-. .... --- -.")
        'GACHON'
        # >>> mc.decoding_sentence("..  .-.. --- ...- .  -.-- --- ..-")
        'I LOVE YOU'
        # >>> mc.decoding_sentence("-.-- --- ..-  .- .-. .  ..-. ")
        'YOU ARE F'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_sentence_tmp = morse_sentence.strip().split("  ")
    # morse_sentence의 양 공백을 제거하고 더블스페이스를 기준으로 분리 (단어 간의 구분)
    english_sentence = []
    # english_word가 추가될 리스트
    for i in morse_sentence_tmp:
        morse_word_tmp = i.split(" ")
        # 스페이스를 기준으로 분리 (모스 부호 간의 구분)
        english_word = ""
        # decoding_character가 추가될 문자열
        for j in morse_word_tmp:
            # decoding_character 후 english_word에 추가
            english_word += decoding_character(j)
        english_sentence.append(english_word) # decoding된 단어를 english_sentence에 추가
    result = " ".join(english_sentence) # english_sentence에서 스페이스를 기준으로 결합
    return result
    # ==================================


def encoding_sentence(english_sentence):
    """
    Input:
        - english_sentence : 문자열 값으로 모스 부호로 변환이 가능한 영어문장
    Output:
        - 입력된 영어문장 문자열 값을 모스부호로 변환된 알파벳으로 변환한 문자열
          단 양쪽 끝에 빈칸은 삭제한다.
    Examples:
        # >>> import morsecode as mc
        # >>> mc.encoding_sentence("HI! Fine, Thank you.")
        '.... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-'
        # >>> mc.encoding_sentence("Hello! This is CS fifty Class.")
        '.... . .-.. .-.. ---  - .... .. ...  .. ...  -.-. ...  ..-. .. ..-. - -.--  -.-. .-.. .- ... ...'
        # >>> mc.encoding_sentence("We Are Gachon")
        '.-- .  .- .-. .  --. .- -.-. .... --- -.'
        # >>> mc.encoding_sentence("Hi! Hi!")
        '.... ..  .... ..'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    english_sentence_tmp = get_cleaned_english_sentence(english_sentence)
    # get_cleaned_english_sentence()를 사용하여 4개의 문장부호 ".,!?"를 삭제하고, 양쪽 끝 여백을 제거
    english_sentence_tmp = english_sentence_tmp.split()
    # 스페이스를 기준으로 분리 (단어 간의 구분)
    morse_sentence = []
    # morse_word가 추가될 리스트
    for i in english_sentence_tmp:
        morse_word = []
        # encoding_character가 추가될 리스트
        for j in i:
            # encoding_character 후 morse_word에 추가
            morse_word.append(encoding_character(j))
        morse_sentence.append(" ".join(morse_word))  # encoding된 단어를 스페이스를 기준으로 결합 후, morse_sentence에 추가
    result = "  ".join(morse_sentence)  # morse_sentence에 더블스페이스를 기준으로 결합
    return result
    # ==================================


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    while True:
        user_input = input("Input your message(H - Help, 0 - Exit): ")
        # 사용자의 입력을 받음
        if user_input == "0":
            # 사용자가 0을 입력하면 종료
            break
        elif is_help_command(user_input):
            # 사용자가 대소문자에 상관없이 "h"또는 "help"를 입력하면 get_help_message 함수를 호출
            print(get_help_message())
        elif is_validated_english_sentence(user_input):
            # 모스부호로 변환이 가능한 알파벳 문장이 입력되면 모스부호로 변환된 값이 출력
            print(encoding_sentence(user_input))
        elif is_validated_morse_code(user_input):
            # 알파벳으로 변환이 가능한 모스부호가 입력되면 알파벳으로 변환
            print(decoding_sentence(user_input))
        else:
            # 그외 변환이 불가능한 입력일 경우 에러 메세지를 출력
            print("Wrong Input")
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
