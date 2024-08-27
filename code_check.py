#@title
import sys, random, math, os, traceback, gspread, shutil, random
import pandas as pd
import numpy as np
from requests import get
# from oauth2client.service_account import ServiceAccountCredentials
from IPython.core.display import display, HTML
from jupyter_judge.question_bank.problem import *
from jupyter_judge.ColabTurtleClass import *
from PIL import Image
from google.colab import _frontend
import globals_variable

import warnings
warnings.filterwarnings(action='ignore')

# matplotlib에서 한글을 사용하기 위한 코드
# 나눔바른고딕을 git에 저장시켜서 다운로드하기. 그래야 나눔 폰트 다운로드에 시간 안씀.
# 폰트 크기 수정하기
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mpl.font_manager.fontManager.addfont('/content/jupyter_judge/NanumBarunGothic.ttf')
mpl.rcParams['font.family'] = 'NanumBarunGothic'
mpl.rcParams['axes.unicode_minus'] = False
mpl.rc('font', size = 14)
# addfont reference
# https://github.com/matplotlib/matplotlib/blob/v3.7.1/lib/matplotlib/font_manager.py#L1025-L1046
#------------------------------------------------------------------------------#

# 문서 이름을 ID로 불러오기
# 학생들이 문서이름을 ID로 만들어야 함.
# my_id = input('이름을 입력해주세요.')
print('지금부터 공부를 시작합니다.')
#------------------------------------------------------------------------------#
#문제 입력
#problem.py에 입력
#------------------------------------------------------------------------------#
#출력할 때 글씨 색
reset = '\033[0m'
tc_red = '\033[38;2;255;0;0m'
tc_green = '\033[38;2;0;255;0m'
bc_yellow = '\033[48;2;255;255;0m'
bc_green = '\033[48;2;0;255;0m'
bc_red = '\033[48;2;255;0;m'
bc_black = '\033[40m'
#------------------------------------------------------------------------------#
# JavaScript를 통해 Python 함수를 호출하는 HTML/JavaScript 코드 생성
def create_button_with_scratch_cell():
    global  attempts, question_info

    html_script = """
    <button onclick="createScratchCell()">문제 추천</button>
    <script>
    function createScratchCell() {
        // Python 함수를 호출하여 스크래치 코드 셀을 생성
        google.colab.kernel.invokeFunction('notebook.create_scratch_cell', [], {});
    }
    </script>
    """
    display_HTML(html_script)

    # Python 측에서 호출할 함수를 등록
    def create_scratch_cell():

        next_question = recommend_next_question(globals_variable.question_num, globals_variable.final_result, question_info, attempts)
        if next_question == '추천 문제가 없습니다.' : 
            _frontend.create_scratch_cell(f"#{next_question}.\n#노트북으로 돌아가세요.")            
        else : 
            _frontend.create_scratch_cell(f"#이 코드를 실행해주세요.\nQuestion('{next_question}')")

    output.register_callback('notebook.create_scratch_cell', create_scratch_cell)

global question_info
question_info = pd.read_csv('/content/jupyter_judge/question_bank/question_info.csv', dtype = {'id' : str, '1st_area' : str, '2nd_area' : str, 'difficulty' : int})

# 문제 추천 함수
def recommend_next_question(current_question_id, is_correct, df, wrong_attempts):
    current_question = df[df['id'] == current_question_id]

    if current_question.empty:
        return "추천 문제가 없습니다."

    area = current_question['1st_area'].iloc[0]
    sub_area = current_question['2nd_area'].iloc[0]
    difficulty = current_question['difficulty'].iloc[0]

    if is_correct:
        next_difficulty = min(difficulty + 1, 5)
        wrong_attempts = 0  # 정답 시 오답 카운트 초기화
    else:
        if wrong_attempts == 1:
            # 첫 번째 오답인 경우 같은 난이도 유지
            next_difficulty = difficulty
        else:
            # 두 번째 오답인 경우 난이도 감소 및 오답 카운트 초기화
            next_difficulty = max(difficulty - 1, 1)

    # 같은 난이도 내에서 다른 문제 추천 (첫 번째 오답)
    recommended_questions = df[(df['1st_area'] == area) &
                               (df['2nd_area'] == sub_area) &
                               (df['difficulty'] == next_difficulty) &
                               (df['id'] != current_question_id)].sample(n=1)

    if recommended_questions.empty:
        return "추천 문제가 없습니다."
    else : 
        return recommended_questions['id'].iloc[0]

#------------------------------------------------------------------------------#
global attempts
attempts = 0

result_df = pd.DataFrame(columns = ['id', 'question_file', 'final_result', 'total_attempts']) 

#------------------------------------------------------------------------------#
# 코드를 input/output 리스트에 넣기
def code_arrange(py_name) :
  global result, code, code_input, code_input_count
  result= []
  code = []
  code_input_count = 0
  code_input = []

  file_name = '/content/'+py_name

  f = open(file_name, 'r')  # '/content/____.py  << 이 부분은 함수 매개변수로 불러와야 함.
  lines = f.readlines()
  for line in lines :
    if line != '' :
      code.append(line)
      if line.find('input') >= 0 :
        code_input_count += 1
        code_input.append(code.index(line))
  f.close()

  for i in range(len(code)) :
    if code[i].find('\n') >= 0 :
      code[i] = code[i][:-1]
    code[i] = code[i].rstrip()

#------------------------------------------------------------------------------#
# 리스트에 있는 코드를 평가 코드로 수정하기
def code_convert(answer_input) :
  global test_py, answer_txt, original

  f = open(test_py, 'w')
  original = sys.stdout
  sys.stdout = f

  print('import sys')
  print(f"f = open('{answer_txt}', 'w')")
  print('original = sys.stdout')
  print('sys.stdout = f')
  try :
    order = 0
    count = 0

    for order in range(len(code)) :
      if order in code_input :
        if len(answer_input[test_count]['input'][code_input.index(order)]) == 1 :
          replace_input =  '"'+str(answer_input[test_count]['input'][code_input.index(order)][0])+'"'
          print(code[order].replace('input()',replace_input))

        else :
          replace_input =  str(answer_input[test_count]['input'][code_input.index(order)])
          print(code[order].replace('input().split()',replace_input))

      else :
        print(code[order])

    print('sys.stdout = original')
    print('f.close()')

    # 파이썬 코드로 실행해야 함. 원상복구
    sys.stdout = original
    f.close()
  except :
    print('sys.stdout = original')
    print('f.close()')

    sys.stdout = original
    f.close()

#------------------------------------------------------------------------------#

def code_test(answer_input) :
  global user_answer, answer_txt, test_count
  user_answer = []
  answer_filename = '/content/'+answer_txt
  f = open(answer_filename, 'r')
  lines = f.readlines()

  for line in lines :  # 결과를 문자열로 형태로 정답 리스트에 추가한다.
    line = line.strip()
    if line != '' :
      user_answer.append(str(line))
  f.close()

  answer_input[test_count]['output'] = list(map(str, answer_input[test_count]['output']))
  if user_answer == answer_input[test_count]['output'] :
    result.append(True)
  else :
    result.append(False)

#------------------------------------------------------------------------------#
# syntax 오류 외 코드 출력창에 코드 불러오는 것
# 틀린 코드에 빨간색 표시
def code_print(py_name) :
  global code
  file_name = '/content/'+py_name
  f = open(file_name, 'r')  # '/content/____.py  << 이 부분은 함수 매개변수로 불러와야 함.
  lines = f.readlines()
  error_count = error_line()
  code_count = 1

#   for line in lines[4:-2] :
  for line in lines[4:4+len(code)] :
    if error_count == code_count :
      print(tc_red+line[:-1]+reset)
      code_count += 1
    else :
      print(line[:-1])
      code_count += 1
  f.close()
#------------------------------------------------------------------------------#
# syntax 오류 코드 출력창에 코드 불러오는 것
# 틀린 코드에 빨간색 표시 없음
def code_print_syntax(py_name) :
  global code
  file_name = '/content/'+py_name
  f = open(file_name, 'r')  # '/content/____.py  << 이 부분은 함수 매개변수로 불러와야 함.
  lines = f.readlines()
  error_line()
  for line in lines[4:4+len(code)] :
  #for line in lines[4:-2] :
    print(line[:-1])
  f.close()
#------------------------------------------------------------------------------#
# syntax 외 오류 라인 검출
# 오류가 몇 번째 코드에서 발생했는지 번호 호출
def error_line() :
  global trace
  trace = traceback.format_exc()
  error = ''
  line = ''
  # print(trace)
  for i in trace.split('\n') :
    if i.find('string') >= 0 :
      error = i.strip()
  for i in error.split(',') :
    if i.find('line') >= 0 :
      line = i.strip()
  return int(line[line.find('e')+2:])-4
#------------------------------------------------------------------------------#
#에러에 따른 정보를 알려주는 함수
def name_error(test_py) :
  print(error_line(), '번째 줄에 정의되지 않은 변수가 있습니다.')
  print('또는 따옴표 없는 문자열입니까? 아니면 잘못 입력한 명령어입니까?')
  print("="*40)
  code_print(test_py)

def type_error(test_py) :
  print(error_line(), '번째 줄에 적절한 데이터 형태로 입력했나요?')
  print("="*40)
  code_print(test_py)

def attribute_error(test_py) :
  print(error_line(), '번째 줄에 라이브러리의 속성 또는 메서드를 바르게 입력했나요?')
  print("="*40)
  code_print(test_py)

def value_error(test_py) :
  print(error_line(), '번째 줄에 적절한 값을 입력했나요?')
  print("="*40)
  code_print(test_py)

def index_error(test_py) :
  print(error_line(), '번째 줄에서 시퀀스 자료형(리스트 등)의 길이를 초과했습니다.')
  print("="*40)
  code_print(test_py)

def key_error(test_py) :
  print(error_line(), '번째 줄에서 딕셔너리의 key를 찾을 수 없습니다. ')
  print("="*40)
  code_print(test_py)


def indentation_error(test_py) :
  print(error_line(), '번째 줄에 띄어쓰기를 확인해주세요.')
  print("="*40)
  code_print(test_py)

def zerodivision_error(test_py) :
  print(error_line(), '번째 줄에 숫자를 0으로 나누면 안되요.')
  print("="*40)
  code_print(test_py)

def overflow_error(test_py) :
  print(error_line(), '번째 줄에 너무 큰 수는 표현할 수 없어요')
  print("="*40)
  code_print(test_py)

def keyboard_interrupt(test_py) :
  print('사용자가 작동 정지함.')

def syntax_error(test_py) :
  global error_code
  # code_print_syntax(test_py)
  # code_print(test_py)
  error_code = []
  file_name = '/content/syntaxerror.txt'
  f = open(file_name, 'r') 
  lines = f.readlines()
  for line in lines :
    if line != '' :
      line = line.replace('\n', '')
      if line.find('SyntaxError') >= 0 : 
        line = line.replace('SyntaxError', '문법오류')
      error_code.append(line)
  f.close()

  error_code_line = int(error_code[-5][error_code[-5].find('line ')+5:])-4  
  print(error_code_line, '번째 줄에 문법오류입니다.')
  print("="*40) 
  print(tc_red+error_code[-4]+reset) 
  for line in error_code[-3: ] : 
    print(line)
def modulenotfound_error(test_py) :
  print(error_line(), '번째 줄에 라이브러리를 확인해주세요.')
  print("="*40)
  code_print(test_py)

def import_error(test_py) : 
  print(error_line(), '번째 줄에 import 하려는 라이브러리를 확인해주세요.' )
  print("="*40)
  code_print(test_py)

def else_error(test_py) :
  print(error_line(), '번째 줄에 오류가 있습니다.')
  print("="*40)
  code_print(test_py)

def error_check(test_py) :
  global compile_error, original, trace, error_code, df, df_answer
  df = ''
  df_answer = ''
  compile_error = False
  try :
    exec(open(test_py).read())
    return df
  except NameError :
    sys.stdout = original
    name_error(test_py)
    compile_error = True
    return
  except TypeError as typeerror:

    sys.stdout = original
    type_error(test_py)
    compile_error = True
    print('오류메세지 : ',bc_black+str(typeerror)+reset)
    #에러 메세지 txt 파일로 저장
    #여기서 오류가 난 코드와 원인 출력
    sys.stdout = original
    f = open('typeerror.txt', 'w')
    original = sys.stdout
    sys.stdout = f
    print(trace)
    f.close()
    sys.stdout = original

    return
  except AttributeError :
    sys.stdout = original
    attribute_error(test_py)
    compile_error = True
    return
  except ValueError as valueerror :
    sys.stdout = original
    value_error(test_py)
    compile_error = True
    print('오류메세지 : ',bc_black+str(valueerror)+reset)   
    return
  except IndexError :
    sys.stdout = original
    index_error(test_py)
    compile_error = True
    return
  except KeyError :
    sys.stdout = original
    key_error(test_py)
    compile_error = True
    return
  except IndentationError :
    sys.stdout = original
    indentation_error(test_py)
    compile_error = True
    return
  except ZeroDivisionError :
    sys.stdout = original
    zerodivision_error(test_py)
    compile_error = True
    return
  except OverflowError :
    sys.stdout = original
    overflow_error(test_py)
    compile_error = True
    return
  except KeyboardInterrupt :
    sys.stdout = original
    keyboard_interrupt(test_py)
    compile_error = True
    return
  except SyntaxError as syntax :
    trace = traceback.format_exc()
    sys.stdout = original
    f = open('syntaxerror.txt', 'w')
    original = sys.stdout
    sys.stdout = f
    print(trace)
    f.close()
    sys.stdout = original

    syntax_error(test_py)



    compile_error = True  
    # for i in code[-4:] : 
    #   if i.find('SyntaxError') >= 0 : 
    #     i = i.replace('SyntaxError', '문법오류')
    #   print(i)


    # print('오류메세지 : ',bc_black+str(valueerror)+reset)    
    return
  except ModuleNotFoundError :
    sys.stdout = original
    modulenotfound_error(test_py)
    compile_error = True
    return
  except ImportError :
    sys.stdout = original
    import_error(test_py)
    compile_error = True
    return    
  except :
    sys.stdout = original
    else_error(test_py)
    compile_error = True
    return

#------------------------------------------------------------------------------#
#HTML 형식의 문제 불러오기기
def display_HTML(question_) :
  display(HTML(question_))
#------------------------------------------------------------------------------#
#코드의 정답 여부를 확인하는 함수
def code_check(py) :
  global attempts
  attempts +=1
    
  for i in range(len(test_set)) :
    if test_set[i]['test_file'] == py :
      global answer
      answer = test_set[i]['answer']
      global question
      question = test_set[i]['question']
  # trial_error_count[py] += 1
  try :
    code_arrange(py)
  except :
    print('평가 코드를 생성하세요.')
    return
  if code_input_count :
    if code_input_count != len(answer[0]['input']) :
      # update_excel('입력 오류', py)
      print('입력을 확인해주세요.')
      return

  display_HTML('<h2 style = "background-color:yellow">결과 확인</h2>')

  global test_count
  for test_count in range(len(answer)) :
    global test_py, answer_txt
    test_py = 'test'+str(test_count)+'.py'
    answer_txt = 'answer'+str(test_count)+'.txt'
    code_convert(answer)
    error_check(test_py)
    # 코드 실행 시 오류발생하면 확인 종료
    if compile_error == True :
      try :
        # update_excel('오류입니다.', py)
        return
      except :
        return

    code_test(answer)
    #입력이 없는 문제
    if len(answer[0]['input']) == 0 :
      if result[test_count] == True :
        display_HTML('<li>처리한 데이터 : </li>')
        for i in user_answer :
          if i == user_answer[-1] :
            print(bc_yellow+str(i)+reset,tc_green+'O'+reset)
          else :
            print(bc_yellow+str(i)+reset)
      else :
        display_HTML('<li>처리한 데이터 : </li>')
        for i in user_answer :
          if i == user_answer[-1] :
            print(bc_yellow+str(i)+reset, tc_red+'X'+reset)
          else :
            print(bc_yellow+str(i)+reset)
    else :
    #입력이 있는 문제
      if result[test_count] == True :
        display_HTML('<li>입력한 데이터 : </li>')
        for i in answer[test_count]['input'] :
          if len(i) == 1 :
            print(i[0])
          else :
            for j in i :
              if j == i[-1] :
                print(j, end = '\n')
              else :
                print(j, end = ' ')

        # for i in answer[test_count]['input'] : print(i)
        display_HTML('<li>처리한 데이터 : </li>')
        for i in user_answer :
          if i == user_answer[-1] :
            print(bc_yellow+str(i)+reset, tc_green+'O'+reset)
          else :
            print(bc_yellow+str(i)+reset)
      else :
        display_HTML('<li>입력한 데이터 : </li>')
        for i in answer[test_count]['input'] :
          if len(i) == 1 :
            print(i[0])
          else :
            for j in i :
              if j == i[-1] :
                print(j, end = '\n')
              else :
                print(j, end = ' ')

        display_HTML('<li>처리한 데이터 : </li>')
        for i in user_answer :
          if i == user_answer[-1] :
            print(bc_yellow+str(i)+reset,tc_red+'X'+reset)
          else :
            print(bc_yellow+str(i)+reset)
    display_HTML('<HR>')
  if sum(result) == test_count+1 :
    globals_variable.final_result = True  
    attempts = 0  
    print(globals_variable.question_name_data)
    print(tc_green+'정답입니다.'+reset)
  else :
    globals_variable.final_result = False  
    print(tc_red+'틀렸습니다.'+reset)
      
  if globals_variable.question_num in list(result_df['id']):
    result_df[result_df['id'] == globals_variable.question_num] = [globals_variable.question_num, question_name if globals_variable.question_name in globals() else globals_variable.question_name_data, globals_variable.final_result, globals_variable.total_attempts]
  else : 
    result_df.loc[len(result_df)] = [globals_variable.question_num, question_name if globals_variable.question_name in globals() else globals_variable.question_name_data, globals_variable.final_result, globals_variable.total_attempts]

  create_button_with_scratch_cell()

#------------------------------------------------------------------------------#
#터틀 평가 함수
def turtle_arrange(py) :
  global code
  code = []

  file_name = '/content/'+py

  f = open(file_name, 'r')
  lines = f.readlines()
  for line in lines :
    if line != '' :
      code.append(line)
  f.close()

  for i in range(len(code)) :
    if code[i].find('\n') >= 0 :
      code[i] = code[i][:-1]
    code[i] = code[i].rstrip()

def turtle_convert(output_turtle) :
  global code
  global answer_turtle
  global original
  f = open(output_turtle, 'w')
  original = sys.stdout
  sys.stdout = f
  print('#---코드 변환---')
  print('from jupyter_judge.ColabTurtleClass import Turtle, Window')
  print('window = Window()')
  print('s = Turtle(window)')
  for i in range(len(code)) :
    print(code[i])

  for i in answer_turtle :
    print(i)
  sys.stdout = original
  f.close()


def turtle_check(py) :
  global original
  # trial_error_count[py] += 1
  for i in range(len(test_set)) :
    if test_set[i]['test_file'] == py :
      global answer, answer_turtle
      answer = test_set[i]['answer']
      answer_turtle = answer[0]['output']
      global question
      question = test_set[i]['question']
  try :
    turtle_arrange(py)
  except :
    print('평가 코드를 생성하세요.')
    return
  turtle_convert('turtle_output.py')
  display_HTML('''<h3><p><span style="color:blue">파란색 도형</span>은 여러분이 작성한 코드로 그린 도형입니다.</p><p><span style="color:red">빨간색 도형</span>은 선생님이 작성한 코드로 그린 도형입니다.</p></h3>''')
  #error_check에서 파일을 실행함. 이후 또 실행하면 터틀이 2번 그려짐. 그래서 error_check에서 에러검사 및 실행을 함.(정상 실행되면 그냥 실행함.)
  error_check('turtle_output.py')
  create_button_with_scratch_cell()
  
#------------------------------------------------------------------------------#
from google.colab import output
# 그래프에서 평가 정보를 얻는 것은 info, 평가하는 그래프 종류는 pyplot, 정답과 관련된 것은 A_ 접두사를 붙임.
plot_info= ['pie', 'scatter', 'barh', 'bar', 'hist', 'hlines', 'vlines', 'plot', 'title', 'xlabel', 'ylabel', 'xlim', 'ylim', 'legend']
A_plot_info = ['A_pie', 'A_boxplot', 'A_scatter', 'A_barh', 'A_bar', 'A_hist', 'A_hlines', 'A_vlines', 'A_plot', 'A_title', 'A_xlabel', 'A_ylabel', 'A_xlim', 'A_ylim', 'A_legend']

plot_pyplot = ['pie', 'scatter','barh', 'bar', 'hist', 'hlines', 'vlines', 'plot']
A_plot_pyplot = ['A_pie', 'A_scatter', 'A_barh', 'A_bar', 'A_hist', 'A_hlines', 'A_vlines', 'A_plot']

plot_kind = []
A_plot_kind = []
plot_kind_code = []
A_plot_kind_code = []
code = []
code_dict = {}

def plot_arrange(py) :

  global code_dict
  global code

  file_name = '/content/'+py

  # 코드에서 공백제거고 code에 리스트로 저장하기.
  f = open(file_name, 'r')
  lines = f.readlines()
  for line in lines :
    if line != '' :
      code.append(line)
  f.close()

  # code 리스트에서 \n 개행문자 제거하기
  for i in range(len(code)) :
    if code[i].find('\n') >= 0 :
      code[i] = code[i][:-1]
    code[i] = code[i].rstrip()

  #code 리스트에서 plt.show() 제거하기 < 그렇지 않으면 그래프가 같은 행에 나오지 않음.
  for i in code :
    if i.find('show()') >= 0 :
      code.remove(i)



def plot_convert(output_plot) :

  global code
  global answer_plot
  global original
  global compile_error

  f = open(output_plot, 'w')
  original = sys.stdout
  sys.stdout = f
  print('import matplotlib.pyplot as plt')
  print('from PIL import Image')
  print('plt.figure(figsize = (16,8))')
  print('plt.subplot(1,2,1)')

  for i in range(len(code)) :
    print(code[i])
  print('plt.savefig("submit.png")')

  for i in answer_plot :
    print(i)
  sys.stdout = original
  f.close()



# 함수에 정보를 주기 위 한 함수.

def plot_feedback(A_plot_kind) :
  global pie_text, pie_autotext, box_data, scatter_offset, barh_data, bar_data, hist_data, hlines_data, vlines_data, plot_data, plot_mcl
  global plot_title, plot_xlabel, plot_ylabel, plot_xlim, plot_ylim, plot_legend

  global A_pie_text, A_pie_autotext, A_box_data, A_scatter_offset, A_barh_data, A_bar_data, A_hist_data, A_hlines_data, A_vlines_data, A_plot_data, A_plot_mcl
  global A_plot_title, A_plot_xlabel, A_plot_ylabel, A_plot_xlim, A_plot_ylim, A_plot_legend

  for i in set(A_plot_kind) :
    if i == 'pie' :
      if pie_text != A_pie_text : display_HTML('원 그래프의 <b>labels</b>가 틀렸습니다.') #print('원 그래프의 labels이 틀렸습니다.')
      if pie_autotext != A_pie_autotext : display_HTML('원 그래프의 <b>x값</b>이 틀렸습니다.') #print('원 그래프의 x값이 틀렸습니다.')
      # print('pie label :', pie_text == A_pie_text)
      # print('pie x값 :', pie_autotext == A_pie_autotext)
      # print('label : ', pie_text[i], A_pie_text[i])
      # print('x값 : ', pie_autotext[i], A_pie_autotext[i])
    elif i == 'boxplot' :
      if not np.array_equal(box_data, A_box_data) : display_HTML('상자 그림의 <b>x값</b>이 틀렸습니다.') #print('boxplot의 x값이 틀렸습니다.')
      # print('box_data : ',np.array_equal(box_data, A_box_data))

    elif i == 'scatter' :
      if not np.array_equal(scatter_offset,A_scatter_offset) : display_HTML('산점도의 <b>x값, y값</b>이 틀렸습니다.') #print('scatter의 x값, y값이 틀렸습니다.')
      # print('scatter 데이터 :', np.array_equal(scatter_offset,A_scatter_offset))  # 해결
      # print('scatter : ', scatter_offset[i], A_scatter_offset[i])
    elif i == 'barh' :
      if barh_data != A_barh_data : display_HTML('막대 그래프의 <b>값</b>이 틀렸습니다.') #print('막대그래프의 x값이 틀렸습니다.')
      # print('막대 그래프 데이터 :', bar_data == A_bar_data)  # 해결
      # print('bar : ', bar_data, A_bar_data)
    elif i == 'bar' :
      if bar_data != A_bar_data : display_HTML('막대 그래프의 <b>값</b>이 틀렸습니다.') #print('막대그래프의 x값이 틀렸습니다.')
      # print('막대 그래프 데이터 :', bar_data == A_bar_data)  # 해결
      # print('bar : ', bar_data, A_bar_data)
    elif i == 'hist' :
      if str(hist_data) != str(A_hist_data) : display_HTML('히스토그램의 <b>x값</b>이 틀렸습니다.') #print('히스토그램의 x값이 틀렸습니다.')
      # print('히스토그램 데이터 :', str(hist_data) == str(A_hist_data))  # 이것도 길다...
      # print('hist : ', hist_data[i], A_hist_data[i])
    elif i == 'hlines' :
      if not np.array_equal(hlines_data, A_hlines_data) : display_HTML('수평선의 <b>y, xmin, xmax값</b>이 틀렸습니다.') #print('수평선의 y, xmin, xmax값이 틀렸습니다.')
      # print('수평선 :', np.array_equal(hlines_data, A_hlines_data))
      # print('hlines : ', hlines_data[i], A_hlines_data[i])
    elif i == 'vlines' :
      if not np.array_equal(vlines_data, A_vlines_data) : display_HTML('수직선의 <b>x, ymin, ymax값</b>이 틀렸습니다.') #print('수직선의 x, ymin, ymax값이 틀렸습니다.')
      # print('수직선 :', np.array_equal(vlines_data, A_vlines_data))
      # print('vlines : ', vlines_data[i], A_vlines_data[i])
    elif i == 'plot' :
      if not np.array_equal(plot_data, A_plot_data) : display_HTML('plot의 <b>데이터</b>가 틀렸습니다.') #print('plot의 데이터가 틀렸습니다.')
      if not np.array_equal(plot_mcl, A_plot_mcl) : display_HTML('plot의 <b>마커, 색, 선 종류</b>가 틀렸습니다.') #print('plot의 마커, 색, 선종류가 틀렸습니다.')
      # print('plot 데이터 :', np.array_equal(plot_data, plot_data))
      # print('plot 마커, 색, 선 :', np.array_equal(plot_mcl, A_plot_mcl))
      # print('데이터 : ', plot_data[i], A_plot_data[i])
      # print('마커 등 : ', plot_mcl[i], A_plot_mcl[i])

  if A_plot_title != '' :
    if A_plot_title != plot_title : display_HTML('<b>title</b>이 틀렸습니다.') #print('title이 틀렸습니다.')
    # print('제목 :',A_plot_title == plot_title)
  if A_plot_xlabel != '' :
    if A_plot_xlabel != plot_xlabel : display_HTML('<b>xlabel</b>이 틀렸습니다.') #print('xlabel이 틀렸습니다.')
    # print('x축 이름 :', A_plot_xlabel == plot_xlabel)
  if A_plot_ylabel != '' :
    if A_plot_ylabel != plot_ylabel : display_HTML('<b>ylabel</b>이 틀렸습니다.') #print('ylabel이 틀렸습니다.')
    # print('y축 이름 :', A_plot_ylabel == plot_ylabel)
  if A_plot_xlim != '' :
    if A_plot_xlim != plot_xlim : display_HTML('<b>xlim</b>이 틀렸습니다.') #print('xlim이 틀렸습니다.')
    # print('x축 범위 :', A_plot_xlim == plot_xlim)
  if A_plot_ylim != '' :
    if A_plot_ylim != plot_ylim : display_HTML('<b>ylim</b>이 틀렸습니다.') #print('ylim이 틀렸습니다.')
    # print('y축 범위 :', A_plot_ylim == plot_ylim)
  if A_plot_legend != '' :
    if str(A_plot_legend) != str(plot_legend) : display_HTML('<b>legend</b>가 틀렸습니다.') #print('legend가 틀렸습니다.')
    # print('범례 :', str(A_plot_legend) == str(plot_legend))
  # print('title :', plot_title, A_plot_title)
  # print('xlabel :', plot_xlabel, A_plot_xlabel)
  # print('ylabel :', plot_ylabel, A_plot_ylabel)
  # print('xlim :', plot_xlim, A_plot_xlim)
  # print('ylim :', plot_ylim, A_plot_ylim)
  # print('legend :', plot_legend, A_plot_legend)

def get_return(info) :
  global pie_text, pie_autotext, box_data, scatter_offset, barh_data, bar_data, hist_data, hlines_data, vlines_data, plot_data, plot_mcl
  global plot_title, plot_xlabel, plot_ylabel, plot_xlim, plot_ylim, plot_legend

  global A_pie_text, A_pie_autotext, A_box_data, A_scatter_offset, A_barh_data, A_bar_data, A_hist_data, A_hlines_data, A_vlines_data, A_plot_data, A_plot_mcl
  global A_plot_title, A_plot_xlabel, A_plot_ylabel, A_plot_xlim, A_plot_ylim, A_plot_legend

  if info == 'pie' :
    pie_text.append([globals()['_pie'][1][i].get_text() for i in range(len(globals()['_pie'][1]))])
    pie_autotext.append([globals()['_pie'][2][i].get_text() for i in range(len(globals()['_pie'][2]))])
  elif info == 'boxplot' :
    box_data.append([globals()['_boxplot']['boxes'][0].get_data()[1][1], globals()['_boxplot']['boxes'][0].get_data()[1][2], globals()['_boxplot']['medians'][0].get_data()[1][0]])    #[_boxplot['boxes'][0].get_data()[1][1], _boxplot['boxes'][0].get_data()[1][2], _boxplot['medians'][0].get_data()[1][0]]
  elif info == 'scatter' :
    scatter_offset.append(globals()['_scatter'].get_offsets())  # np.array_equal(_scatter_offset,A_scatter_offset) << 형태로 일치 여부 확인
  elif info == 'barh' :   #높이 값을 구할 수 있음, x 값은 아직,
    barh_data.append(list(globals()['_barh'].datavalues))     # array를 list로 변환
  elif info == 'bar' :   #높이 값을 구할 수 있음, x 값은 아직,
    bar_data.append(list(globals()['_bar'].datavalues))     # array를 list로 변환
  elif info == 'hist' :
    hist_data.append([globals()['_hist'][0], globals()['_hist'][1]])  #값  이거 len 한게 bins
  elif info == 'hlines' :
    hlines_data.append(globals()['_hlines'].get_segments()[0]) # np.array_equal(A,B) 형태로 비교
  elif info == 'vlines' :
    vlines_data.append(globals()['_vlines'].get_segments()[0])
  elif info == 'plot' :
    plot_data.append(globals()['_plot'][0].get_data())
    plot_mcl.append([globals()['_plot'][0].get_marker(), globals()['_plot'][0].get_color(), globals()['_plot'][0].get_linestyle()])
  elif info == 'title' :
    plot_title = globals()['_title'].get_text()
  elif info == 'xlabel' :
    plot_xlabel = globals()['_xlabel'].get_text()
  elif info == 'ylabel' :
    plot_ylabel = globals()['_ylabel'].get_text()
  elif info == 'xlim' :
    plot_xlim = globals()['_xlim']
  elif info == 'ylim' :
    plot_ylim = globals()['_ylim']
  elif info == 'legend' :
    plot_legend = list(globals()['_legend'].get_texts())
  elif info == 'A_pie' :
    A_pie_text.append([globals()['A_pie'][1][i].get_text() for i in range(len(globals()['A_pie'][1]))])
    A_pie_autotext.append([globals()['A_pie'][2][i].get_text() for i in range(len(globals()['A_pie'][2]))])
  elif info == 'A_boxplot' :
    A_box_data.append([globals()['A_boxplot']['boxes'][0].get_data()[1][1], globals()['A_boxplot']['boxes'][0].get_data()[1][2], globals()['A_boxplot']['medians'][0].get_data()[1][0]])
  elif info == 'A_scatter' :
    A_scatter_offset.append(globals()['A_scatter'].get_offsets())   #boxplot 검토 필요, 1분위, 3분위 값만 저장
  elif info == 'A_barh' :   #높이 값을 구할 수 있음, x 값은 아직,
    A_barh_data.append(list(globals()['A_barh'].datavalues))     # array를 list로 변환
  elif info == 'A_bar' :   #높이 값을 구할 수 있음, x 값은 아직,
    A_bar_data.append(list(globals()['A_bar'].datavalues))     # array를 list로 변환
  elif info == 'A_hist' :
    A_hist_data.append([globals()['A_hist'][0], globals()['A_hist'][1]])  #값  이거 len 한게 bins
  elif info == 'A_hlines' :
    A_hlines_data.append(globals()['A_hlines'].get_segments()[0])
  elif info == 'A_vlines' :
    A_vlines_data.append(globals()['A_vlines'].get_segments()[0])
  elif info == 'A_plot' :
    A_plot_data.append(globals()['A_plot'][0].get_data())
    A_plot_mcl.append([globals()['A_plot'][0].get_marker(), globals()['A_plot'][0].get_color(), globals()['A_plot'][0].get_linestyle()])
  elif info == 'A_title' :
    A_plot_title = globals()['A_title'].get_text()
  elif info == 'A_xlabel' :
    A_plot_xlabel = globals()['A_xlabel'].get_text()
  elif info == 'A_ylabel' :
    A_plot_ylabel = globals()['A_ylabel'].get_text()
  elif info == 'A_xlim' :
    A_plot_xlim = globals()['A_xlim']
  elif info == 'A_ylim' :
    A_plot_ylim = globals()['A_ylim']
  elif info == 'A_legend' :
    A_plot_legend = list(globals()['A_legend'].get_texts())
  else :
    print('피드백 제외')


def plot_check(py) :
  file_list = os.listdir("/content/")
  for file in file_list:    
    if file == 'submit.png' : 
      os.remove("/content/submit.png")

  # 피드백을 주기 위해 그래프에 설명을 넣기 위한 변수들
  global pie_text, pie_autotext, box_data, scatter_offset, barh_data, bar_data, hist_data, hlines_data, vlines_data, plot_data, plot_mcl
  global plot_title, plot_xlabel, plot_ylabel, plot_xlim, plot_ylim, plot_legend

  global A_pie_text, A_pie_autotext, A_box_data, A_scatter_offset, A_barh_data, A_bar_data, A_hist_data, A_hlines_data, A_vlines_data, A_plot_data, A_plot_mcl
  global A_plot_title, A_plot_xlabel, A_plot_ylabel, A_plot_xlim, A_plot_ylim, A_plot_legend

  #plot_check() 실행할 때마다 초기화해야 함. append를 사용하므로 그래야 쌓이지 않음.
  pie_text = []
  A_pie_text = []
  pie_autotext = []
  A_pie_autotext = []

  box_data = []
  A_box_data = []

  scatter_offset = []
  A_scatter_offset = []

  barh_data = []
  A_barh_data = []
  bar_data = []
  A_bar_data = []

  hist_data = []
  A_hist_data = []
  hlines_data = []
  A_hlines_data = []
  vlines_data = []
  A_vlines_data = []
  plot_data = []
  A_plot_data = []
  plot_mcl = []
  A_plot_mcl = []

  plot_title = ''
  A_plot_title = ''
  plot_xlabel = ''
  A_plot_xlabel = ''
  plot_ylabel = ''
  A_plot_ylabel = ''
  plot_xlim = ''
  A_plot_xlim = ''
  plot_ylim = ''
  A_plot_ylim = ''
  plot_legend = ''
  A_plot_legend = ''

  global code, plot_kind, A_plot_kind, code_dict, plot_kind_code, A_plot_kind_code
  code = []
  code_dict = {}
  plot_kind = []
  A_plot_kind = []

  #정보를 얻기 위함. get_return 함수를 plot_check 안에다가 만듬.

  #정답 코드 가져오는것
  answer_graph = '/content/jupyter_judge/graph/answer'+py[:-3]+'.png'
  review = 'question'+'_review'+py[:-3]
  global original
  # trial_error_count[py] += 1
  for i in range(len(test_set)) :
    if test_set[i]['test_file'] == py :
      global answer, answer_plot
      answer = test_set[i]['answer']
      answer_plot = answer[0]['output']
      global question
      question = test_set[i]['question']
  try :
    plot_arrange(py)
  except :
    print('평가 코드를 생성하세요.')
    return

  plot_convert('plot_output.py')

  code = []
  # 변환한 코드를 불러와서 code 리스트에 넣기
  file_name =  '/content/'+'plot_output.py'
  f = open(file_name, 'r')
  lines = f.readlines()
  for line in lines :
    if line != '' :
      if line.find('\n') >= 0 :
        line = line[:-1]
        code.append(line.rstrip())
      else :
        line = line.rstrip()
        code.append(line)
  f.close()

  # 그래프에서 정보를 얻어오면 안되는 것들
  plot_not = ['matplotlib', 'pyplot', 'subplot']

  # 어떤 그래프를 그렸는지 알기

  for i in range(len(code)) :

    if code[i].find('plt') >= 0 and code[i].find('A_') == 0 :
      for j in plot_pyplot :
        if code[i].find(j) >= 0 :  # 여기서  bar, barh 둘 중 하나만 나오도록 해야함.
          if  code[i].find('boxplot') >= 0 :
            A_plot_kind.append('boxplot')
          elif  (code[i].find('h') >=0) and (code[i].find('h') - code[i].find('barh')==3) :
            if j == 'barh' : 
              A_plot_kind.append('barh')
          # elif  (code[i].find('h') >=0) and (code[i].find('h') - code[i].find('barh')!=3) :
          #   A_plot_kind.append('bar')
          else :
            A_plot_kind.append(j)
            A_plot_kind_code.append(code[i])
    elif code[i].find('plt') >= 0 and code[i].find(plot_not[0]) == -1 and code[i].find(plot_not[1]) == -1 and code[i].find(plot_not[2]) == -1  :
      for j in plot_pyplot :
        if code[i].find(j) >= 0 :
          if code[i].find('boxplot') >= 0 :
            plot_kind.append('boxplot')
          elif (code[i].find('h') >= 0) and (code[i].find('h') - code[i].find('barh') == 3) :
            if j == 'barh' : 
              plot_kind.append('barh')
          # elif (code[i].find('h') >= 0) and (code[i].find('h') - code[i].find('barh') != 3) :
          #   plot_kind.append('bar')
          else :
            plot_kind.append(j)
            plot_kind_code.append(code[i])


  #code에서 code_dict에 값 넣기

  for i in range(len(code)) :

    if code[i].find('A_') == 0 :
      for j in A_plot_info :
        if code[i].find(j) >= 0  :
          if code[i].find('boxplot') >= 0:
            code_dict[code[i]] = 'A_boxplot'
          elif code[i].find('barh') >= 0:
            code_dict[code[i]] = 'A_barh'
          else :
            code_dict[code[i]] = j
    elif code[i].find('plt') >= 0 :
      for j in plot_info :
        if code[i].find(j) >= 0 and code[i].find(plot_not[0]) == -1 and code[i].find(plot_not[1]) == -1 and code[i].find(plot_not[2]) == -1  and not code[i].find('A_') == 0:
          if code[i].find('boxplot') >= 0 :
            code_dict['_boxplot='+code[i]] = 'boxplot'
            code[i] = '_boxplot='+code[i]
          elif code[i].find('barh') >= 0 :
            code_dict['_barh='+code[i]] = 'barh'
            code[i] = '_barh='+code[i]
          else :
            code_dict['_'+j+'='+code[i]] = j
            code[i] = '_'+j+'='+code[i]



  display_HTML('''
  <h3 style = "float:left;width:50%" >왼쪽 그래프는 여러분이 작성한 그래프입니다. </h3>
  <h3 style = "float:right;width:50%" >오른쪽 그래프는 예시 답안입니다. </h3>
  ''')

  # 기존에는 코드 전체를 실행시켰다면 이번에는 코드 한 줄씩 실행시킴.
  # 한 줄 실행시키고 정보를 얻고, 한 줄 실행시키고 정보를 얻고, 오류 발생하면 출력한 것 삭제하고 오류 발생 보여주고 이렇게 함.

  global compile_error
  compile_error = False

  for i in code :
    try :
      exec(i, globals())
      if i in list(code_dict.keys()) :
        get_return(code_dict[i])
    except NameError :
      plt.clf()
      # output.clear()
      print('오류가 있는 코드 :',tc_red,i,reset)
      print('명령어 이름을 확인하거나 문자열에 따옴표가 붙어 있는지 확인하세요. ')
      compile_error = True
      break
    except TypeError :
      plt.clf()
      # output.clear()
      print('오류가 있는 코드 :',tc_red,i,reset)
      print('숫자나 문자를 바르게 입력하세요')
      compile_error = True
      break
    except AttributeError :
      plt.clf()
      # output.clear()
      print('오류가 있는 코드 :',tc_red,i,reset)
      print('라이브러리 속성 또는 메서드를 바르게 입력하세요.')
      compile_error = True
      break
    except ValueError :
      plt.clf()
      # output.clear()
      print('오류가 있는 코드 :',tc_red,i,reset)
      print('입력할 때 숫자나 문자를 바르게 입력하세요')
      compile_error = True
      break
    except IndexError :
      plt.clf()
      # output.clear()
      print('오류가 있는 코드 :',tc_red,i,reset)
      print('리스트나 튜플의 길이를 확인하세요.')
      compile_error = True
      break
    except IndentationError :
      plt.clf()
      # output.clear()
      print('오류가 있는 코드 :',tc_red,i,reset)
      print('띄어쓰기를 확인하세요.')
      compile_error = True
      break
    except ZeroDivisionError :
      plt.clf()
      # output.clear()
      print('오류가 있는 코드 :',tc_red,i,reset)
      print('숫자를 0으로 나누었는지 확인하세요.')
      compile_error = True
      break
    except OverflowError :
      plt.clf()
      # output.clear()
      print('오류가 있는 코드 :',tc_red,i,reset)
      print('너무 큰 수는 표현할 수 없습니다.')
      compile_error = True
      break
    except KeyboardInterrupt :
      plt.clf()
      # output.clear()
      print('사용자가 작동 중지함.')

    except SyntaxError :
      plt.clf()
      # output.clear()
      print('오류가 있는 코드 :',tc_red,i,reset)
      print('문법 오류입니다. 명령어, :, () 등을 확인하세요.')
      compile_error = True
      break
    except ModuleNotFoundError :
      plt.clf()
      # output.clear()
      print('오류가 있는 코드 :',tc_red,i,reset)
      print('라이브러리를 확인하세요.')
      compile_error = True
      break
    except :
      plt.clf()
      # output.clear()
      print('오류가 있는 코드 :',tc_red,i,reset)
      print('코드 오류입니다.')
      compile_error = True
      break

  display_HTML(eval(review))
  display_HTML('<HR>')
  try :
    img_submit = np.asarray(Image.open("/content/submit.png"))
    img_answer = np.asarray(Image.open(answer_graph))

    if np.array_equal(img_submit, img_answer) :
    # print(tc_green+'정답입니다.'+reset)
      display_HTML('<h3 style = "color:green; ">정답입니다.</h2>')
      # input('그래프를 보고 알 수 있는 내용을 적어봅시다.')
    else :
     # print(tc_red+'오답입니다.'+reset)
      display_HTML('<h3 style = "color:red; ">오답입니다.</h2>')
      plot_feedback(A_plot_kind)

  except : 
    print('그래프가 생성되지 않았습니다.')

  create_button_with_scratch_cell()


  # if compile_error == True :
    # update_excel('틀렸습니다.',py)
  # else :
    # update_excel('정답입니다.', py)
###
global df, df_answer

#___________________________________________#
###  판다스 평가 도구

# 전처리 함수

def table_arrange(py) :
  global raw_code, code
  raw_code = []
  code = []
  
  file_name = '/content/'+py

  # 코드에서 공백제거고 code에 리스트로 저장하기.
  f = open(file_name, 'r')
  lines = f.readlines()
  for line in lines :
    if line != '' :
      raw_code.append(line)
  f.close()

  # code 리스트에서 \n 개행문자 제거하기
  for i in range(len(raw_code)) :
    if raw_code[i].find('\n') >= 0 :
      raw_code[i] = raw_code[i][:-1]
    raw_code[i] = raw_code[i].rstrip()

  #code 리스트에서 df, print(df), display(df) 제거하기
  for i in raw_code :
    if i != 'df' and i != 'print(df)' and i != 'display(df)':
      code.append(i)


def table_convert(output_table) :

  global code
  global answer_table
  global original

  f = open(output_table, 'w')
  original = sys.stdout
  sys.stdout = f
  print('import pandas as pd')
  print('import numpy as np')
  print('from IPython.display import display, HTML')
  print('global df, df_answer')  # 변수를 전역으로 선언해야 함! ~ 아마 시각화 함수에서도 비슷했을 것 같음.

  for i in range(len(code)) :
    print(code[i])

  for i in answer_table :
    print(i)
  sys.stdout = original
  f.close()

table_count = 0
def table_compare(x, df_answer, color='#fffacd') :
  global table_count
  # print(count)
  if type(df_answer) == pd.core.series.Series : 
    df_answer = df_answer.to_frame()
  row = df_answer.shape[0]
  col = df_answer.shape[1]
  new_row = table_count % row
  new_col = table_count // row
  table_count += 1
  # print(f'new_row : {new_row}')
  # print(f'new_col : {new_col}')
  # print(f'x : {x}')
  # print(f'df_answer.iloc[new_row, new_col] : {df_answer.iloc[new_row, new_col]}')
  if x != df_answer.iloc[new_row, new_col]:
    color = f'background-color:{color}'
    return color
  else :
    return ''
#df.style.applymap(table_compare) <- 이런 형태로 출력함.



def table_check(py) :
  global code, raw_code
  global original
  global compile_error
  global df, df_answer
  df, df_answer = '', ''
  compile_error = False

  code = []
  raw_code = []

  # trial_error_count[py] += 1
  for i in range(len(test_set)) :
    if test_set[i]['test_file'] == py :
      global answer, answer_table
      answer = test_set[i]['answer']
      answer_table = answer[0]['output']
      global question
      question = test_set[i]['question']
  try :
    table_arrange(py)
  except :
    print('평가할 코드를 작성하세요.')
    return
  table_convert('table_output.py')
  error_check('table_output.py')


  if type(df) != type(df_answer) :
    print('Type is different.')
  elif type(df) == pd.core.frame.DataFrame and type(df_answer) == pd.core.frame.DataFrame :
    display_HTML('<h2 style = "background-color:yellow">결과 확인</h2>')
  # 결과 자가 평가
    df_answer_html = df_answer.to_html(max_cols = 5, max_rows =5, show_dimensions = True)
    df_html = df.to_html(max_cols = 5, max_rows =5, show_dimensions = True)
    
    if df.shape == df_answer.shape : 
      global table_count
      table_count = 0     
      df_answer_html = df_answer.style.format(precision = 2). to_html(max_rows = 5, max_columns = 5).replace('<table', '<table class = "dataframe"')
      df_html_color = df.style.format(precision=2).applymap(table_compare, df_answer = df_answer).to_html(max_rows = 5, max_columns = 5).replace('<table', '<table class = "dataframe"')
      output_html_color = f'''
      <div style="display: flex; flex-direction: row;">
          <div style="float:left;width:50%">
          <h3>왼쪽은 여러분이 전처리한 Data입니다.</h3>
          <p >{df_html_color}</p>
          </div>
          <div style="float:right;width:50%">
          <h3>오른쪽은 예시 답안으로 전처리한 Data입니다.</h3>
          <p >{df_answer_html}</p>
          </div>
      </div>
      '''      

      display_HTML(output_html_color)
    else : 
      df_answer_html = df_answer.to_html(max_cols = 5, max_rows =5)
      output_html = f'''
      <div style="display: flex; flex-direction: row;">
          <div style="float:left;width:50%">
          <h3>왼쪽은 여러분이 전처리한 Data입니다.</h3>
          <p >{df_html}</p>
          </div>
          <div style="float:right;width:50%">
          <h3>오른쪽은 예시 답안으로 전처리한 Data입니다.</h3>
          <p >{df_answer_html}</p>
          </div>
      </div>
      '''      
      display_HTML(output_html)
    display_HTML('<HR>')
# 자동 평가
    #NAN이 있어도 평가하기 위해 추가한 코드
    if df_answer.isna().to_numpy().sum() : 
      random_number = random.randint(1, 20141112)
      df.fillna(value = random_number, inplace = True)
      df_answer.fillna(value = random_number, inplace = True)
    #NAN이 있어도 평가하기 위해 추가한 코드
    
    df_numpy = df.to_numpy()
    df_answer_numpy = df_answer.to_numpy()
    if np.array_equal(df_numpy, df_answer_numpy) and np.array_equal(df.columns, df_answer.columns) and np.array_equal(df.index, df_answer.index) :
      print(tc_green+'정답'+reset)
    else :
      print(tc_red+'오답'+reset)
      table_feedback(df, df_answer)
###
  # elif type(df) == pd.core.series.Series and type(df_answer) == pd.core.series.Series :

###
  elif type(df) == pd.core.series.Series and type(df_answer) == pd.core.series.Series :
    display_HTML('<h2 style = "background-color:yellow">Check the results</h2>')
  # 결과 자가 평가
    # df_answer_html = df_answer.to_html(max_cols = 5, max_rows =5, show_dimensions = True)
    # df_html = df.to_html(max_cols = 5, max_rows =5, show_dimensions = True)
    
    if df.shape == df_answer.shape : 
      # global table_count
      table_count = 0     
      df_answer_html = df_answer.to_frame().style.format(precision = 2).to_html(max_rows = 5, max_columns = 5).replace('<table', '<table class = "dataframe"')
      df_html_color = df.to_frame().style.format(precision=2).applymap(table_compare, df_answer = df_answer).to_html(max_rows = 5, max_columns = 5).replace('<table', '<table class = "dataframe"')
      output_html_color = f'''
      <div style="display: flex; flex-direction: row;">
          <div style="float:left;width:50%">
          <h3>왼쪽은 여러분이 전처리한 Data입니다.</h3>
          <p >{df_html_color}</p>
          </div>
          <div style="float:right;width:50%">
          <h3>오른쪽은 예시 답안으로 전처리한 Data입니다.</h3>
          <p >{df_answer_html}</p>
          </div>
      </div>
      '''      

      display_HTML(output_html_color)
    else : 
      df_html = df.to_frame().to_html(max_cols =5, max_rows = 5)
      df_answer_html = df_answer.to_html(max_cols = 5, max_rows =5)
      output_html = f'''
      <div style="display: flex; flex-direction: row;">
          <div style="float:left;width:50%">
          <h3>왼쪽은 여러분이 전처리한 Data입니다.</h3>
          <p >{df_html}</p>
          </div>
          <div style="float:right;width:50%">
          <h3>오른쪽은 예시 답안으로 전처리한 Data입니다.</h3>
          <p >{df_answer_html}</p>
          </div>
      </div>
      '''      
      display_HTML(output_html)
    display_HTML('<HR>')
# 자동 평가
    #NAN이 있어도 평가하기 위해 추가한 코드
    if df_answer.isna().to_numpy().sum() : 
      random_number = random.randint(1, 20141112)
      df.fillna(value = random_number, inplace = True)
      df_answer.fillna(value = random_number, inplace = True)
    #NAN이 있어도 평가하기 위해 추가한 코드
    
   
    df_numpy = df.to_numpy()
    df_answer_numpy = df_answer.to_numpy()
    if np.array_equal(df_numpy, df_answer_numpy) and np.array_equal(df.index, df_answer.index) :
      print(tc_green+'정답'+reset)
    else :
      print(tc_red+'오답'+reset)
      table_series_feedback(df, df_answer)

  elif df == df_answer and df !='' :
    output_html = f'''
    <div style="display: flex; flex-direction: row;">
        <div style="float:left;width:50%">
        <h3>왼쪽은 여러분이 전처리한 Data입니다.</h3>
        <p >{df}</p>
        </div>
        <div style="float:right;width:50%">
        <h3>오른쪽은 예시 답안으로 전처리한 Data입니다.</h3>
        <p >{df_answer}</p>
        </div>
    </div>
    '''
    display_HTML(output_html)
    display_HTML('<HR>')
    print(tc_green+'정답'+reset)

     
  elif df != df_answer and df != '' :
    output_html = f'''
    <div style="display: flex; flex-direction: row;">
        <div style="float:left;width:50%">
        <h3>왼쪽은 여러분이 전처리한 Data입니다.</h3>
        <p >{df}</p>
        </div>
        <div style="float:right;width:50%">
        <h3>오른쪽은 예시 답안으로 전처리한 Data입니다.</h3>
        <p >{df_answer}</p>
        </div>
    </div>
    '''
    display_HTML(output_html)
    display_HTML('<HR>')
    print(tc_red+'오답'+reset)

  elif df == df_answer and df == '' :
    return
  create_button_with_scratch_cell()

#------------------------------------------------------------------------------#
#에러에 따른 정보를 알려주는 함수

def table_feedback(df, df_answer) :
  if df.shape != df_answer.shape :
    display_HTML('Shape가 다릅니다.')
  elif (df.columns != df_answer.columns).sum() != 0 :
    display_HTML('Columns이 다릅니다.')
  elif (df.index != df_answer.index).sum() != 0 :
    display_HTML('Index가 다릅니다.')
  else :
    display_HTML('Dataframe 속 값이 다릅니다.')



def table_series_feedback(df, df_answer) :
  if df.shape != df_answer.shape :
    display_HTML('Shape가 다릅니다.')
  elif (df.index != df_answer.index).sum() != 0 :
    display_HTML('Index가 다릅니다.')
  else :
    display_HTML('Dataframe 속 값이 다릅니다.')
