from IPython.display import display, HTML, Javascript
import pandas as pd
import numpy as np
from google.colab import output
import globals_variable

def Question(question_number, _type = 'code'):

    globals_variable.question_num = question_number

    if question_number in globals_variable.result_df['id'] : 
        print(globals_variable.result_df[globals_variable.result_df['id'] == question_number]['total_attempts'])
        globals_variable.total_attempts = globals_variable.result_df.loc[globals_variable.result_df['id'] == question_number, 'total_attempts'].iloc[0]
        globals_variable.final_result = False
    else : 
        globals_variable.total_attempts = 0
    
    question_path = '/content/jupyter_judge/question_bank/question/' + question_number+'.html'
    globals_variable.question_name = 'question_'+question_number
    question_file = 'question_'+question_number

    file_name = '_'+ question_number+'.py'
    img_name = 'img_'+question_number

    
    globals()[img_name] = ''

    code_editor = setup_html_js()

    if globals_variable.question_name in globals() : 
        globals_variable.question_name_data = globals()[globals_variable.question_name]
        display(HTML(globals()[globals_variable.question_name] + code_editor))

    else : 
        with open(question_path, 'r') as f :
            data = f.read()
        globals()[globals_variable.question_name] = data
        globals_variable.question_name_data = globals()[globals_variable.question_name]

        answer_path = '/content/jupyter_judge/question_bank/answer/answer_' + question_number + '.py'
        with open(answer_path, 'r') as f : 
            _answer = f.read()
        exec(_answer)


        meta_path = '/content/jupyter_judge/question_bank/metadata/meta_data_' + question_number + '.py'
        with open(meta_path, 'r') as f : 
            meta = f.read()
        exec(meta)
  
        display(HTML(globals()[globals_variable.question_name] + code_editor))

    # 콜백 함수 등록
    def save_text(text):
        globals_variable.total_attempts += 1
        print(globals_variable.result_df)
        file_path = f'/content/{file_name}'
        with open(file_path, 'w') as file:
            file.write(text)
            
        if _type == 'code' :
          code_check(file_name)  # 결과 확인 함수
        elif _type =='turtle' :
          turtle_check(file_name)
        elif _type == 'plot' :
          plot_check(file_name)
        elif _type == 'pandas' :
          table_check(file_name)

    output.register_callback('notebook.save_text', save_text)

def setup_html_js():
    return """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/codemirror.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/mode/python/python.min.js"></script>
    <style>.CodeMirror {height: 200px; border: 1px solid #ccc; border-radius: 5px;}</style>
    <div style="clear: both"></div>
    <hr>
    <h2 style="background-color:orange;">코드 작성</h2>
    <div><textarea id="code-editor"></textarea></div>
    <button id="submitBtn">제출</button>
    <button onclick="deleteAllExceptSpecified()">초기화</button>
    <hr>
    <script>
        var editor = CodeMirror.fromTextArea(document.getElementById('code-editor'), {
            lineNumbers: true, mode: 'python', theme: 'default', viewportMargin: Infinity, inputStyle: 'textarea'
        });

        document.getElementById('submitBtn').addEventListener('click', function() {
            const text = editor.getValue();
            google.colab.kernel.invokeFunction('notebook.save_text', [text], {});
        });

        function deleteAllExceptSpecified() {
            var allDivs = document.querySelectorAll('div');
            var allClasses = [];
            allDivs.forEach(function(div) {
                if (div.className.includes('output-id')) {
                    allClasses.push(div.className);
                }
            });
            allClasses = allClasses.slice(1).map(className => className.replace(' ', '.'));
            allClasses.forEach(className => {
                document.querySelectorAll('.' + className).forEach(element => element.remove());
            });
        };
    </script>
    """


question_1101 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>5.24에서 자연수 부분을 출력해봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>없음</p>
<h2> 출력
</h2>
<p>자연수에 해당하는 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>5.24에서 자연수 부분</p>
</div>
'''
img_1101 = "https://github.com/GoHakNeung/python/blob/main/img_1101.JPG?raw=true"
answer_1101 = [
    {'input' : [], 'output' : [5]}
]

question_1102 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>1.1+1.7에서 소수 부분을 출력해봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>없음</p>
<h2> 출력
</h2>
<p>소수 부분 숫자</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>1.1+1.7에서 자연수가 아닌 부분 부분</p>
</div>'''
img_1102 = "https://github.com/GoHakNeung/python/blob/main/img_1102.JPG?raw=true"
answer_1102 = [
    {'input' : [], 'output' : [0.8]}
]

question_1103 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>0.01이 429개 있을 때, 자연수 부분과 소수 부분을 줄바꿈하여 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>없음</p>
<h2> 출력
</h2>
<p>첫째 줄에 자연수를, 둘째 줄에 소수를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>첫째 줄 : 자연수</p>
<p>둘째 줄 : 소수</p>
</div>'''
img_1103 = "https://github.com/GoHakNeung/python/blob/main/img_1102.JPG?raw=true"
answer_1103 = [
    {'input' : [], 'output' : [4,0.29]}
]

question_1201 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>아래 도형의 이름을 출력해봅시다.</p>
<svg width = "200" height = "100"><polygon points = "80,5 160,70 40,75", fill = "#FFFFFF", stroke = "#000000", stroke-width = "4"></svg>
<HR>
<h2>입력</h2>
<p>없음</p>
<h2>출력</h2>
<p>도형의 이름을 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>없음</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>도형이름</p>
</div>
'''
img_1201 = "https://github.com/GoHakNeung/python/blob/main/img_1102.JPG?raw=true"
answer_1201 = [
    {'input' : [], 'output' : ['삼각형']}
]

question_1202 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>아래 도형의 이름을 출력해봅시다.</p>
<svg width = "200" height = "100"><rect width = "200" height="100", fill = "#FFFFFF", stroke = "#000000", stroke-width = "4"></rect></svg>
<HR>
<h2>입력</h2>
<p>없음</p>
<h2>출력</h2>
<p>각도를 고려해서 도형의 이름을 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p></p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>도형 이름</p>
</div>
'''
img_1202 = "https://github.com/GoHakNeung/python/blob/main/img_1102.JPG?raw=true"
answer_1202 = [
    {'input' : [], 'output' : ['직사각형']}
]

question_1203 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>아래 도형에서 대각선 수를 출력해봅시다.</p>
<svg width = "200" height = "100"><polygon points = "100,5 160,40 130,80 70,80 40,40", fill = "#FFFFFF", stroke = "#000000", stroke-width = "4"></svg>
<HR>
<h2>입력</h2>
<p>없음</p>
<h2>출력</h2>
<p>도형이 가지고 있는 대각선 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>대각선 숫자</p>
</div>
'''
img_1203 = "https://github.com/GoHakNeung/python/blob/main/img_1102.JPG?raw=true"
answer_1203 = [
    {'input' : [], 'output' : [5]}
]

question_1204 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>아래 도형에서 대각선 수를 출력해봅시다.</p>
<svg width = "200" height = "100"><polygon points = "70,5 160,5 190,50 160,90 70,90 30,50", fill = "#FFFFFF", stroke = "#000000", stroke-width = "4"></svg>
<HR>
<h2>입력</h2>
<p>없음</p>
<h2>출력</h2>
<p>도형이 가지고 있는 대각선 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>없음</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>대각선 숫자</p>
</div>
'''
img_1204 = "https://github.com/GoHakNeung/python/blob/main/img_1102.JPG?raw=true"
answer_1204 = [
    {'input' : [], 'output' : [9]}
]

#입출력, 기준량, 비교하는양
question_2401 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>사과와 귤의 개수를 입력받습니다. </p>
<p>사과에 대한 귤의 비에서 기준량에 해당하는 숫자를 출력하는 프로그램을 만들어봅시다. </p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 사과 개수가, 둘째 줄에 귤 개수가 주어진다.</p>
<p>(사과와 귤의 개수는 1000이하의 숫자가 입력된다.)</p>
<h2> 출력
</h2>
기준량에 해당하는 숫자를 출력한다.
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 10</p>
<p> 15</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>10</p>
</div>
'''
img_2401 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_2401 = [
    {'input' : [[23], [17]], 'output' : [23]},
    {'input' : [[2], [5]], 'output' : [2]},
    {'input' : [[45], [7]], 'output' : [45]}
]
#입출력, 기준량, 비교하는양

question_2402 = '''<h1 style = "background-color:yellow; ">문제 설</h1>
<p>2개의 숫자를 입력받습니다. <span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>는 가득이네 반 학생 수이고 <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>는 축구를한 학생 수입니다. </p>
<p>전체 학생 수에 대한 축구를 한 학생 수의 비에서 비교하는 양을 출력하는 프로그램을 만들어봅시다.  </p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 가득이네 반 학생 수가 입력되고, 둘째 줄에는 축구를 한 학생 수가 입력됩니다.</p>
<h2>출력</h2>
<p>비교하는 양에 해당하는 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>27</p>
<p>19</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>19</p>
</div>
'''
img_2402 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_2402 = [
    {'input' : [[26], [13]], 'output' : [13]},
    {'input' : [[11], [5]], 'output' : [5]},
    {'input' : [[30], [17]], 'output' : [17]}
]

#입출력, 기준량, 비교하는양
question_2403 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다. <span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>는 사과 개수, <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>는 귤 개수입니다. </p>
<p>사과와 귤의 비에서 기준량을 출력하는 프로그램을 만들어봅시다. </p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 사과 개수가 입력되고, 둘째 줄에는 귤 개수가 입력됩니다.</p>
<h2>출력</h2>
<p>기준량에 해당하는 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>10</p>
<p>15</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>15</p>
</div>
'''
img_2403 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_2403 = [
    {'input' : [[23], [17]], 'output' : [17]},
    {'input' : [[2], [5]], 'output' : [5]},
    {'input' : [[45], [7]], 'output' : [7]}
]

#입출력, 기준량, 비교하는양
question_2404 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>2개의 숫자를 입력 받습니다. <span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>는 복숭아 개수, <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>는 포도 개수입니다. </p>
<p>복숭아와 포도의 비에서 비교하는 양을 출력하는 프로그램을 만들어봅시다. </p>
<HR>
<h2>입력</h2>
<p>첫째 줄에 복숭아 개수가 입력되고, 둘째 줄에 포도 개수가 입력됩니다.</p>
<p>(복숭아와 포도의 개수는 1000이하의 숫자가 입력된다.)</p>
<h2>출력</h2>
<p>비교하는 양에 해당하는 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>20</p>
<p>25</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>20</p>
</div>
'''
img_2404 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_2404 = [
    {'input' : [[23], [17]], 'output' : [23]},
    {'input' : [[2], [5]], 'output' : [2]},
    {'input' : [[45], [7]], 'output' : [45]}
]

question_3101 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>와 <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>를 더한 결과를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 첫번째 숫자가, 둘째 줄에 두번째 숫자가 주어집니다.</p>
<p>(1000이하의 숫자가 입력됩니다.)</p>
<h2> 출력
</h2>
<p>첫번째 숫자와 두번째 숫자를 더한 결과를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 10</p>
<p> 20</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>30</p>
</div>
'''
img_3101 = "https://github.com/GoHakNeung/python/blob/main/img_1101.JPG?raw=true"
answer_3101 = [
    {'input' : [[35], [23]], 'output' : [58]},
    {'input' : [[54], [1243]], 'output' : [1297]},
    {'input' : [[453], [987]], 'output' : [1440]}
]

question_3102 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫번째 숫자</span>와 <span style = "background-color:	#E0E0E0;">두번째 숫자</span>를 뺀 결과를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 첫번째 숫자가, 둘째 줄에 두번째 숫자가 주어집니다.</p>
<p>(1000이하의 숫자가 입력됩니다.)</p>
<h2> 출력
</h2>
<p>첫번째 숫자와 두번째 숫자를 뺀 결과를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 533</p>
<p> 134</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>399</p>
</div>
'''
img_3102 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_3102 = [
    {'input' : [[32], [18]], 'output' : [14]},
    {'input' : [[100], [19]], 'output' : [81]},
    {'input' : [[455], [92]], 'output' : [363]}
]

question_3103 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫번째 숫자</span>와 <span style = "background-color:	#E0E0E0;">두번째 숫자</span>를 곱한 결과를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 첫번째 숫자가, 둘째 줄에 두번째 숫자가 주어집니다.</p>
<p>(1000이하의 숫자가 입력됩니다.)</p>
<h2> 출력
</h2>
<p>첫번째 숫자와 두번째 숫자를 곱한 결과를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 342</p>
<p> 345</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>117990</p>
</div>
'''
img_3103 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_3103 = [
    {'input' : [[13], [21]], 'output' : [273]},
    {'input' : [[19], [212]], 'output' : [4028]},
    {'input' : [[234], [142]], 'output' : [33228]}
]

question_3104 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫번째 숫자</span>와 <span style = "background-color:	#E0E0E0;">두번째 숫자</span>를 나눈 결과를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 첫번째 숫자가, 둘째 줄에 두번째 숫자가 주어집니다.</p>
<p>(1000이하의 숫자가 입력됩니다.)</p>
<h2> 출력
</h2>
<p>첫번째 숫자와 두번째 숫자를 나눈 결과를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 4</p>
<p> 2</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>2.0</p>
</div>
'''
img_3104 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_3104 = [
    {'input' : [[12], [3]], 'output' : [4.0]},
    {'input' : [[578], [32]], 'output' : [578/32]},
    {'input' : [[764], [50]], 'output' : [764/50]}
]

## 3105 문제는 조건문으로 옮김.

question_3106 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>는 올 가을 수확한 사과 수이고, <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>는 한 상자에 담을 수 있는 사과 수입니다.</p>
<p>사과를 상자에 담아 판매하려고 할 때, 몇 상자를 팔 수 있을지 프로그램을 만들어봅시다.</p>
<p>(상자에는 사과가 가득 담겨있어야 판매할 수 있습니다.)</p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 올 가을에 수확한 사과 숫자이고, 둘째 줄에는 한 상자에 담을 수 있는 사과 숫자가 입력됩니다.</p>
<h2>출력</h2>
<p>판매할 수 있는 상자 숫자</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>67</p>
<p>8</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>8</p>
</div>
'''
img_3106 = "https://github.com/GoHakNeung/python/blob/main/img_1106.jpg?raw=true"
answer_3106 = [
    {'input' : [[543], [30]], 'output' : [18]},
    {'input' : [[24], [25]], 'output' : [0]},
    {'input' : [[768], [40]], 'output' : [19]},
    {'input' : [[128], [8]], 'output' : [16]}
]

#혼합계산산
question_3107 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>3개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>는 가득이 나이이고, <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>는 가득이 동생 나이입니다. </p>
<p>가득이 어머니 나이는 가득이 나이와 가득이 동생 나이를 합한 것의 2배보다 <span style = "background-color:	#E0E0E0;">세 번째 숫자</span>만큼 많습니다. </p>
<p>가득이 어머니 나이를 구하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 가득이 나이 숫자가 입력되고, 둘째 줄에는 가득이 동생 숫자가 입력되고, 셋째 줄에는 숫자가 입력됩니다.</p>
<h2>출력</h2>
<p>가득이 엄마 나이가 출력됩니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>12</p>
<p>10</p>
<p>3</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>47</p>
</div>
'''
img_3107 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3107 = [
    {'input' : [[12], [5], [9]], 'output' : [(12+5)*2+9]},
    {'input' : [[10], [9], [5]], 'output' : [(10+9)*2+5]},
    {'input' : [[13], [7], [3]], 'output' : [(13+7)*2+3]}
]

question_3108 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>3개의 숫자를 입력받습니다.</p>
<p>어떤 수에 <span style = "background-color:	#E0E0E0;">첫번째 숫자</span>를 뺀 다음 <span style = "background-color:	#E0E0E0;">두번째 숫자</span>를 나눈 뒤 <span style = "background-color:	#E0E0E0;">세번째 숫자</span>를 더했더니 542가 나왔습니다.</p>
<p>어떤 수를 구하는 프로그램을 만들어봅시다. </p>
<HR>
<h2>입력</h2>
<p>3개의 숫자가 줄바꿈하여 입력됩니다.</p>
<h2>출력</h2>
<p>자연수에 해당하는 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>2</p>
<p>3</p>
<p>10</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>1598</p>
</div>
'''
img_3108 = "https://github.com/GoHakNeung/python/blob/main/img_1109.jpg?raw=true"
answer_3108 = [
    {'input' : [[10], [20], [30]], 'output' : [10250]},
    {'input' : [[123], [4], [12]], 'output' : [2243]},
    {'input' : [[53], [7], [123]], 'output' : [2986]}
]

#단명수, 복명수수
question_3301 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫번째 숫자</span>의 단위는 km이고 <span style = "background-color:	#E0E0E0;">두번째 숫자</span>의 단위는 m입니다. </p>
<p>'<span style = "background-color:	#E0E0E0;">첫번째 숫자</span>km <span style = "background-color:	#E0E0E0;">두번째 숫자</span>m'인 길이를 m로 출력하는 프로그램을 만들어봅시다. </p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 km에 해당하는 숫자가 입력되고, 둘째 줄에는 m에 해당하는 숫자가 입력됩니다.</p>
<h2>출력</h2>
<p>m로 단위를 바꾼 숫자가 출력됩니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>51</p>
<p>102</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>51102</p>
</div>
'''
img_3301 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3301 = [
    {'input' : [[15], [25]], 'output' : [15*1000+25]},
    {'input' : [[351], [102]], 'output' : [351*1000+102]},
    {'input' : [[901], [1]], 'output' : [901*1000+1]}
]

#단명수, 복명수수
question_3302 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>1개의 숫자를 입력받습니다.</p>
<p>mL단위 <span style = "background-color:	#E0E0E0;">숫자</span>를 '_L_mL' 단위로 바꾸어 L와 mL를 줄바꿈하여 출력하는 프로그램을 만들어봅시다.
<HR>
<h2>입력</h2>
<p>mL 단위인 숫자가 입력됩니다.</p>
<h2>출력</h2>
<p>L와 mL로 단위롤 바꾸어 첫째 줄에는 L에 해당하는 숫자를, 둘째 줄에는 mL에 해당하는 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>1812</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>1</p>
<p>812</p>
</div>
'''
img_3302 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3302 = [
    {'input' : [[12053]], 'output' : [12, 53]},
    {'input' : [[205]], 'output' : [0, 205]},
    {'input' : [[12001]], 'output' : [12, 1]}
]
#단명수, 복명수수

question_3303 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받으며 <span style = "background-color:	#E0E0E0;">첫번째 숫자</span>의 단위는 km이고 <span style = "background-color:	#E0E0E0;">두번째 숫자</span>의 단위는 m입니다. </p>
<p>가득이는 50km 떨어져 있는 할아버지 댁에 갔습니다. '<span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>km <span style = "background-color:	#E0E0E0;">두번째 숫자</span>m'는 기차를 타고 나머지는 버스를 타고 갔습니다. </p>
<p>가득이가 버스타고 간 거리 m로 출력하는 프로그램을 만들어봅시다.</p> 
<HR>
<h2>입력</h2>
<p>첫째 줄에는 km에 해당하는 숫자가 입력되고, 둘째 줄에는 m에 해당하는 숫자가 입력됩니다</p>
<p></p>
<h2>출력</h2>
<p>버스를 타고 간 거리를 첫째 줄에는 km에 해당하는 숫자를 출력하고, 둘째 줄에는 m에 해당하는 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>32</p>
<p>150</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>17</p>
<p>850</p>
</div>
'''
img_3303 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3303 = [
    {'input' : [[15], [123]], 'output' : [34,877]},
    {'input' : [[21], [0]], 'output' : [29, 0]},
    {'input' : [[40], [999]], 'output' : [9, 1]}
]

#단명수, 복명수수
question_3304 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받으며 <span style = "background-color:	#E0E0E0;">첫번째 숫자</span>의 단위는 km이고 <span style = "background-color:	#E0E0E0;">두번째 숫자</span>의 단위는 m입니다. </p>
<p>km단위인 첫번째 숫자와 m단위인 두번째 숫자 크기 비교하여 첫 번째 숫자가 크면 True를 출력하고, 두 번째 숫자가 크면 False를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 km 단위인 숫자가 입력되고, 둘째 줄에는 m 단위인 숫자가 입력됩니다.</p>
<h2>출력</h2>
<p>두 숫자의 크기비교를 하여 True 또는 False를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>32</p>
<p>31092</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>True</p>
</div>
'''
img_3304 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3304 = [
    {'input' : [[15], [12003]], 'output' : ['True']},
    {'input' : [[21], [22343]], 'output' : ['False']},
    {'input' : [[40], [999111]], 'output' : ['False']}
]
#단명수, 복명수수

question_3305 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받으며 <span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>는 세종이가 숙제하는데 걸린 시간이며 단위는 시간이고 <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>는 가득이가 숙제하는데 걸린 시간이며 단위는 분입니다.</p>
<p>세종이가 숙제하는데 걸린 시간과 가득이가 숙제하는데 걸린 시간이 동일하면 True를 출력하고 다르면 False를 출력하는 프로그램을 만들어봅시다. </p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 세종이가 숙제하는데 걸린 시간(시간 단위)이 입력되고, 둘째 줄에는 가득이가 숙제하는데 걸린 시간(분 단위)이 입력됩니다. </p>
<h2>출력</h2>
<p>True 또는 False를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>3</p>
<p>150</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>False</p>
</div>
'''
img_3305 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3305 = [
    {'input' : [[2], [120]], 'output' : ['True']},
    {'input' : [[8], [490]], 'output' : ['False']},
    {'input' : [[6], [355]], 'output' : ['False']}
]

#단명수, 복명수수
question_3306 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>입력 받은 <span style = "background-color:	#E0E0E0;">2개의 숫자</span>는 마름모에서 두 대각선의 길이입니다.</p>
<p>마름모의 넓이가 50cm<sup>2</sup>보다 넓으면 True를 출력하고 작으면 False를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 대각선의 길이가 입력되고, 둘째 줄에는 다른 대각선의 길이가 입력됩니다.</p>
<h2>출력</h2>
<p>마름모와 사다리꼴의 넓이(50cm<sup>2</sup>)를 비교하여 True 또는 False를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>8</p>
<p>9</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>False</p>
</div>
'''
img_3306 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3306 = [
    {'input' : [[15], [6]], 'output' : ['False']},
    {'input' : [[9], [12]], 'output' : ['True']},
    {'input' : [[40], [4]], 'output' : ['True']}
]
#단명수, 복명수수

question_3307 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>는 원의 지름이며 <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>는 정사각형의 한 변의 길이입니다.</p>
<p>정사각형 둘레의 길이가 원주보다 길면 True를 출력하고 원주가 정사각형 둘레의 길이보다 길면 False를 출력하는 프로그램을 만들어봅시다.</p>
<p>(원주율은 3.14로 계산합니다.)</p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 원의 지름이 입력되고, 둘째 줄에는 정사각형의 한 변의 길이가 입력됩니다.</p>
<h2>출력</h2>
<p>정사각형 둘레의 길이와 원주를 비교하여 True 또는 False를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>12</p>
<p>10</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>True</p>
</div>
'''
img_3307 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3307 = [
    {'input' : [[124], [99]], 'output' : ['True']},
    {'input' : [[324], [220]], 'output' : ['False']},
    {'input' : [[54], [49]], 'output' : ['True']}
]

#부피, 이미지 넣기, 기준량, 비교하는양
question_3308 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>1개의 숫자를 입력받습니다.</p>
<p>가로 20cm, 세로 15cm인 수조에 물이 담겨 있습니다. 수조에 돌을 넣었더니 <span style = "background-color:	#E0E0E0;">입력 받은 숫자</span>만큼 높이가 늘어났습니다.</p>
<p>이 돌의 부피를 구하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>늘어난 높이(cm 단위)가 입력됩니다.</p>
<h2>출력</h2>
<p>cm<sup>3</sup>단위인 돌의 부피를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>5</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>1500</p>
</div>
'''
img_3308 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3308 = [
    {'input' : [[10]], 'output' : [3000]},
    {'input' : [[39]], 'output' : [11700]},
    {'input' : [[99]], 'output' : [29700]}
]

#사다리꼴 넓이
question_3309 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>cm단위의 3개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>는 윗변의 길이, <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>는 아랫변의 길이, <span style = "background-color:	#E0E0E0;">세 번째 숫자</spanu>는 높이입니다.</p>
<p>사다리꼴의 넓이를 구하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 윗변의 길이, 둘째 줄에는 아랫 변의 길이, 셋째 줄에는 높이가 입력됩니다.</p>
<h2>출력</h2>
<p>사다리꼴의 넓이가 출력됩니다.</p>
<p>(단위 생략)</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>5</p>
<p>10</p>
<p>20</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>1500</p>
</div>
<h2>
'''
img_3309 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3309 = [
    {'input' : [[43], [64], [9]], 'output' : [(43+64)*9/2]},
    {'input' : [[23], [1], [6]], 'output' : [(23+1)*6/2]},
    {'input' : [[8],[4],[12]], 'output' : [(8+4)*12/2]}
]

#부피, 이미지 넣기, 기준량, 비교하는양
question_3310 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p><span  style = "background-color:#E0E0E0; ">원의 지름</span>을 입력받아 원의 넓이를 구하는 프로그램을 만들어봅시다.</p>
<p>(원주율은 3.14로 계산합니다.)</p>
<HR>
<h2>입력</h2>
<p>자연수인 원의 지름을 입력받습니다.</p>
<p>cm단위이며 단위는 생략하고 입력됩니다.</p>
<h2>출력</h2>
<p>원의 넓이를 출력합니다.</p>
<p>단위는 생략합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>6</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>28.26</p>
</div>
'''
img_3310 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3310 = [
    {'input' : [[12]], 'output' : [6*6*3.14]},
    {'input' : [[7]], 'output' : [7/2*7/2*3.14]},
    {'input' : [[35]], 'output' : [35/2*35/2*3.14]}
]

#원주, 원의 넓이
question_3311 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p><span style = "background-color:	#E0E0E0;">원의 지름</span>을 입력받습니다. </p>
<p>반지름과 원주, 원의 넓이를 구하는 프로그램을 만들어봅시다. </p>
<p>원주율은 3.14로 계산합니다.</p>
<HR>
<h2>입력</h2>
<p>자연수인 원의 지름을 입력받습니다.</p>
<p>cm단위이며 단위는 생략하고 입력됩니다.</p>
<h2>출력</h2>
<p>첫째 줄에는 반지름, 둘째 줄에는 원주, 셋째 줄에는 원의 넓이를 출력합니다.</p>
<p>단위는 생략합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>8</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>4</p>
<p>25.12</p>
<p>50.24</p>
</div>
'''
img_3311 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3311 = [
    {'input' : [[10]], 'output' : [5, 10*3.14, 5*5*3.14]},
    {'input' : [[50]], 'output' : [25, 50*3.14, 25*25*3.14]},
    {'input' : [[128]], 'output' : [64, 128*3.14, 64*64*3.14]}
]

#원주, 원의 넓이
question_3312 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>원기둥의 전개도에서 <span style = "background-color:	#E0E0E0;">옆면의 둘레</span>를 입력받습니다. </p>
<p>원기둥의 높이와 밑면의 지름이 같을 때, 원기둥의 높이를 구하는 프로그램을 만들어봅시다. </p>
<p>원주율은 3으로 계산합니다.</p>
<HR>
<h2>입력</h2>
<p>자연수인 옆면의 둘레를 입력받습니다.</p>
<p>cm단위이며 단위는 생략하고 입력됩니다.</p>
<h2>출력</h2>
<p>원기둥의 높이를 출력합니다.</p>
<p>단위는 생략합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>40</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>5</p>
</div>
'''
img_3312 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3312 = [
    {'input' : [[400]], 'output' : [400/8]},
    {'input' : [[900]], 'output' : [900/8]},
    {'input' : [[324]], 'output' : [324/8]}
]

#올림림
question_3313 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>입력받은 <span style = 'background-color :#E0E0E0'>천의 자리 숫자</span>를 올림하여 천의 자리까지 나타내는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>천의 자리 숫자가 입력됩니다.</p>
<h2>출력</h2>
<p>올림하여 천의 자리까지 나타낸 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>2345</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>3000</p>
</div>
<h2>
'''
img_3313 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3313 = [
    {'input' : [[5436]], 'output' : [6000]},
    {'input' : [[6034]], 'output' : [7000]},
    {'input' : [[9999]], 'output' : [10000]}
]

#버림림
question_3314 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>입력받은 <span style = 'background-color :#E0E0E0'>만의 자리 숫자</span>를 버림하여 만의 자리까지 나타내는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>만의 자리 숫자가 입력됩니다.</p>
<h2>출력</h2>
<p>버림하여 만의 자리까지 나타낸 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>12345</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>10000</p>
</div>
'''
img_3314 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3314 = [
    {'input' : [[45838]], 'output' : [40000]},
    {'input' : [[82345]], 'output' : [80000]},
    {'input' : [[20000]], 'output' : [20000]}
]

#비례배분
question_3401 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다. </p>
<p>지민이와 유나가 <u style = "background-color:	#E0E0E0;">첫 번째 숫자</u>와 <u style = "background-color:	#E0E0E0;">두 번째 숫자</u> 비로 연필 144자루를 나눠갖기로 했습니다.</p>
<p>지민이가 갖게 될 연필을 구하는 프로그램을 만들어봅시다.</p> 
<HR>
<h2>입력</h2>
<p>첫째 줄과 둘째 줄에 자연수인 숫자가 입력됩니다.</p>
<h2>출력</h2>
<p>지민이가 갖게 될 연필의 수를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>1</p>
<p>2</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>48.0</p>
</div>
'''
img_3401 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3401 = [
    {'input' : [[1], [3]], 'output' : [144*1/4]},
    {'input' : [[7], [2]], 'output' : [144*7/9]},
    {'input' : [[5], [1]], 'output' : [144*5/6]}
]

#비례배분
question_3402 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>3개의 숫자를 입력받습니다. </p>
<p>지민이와 유나가 <span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>와 <span style = "background-color:	#E0E0E0;">두 번째 숫자</span> 비로 <span style = "background-color:	#E0E0E0;">세 번째 숫자</span>만큼의 연필을 나눠갖기로 했습니다.</p>
<p>유나가 갖게 될 연필을 구하는 프로그램을 만들어봅시다.</p> 
<HR>
<h2>입력</h2>
<p>첫째 줄, 둘째 줄, 셋째 줄에 자연수인 숫자가 입력됩니다.</p>
<h2>출력</h2>
<p>유나가 갖게 될 연필의 수를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>1</p>
<p>2</p>
<p>24</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>8.0</p>
</div>
'''
img_3402 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3402 = [
    {'input' : [[2], [3], [25]], 'output' : [25*3/5]},
    {'input' : [[8], [7], [60]], 'output' : [60*7/15]},
    {'input' : [[19], [3], [88]], 'output' : [88*3/19]}
]

#비례배분
question_3403 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다. </p>
<p>두 평행사변형 가(왼쪽), 나(오른쪽)의 넓이의 합은 832cm<sup>2</sup>입니다. </p>
<p><span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>는 가 평행사변형의 밑면의 길이이고 <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>는 나 평행사변형의 길이입니다.</p>
<p>평행사변형 가의 넓이를 구하는 프로그램을 만들어봅시다.</p> 
<svg width = "400" height = "100">
<polygon points = "5,5 395,5 300,5 340,95 250,95 210,5 155,5 125,95 45,95 75,5 45,95 5,95 395,95 340,95 300,5", fill = "#FFFFFF", stroke = "#000000", stroke-width = "4">
</svg>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 가(왼쪽) 평행사변형의 밑변의 길이가 입력되고, 둘째 줄에는 나(오른쪽) 평행사변형의 밑변의 길이가 입력됩니다.</p>
<h2>출력</h2>
<p>가(왼쪽) 평행사변형의 넓이를 출력합니다.</p>
<p>단위는 생략합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>3</p>
<p>5</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>312.0</p>
</div>
'''
img_3403 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_3403 = [
    {'input' : [3,1], 'output' : [832*3/4]},
    {'input' : [9, 7], 'output' : [832*9/16]},
    {'input' : [22, 10], 'output' : [832*22/32]}
]

#띄어세기
question_4101 ='''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>15000에서  <span style = "background-color:	#E0E0E0;">입력받은 숫자</span>만큼 띄어세는 수를 리스트로 만들어서 출력하는 프로그램을 만들어봅시다. </p>
<p>리스트에 10개의 숫자를 저장합니다. </p>
<HR>
<h2> 입력
</h2>
<p>인접한 두 숫자의 간격</p>
<p>(10000이하의 숫자가 입력됩니다.)</p>
<h2> 출력
</h2>
<p>입력한 숫자만큼 띄어세기 한 리스트(리스트 길이는 10)를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 100</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>[15000, 15100, 15200, 15300, 15400, 15500, 15600, 15700, 15800, 15900]</p>
</div>
'''
img_4101 = "https://github.com/GoHakNeung/python/blob/main/img_4101.jpg?raw=true"
answer_4101 = [
    {'input' : [[1]], 'output' : ['[15000, 15001, 15002, 15003, 15004, 15005, 15006, 15007, 15008, 15009]']},
    {'input' : [[315]], 'output' : ['[15000, 15315, 15630, 15945, 16260, 16575, 16890, 17205, 17520, 17835]']},
    {'input' : [[5090]], 'output' : ['[15000, 20090, 25180, 30270, 35360, 40450, 45540, 50630, 55720, 60810]']}
]

#띄어세기2
question_4102 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>에서 <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>만큼 띄어세는 수를 만들어서 리스트로 출력하는 프로그램을 만들어봅시다. </p>
<p>리스트의 길이는 10입니다.</p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 시작하는 숫자, 둘째 줄에는 두 숫자 사이의 간격에 해당하는 숫자가 입력됩니다.</p>
<h2>출력</h2>
<p>길이가 10인 리스트가 출력됩니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>100</p>
<p>10</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>[100, 110, 120, 130, 140, 150, 160, 170, 180, 190]</p>
</div>
'''
img_4102 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_4102 = [
    {'input' : [[15], [25]], 'output' : ['[15, 40, 65, 90, 115, 140, 165, 190, 215, 240]']},
    {'input' : [[300], [200]], 'output' : ['[300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100]']},
    {'input' : [[9000], [2000]], 'output' : ['[9000, 11000, 13000, 15000, 17000, 19000, 21000, 23000, 25000, 27000]']}
]

#배수
question_4103 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p><span style = "background-color:	#E0E0E0;">입력 받은 숫자의</span>의 배수를 10개를 리스트로 만들어서 출력하는 프로그램을 만들어봅시다. </p>
<p>첫 번째 숫자는 포함하지 않으며 작은 수부터 차례대로 커지도록 만듭니다.</p>
<HR>
<h2>입력</h2>
<p>자연수가 입력됩니다..</p>
<h2>출력</h2>
<p>길이가 10인 리스트가 출력됩니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>5</p>
<p>7</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>[10,15,20,25,30,35,40,45,50,55]</p>
</div>
'''
img_4103 = "https://github.com/GoHakNeung/python/blob/main/img_1109.jpg?raw=true"
answer_4103 = [
    {'input' : [[48], [5]], 'output' : ['[96, 144, 192, 240, 288, 336, 384, 432, 480, 528]']},
    {'input' : [[20], [6]], 'output' : ['[40, 60, 80, 100, 120, 140, 160, 180, 200, 220]']},
    {'input' : [[13], [3]], 'output' : ['[26, 39, 52, 65, 78, 91, 104, 117, 130, 143]']}
]

#이상이하
question_4104 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다. </p>
<p><span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>초과 <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>이하인 수를 리스트로 만들어서 출력하는 프로그램을 만들어봅시다. </p>
<HR>
<h2>입력</h2>
<p>첫째 줄과 둘째 줄에 자연수가 입력됩니다.</p>
<h2>출력</h2>
<p>범위에 해당하는 자연수를 리스트로 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>5</p>
<p>12</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>[6, 7, 8, 9, 10, 11, 12]</p>
</div>
'''
img_4104 = "https://github.com/GoHakNeung/python/blob/main/img_1109.jpg?raw=true"
answer_4104 = [
    {'input' : [[4], [10]], 'output' : ['[5,6,7,8,9,10]']},
    {'input' : [[12], [13]], 'output' : ['[13]']},
    {'input' : [[81], [86]], 'output' : ['[82,83,84,85,86]']}
]

#규칙성, 리스트 추가하기
question_4105 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<table border="1"
       cellspacing="0"
       width = 10
       height = 10>

    <tr>
    	<td>2</td>
      <td>4</td>
      <td>6</td>
      <td>...</td>
    </tr>
    <tr>
    	<td>4</td>
      <td>6</td>
      <td>8</td>
      <td>...</td>      
    </tr>
    <tr>
    	<td>6</td>
      <td>8</td>
      <td>10</td>
      <td>...</td>      
    </tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>                  
</table>
<p>그림과 같이 대각선(2,6,10...)으로 규칙을 갖는 숫자모음에서 <span style = "background-color:	#E0E0E0;">입력받은 숫자</span>의 길이만큼 리스트를를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>자연수가 입력됩니다.</p>
<h2>출력</h2>
<p>리스트가 출력됩니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>5</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>[2,6,10,14,18]</p>
</div>
'''
img_4105 = "https://github.com/GoHakNeung/python/blob/main/img_1109.jpg?raw=true"
answer_4105 = [
    {'input' : [[10]], 'output' : ['[2, 6, 10, 14, 18, 22, 26, 30, 34, 38]']},
    {'input' : [[15]], 'output' : ['[2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58]']},
    {'input' : [[20]], 'output' : ['[2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78]']}
]

#리스트 요소 및 길이
question_4106 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>5씩 커지는 <span style = "background-color:	#E0E0E0;">숫자 모음(리스트)</span>를 입력받습니다.</p>
<p>5번째에 들어있는 값과 숫자 모음에 포함되어 있는 숫자 개수를 출력하는 프로그램을 구해봅시다.</p> 
<HR>
<h2>입력</h2>
<p>5씩 커지는 리스트가 입력됩니다.</p>
<h2>출력</h2>
<p>첫째 줄에 리스트에 있는 5번째 값을 출력하고 둘째 줄에 리스트 길이를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>[1,6,11,16,21,26,31,36,41,46,51]</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>21</p>
<p>11</p>
</div>
'''
img_4106 = "https://github.com/GoHakNeung/python/blob/main/img_1109.jpg?raw=true"
answer_4106 = [
    {'input' : [[14,19,24,29,34,39,44,49,54]], 'output' : [34, 9]},
    {'input' : [[102,107,112,117,122,127,132,137]], 'output' : [122, 8]},
    {'input' : [[0,5,10,15,20]], 'output' : [20,5]}
]

#리스트 요소 및 길이
question_4107 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>101씩 띄어세기 하는 <span style = "background-color:	#E0E0E0;">숫자 모음(리스트)</span>을 입력받습니다.</p>
<p>숫자 모음에 다음에 올 수를 추가하여 리스트를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>리스트를 입력받습니다.</p>
<h2>출력</h2>
<p>리스트를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>[1,102,203,304,405]</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>[1,102,203,304,405,506]</p>
</div>
'''
img_4107 = "https://github.com/GoHakNeung/python/blob/main/img_1109.jpg?raw=true"
answer_4107 = [
    {'input' : [[34, 135, 236, 337, 438, 539]], 'output' : ['[34, 135, 236, 337, 438, 539, 640]']},
    {'input' : [[18, 119, 220, 321]], 'output' : ['[18, 119, 220, 321, 422]']},
    {'input' : [[1802, 1903, 2004, 2105, 2206, 2307, 2408, 2509, 2610, 2711, 2812, 2913]], 'output' : ['[1802, 1903, 2004, 2105, 2206, 2307, 2408, 2509, 2610, 2711, 2812, 2913, 3014]']}
]

question_5101 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>입력받은 <span style = "background-color:	#E0E0E0;">숫자</span>를 자리 수로 분리해서 리스트로 만드는 프로그램을 만들어봅시다.</p>
<p>일의 자리에 해당하는 숫자가 맨 마지막에 위치하도록 합니다.</p>
<HR>
<h2>입력</h2>
<p>자연수를 입력받습니다.</p>
<h2>출력</h2>
<p>자리 수에 해당하는 숫자를 리스트에 저장해서 리스트를 출력합니다.</p>
<p>일의 자리에 해당하는 숫자가 맨 마지막에 위치하도록 합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>1234</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>[1,2,3,4]</p>
</div>
'''
img_5101 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_5101 = [
    {'input' : [125], 'output' : ['[1, 2, 5]']},
    {'input' : [65423], 'output' : ['[6, 5, 4, 2, 3]']},
    {'input' : [10001], 'output' : ['[1, 0, 0, 0, 1]']}
]

#
question_5102 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>1부터 10까지 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>없음</p>
<h2>출력</h2>
<p>1부터 10까지 줄바꿈하여 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>없음</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
</div>
'''
img_5102 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_5102 = [
    {'input' : [], 'output' : [1,2,3,4,5,6,7,8,9,10]}
]

#
question_5103 ='''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>1부터 21까지 2씩 띄어서 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>없음</p>
<h2> 출력
</h2>
<p>1, 3, 5, ... , 21을 줄바꿈하여 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>1</p>
<p>3</p>
<p>5</p>
<p>7</p>
<p>9</p>
<p>11</p>
<p>13</p>
<p>15</p>
<p>17</p>
<p>19</p>
<p>21</p>
</div>
'''
img_5103 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_5103 = [
    {'input' : [], 'output' : [1,3,5,7,9,11,13,15,17,19,21]}
]
#

question_5104 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>입력받은 <span style = "background-color:	#E0E0E0;">숫자</span>의 구구단을 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>2 ~ 19사이 숫자가 입력됩니다.</p>
<h2> 출력
</h2>
<p>입력한 숫자에 해당하는 구구단이 출력됩니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>5</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>5</p>
<p>10</p>
<p>15</p>
<p>20</p>
<p>25</p>
<p>30</p>
<p>35</p>
<p>40</p>
<p>45</p>
</div>
'''
img_5104 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_5104 = [
    {'input' : [[9]], 'output' : [9, 18, 27, 36, 45, 54, 63, 72, 81]},
    {'input' : [[11]], 'output' : [11, 22, 33, 44, 55, 66, 77, 88, 99]}
]
#

question_5105 ='''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>10씩 띄어세기 하는 <span style = "background-color:	#E0E0E0;">숫자 모음(리스트)</span>을 입력받아 숫자 모음에 저장된 숫자를 순서대로 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>숫자모음(리스트)가 입력됩니다.</p>
<h2> 출력
</h2>
<p>숫자모음(리스트)에 저장된 숫자가 순서대로 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 10, 20, 30, 40, 50</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>10</p>
<p>20</p>
<p>30</p>
<p>40</p>
<p>50</p>
</div>
'''
img_5105 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_5105 = [
    {'input' : [[20, 30, 40, 50, 60]], 'output' : [20, 30, 40, 50, 60]},
    {'input' : [[12,22,32,42,52]], 'output' : [12,22,32,42,52]},
    {'input' : [[45, 55, 65, 75, 85]], 'output' : [45, 55, 65, 75, 85]}
]



question_5201 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>길이가 <span style = "background-color:	#E0E0E0;">100</span>인 정사각형을 그려봅시다.</p>
<svg width = "200" height = "100"><polygon points = "5,5 95,5 95,95 5 95", fill = "#FFFFFF", stroke = "#000000", stroke-width = "4"></svg>
<HR>
<h2> 입력 </h2>
<p>없음</p>
<h2> 출력 </h2>
<p>forward(), left()를 이용해서 정사각형을 그립니다..</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>길이가 100인 정사각형</p>
</div>
'''
img_5201 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_5201 = [
    {'input' : [], 'output' : ['t = Turtle(window)','t.width(3)', "t.color('red')", 'for i in range(4) : ', ' t.forward(100)', ' t.left(90)']}
]

question_5202 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>길이가 <span style = "background-color:	#E0E0E0;">150</span>인 정삼각형을 그려봅시다.</p>
<svg width = "200" height = "200"><polygon points = "100,5 5,167 195,167", fill = "#FFFFFF", stroke = "#000000", stroke-width = "4"></svg>
<HR>
<h2> 입력 </h2>
<p>없음</p>
<h2> 출력 </h2>
<p>forward(), left()를 이용해서 정삼각형을 그립니다..</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>길이가 150인 정삼각형</p>
</div>
'''
img_5202 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_5202 = [
    {'input' : [], 'output' : ['t = Turtle(window)','t.width(3)', "t.color('red')", 'for i in range(3) : ', ' t.forward(150)', ' t.left(120)']}
]

question_5203 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>길이가 <span style = "background-color:	#E0E0E0;">75</span>인 정육각형을 그려봅시다.</p>
<svg width = "210" height = "210"><polygon points = "55,5 155,5 205,90 155,175 55,175 5,90", fill = "#FFFFFF", stroke = "#000000", stroke-width = "4"></svg>
<HR>
<h2> 입력 </h2>
<p>없음</p>
<h2> 출력 </h2>
<p>forward(), left()를 이용해서 정육각형을 그립니다..</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>길이가 75인 정육각형</p>
</div>
'''
img_5203 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_5203 = [
    {'input' : [], 'output' : ['t = Turtle(window)','t.width(3)', "t.color('red')", 'for i in range(6) : ', ' t.forward(75)', ' t.left(60)']}
]

question_5204 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>길이가 <span style = "background-color:	#E0E0E0;">100</span>인 별을 그려봅시다.</p>
<svg width = "210" height = "210"><polygon points = "5,75 195,75 40,185 100,5 160,185 ", fill = "#FFFFFF", stroke = "#000000", stroke-width = "4"></svg>
<HR>
<h2> 입력 </h2>
<p>없음</p>
<h2> 출력 </h2>
<p>forward(), right()를 이용해서 별을 그립니다..</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>길이가 100인 별</p>
</div>
'''
img_5204 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_5204 = [
    {'input' : [], 'output' : ['t = Turtle(window)','t.width(3)', "t.color('red')", 'for i in range(5) : ', ' t.forward(100)', ' t.right(144)']}
]

question_5205 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>길이가 <span style = "background-color:	#E0E0E0;">120</span>이고 한 각이 <span style = "background-color:	#E0E0E0;">45</span>&#176인 마름모를 그려봅시다.</p>
<svg width = "200" height = "100"><polygon points = "5,75 105,75 175,5 75,5", fill = "#FFFFFF", stroke = "#000000", stroke-width = "4"></svg>
<HR>
<h2> 입력 </h2>
<p>없음</p>
<h2> 출력 </h2>
<p>forward(), left(), right() 등을 이용해서 마름모를 그립니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>길이가 120이고 한 각이 45&#176인 마름모</p>
</div>
'''
img_5205 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_5205 = [
    {'input' : [], 'output' : ['t = Turtle(window)','t.width(3)', "t.color('red')", 'for i in range(2) : ', ' t.forward(120)', ' t.left(45)', ' t.forward(120)', ' t.left(135)' ]}
]

question_5206 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>길이가 <span style = "background-color:	#E0E0E0;">100</span>인 다음과 같은 정삼각형을 상하로 뒤집었을 때, 나오는 도형을 그려봅시다.  </p>
<svg width = "150" height = "200"><polygon points = "5,50 55,135 105,50", fill = "#FFFFFF", stroke = "#000000", stroke-width = "4"></svg>
<HR>
<h2> 입력 </h2>
<p>없음</p>
<h2> 출력 </h2>
<p>forward(), left(), right() 등을 이용해서 도형을 그립니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>제시된 삼각형과 상하 뒤집어진 삼각형</p>
</div>
'''
img_5206 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_5206 = [
    {'input' : [], 'output' : ['t = Turtle(window)','t.width(3)', "t.color('red')", 'for i in range(3) : ', ' t.forward(100)', ' t.left(120)']}
]


#이등변 삼각형 가능/불가능
question_6101 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>입력받은 <span style = "background-color:	#E0E0E0;">숫자</span>가 홀수인지 짝수인지 알려주는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>1000이하 숫자가 입력됩니다.</p>
<h2> 출력
</h2>
<p>홀수 또는 짝수가 출력됩니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>23</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>홀수</p>
</div>
'''
img_6101 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_6101 = [
    {'input' : [[10]], 'output' : ['짝수']},
    {'input' : [[54435]], 'output' : ['홀수']},
    {'input' : [[6445]], 'output' : ['홀수']}
]
#크기비교
question_6102 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>입력받은 <span style = "background-color:	#E0E0E0;">2개의 숫자</span> 중 크기가 큰 숫자를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 첫 번째 숫자가 입력되고, 둘째 줄에 두 번째 숫자가 입력됩니다.</p>
<h2> 출력
</h2>
<p>두 숫자 중 큰 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>12</p>
<p>43</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>43</p>
</div>
'''
img_6102 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_6102 = [
    {'input' : [[20], [10]], 'output' : [20]},
    {'input' : [[423], [1233]], 'output' : [1233]},
    {'input' : [[7213], [22321]], 'output' : [22321]},
    {'input' : [[12344], [12344]], 'output' : [12344]}    
]
#크기비교
question_6103 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>3개의 숫자를 입력받습니다. </p>
<p>입력받은 <span style = "background-color:	#E0E0E0;">3개의 숫자</span> 중 가장 큰 숫자를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>첫째 줄, 둘째 줄, 셋째 줄에 자연수를 입력받습니다.</p>
<h2>출력</h2>
<p>가장 큰 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>3</p>
<p>5</p>
<p>2</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>5</p>
</div>
'''
img_6103 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_6103 = [
    {'input' : [[12], [65], [34]], 'output' : [65]},
    {'input' : [[2134], [1243], [32]], 'output' : [2134]},
    {'input' : [[452], [34], [6565]], 'output' : [6565]}
]
#크기비교
question_6104 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>3개의 숫자를 입력받습니다. </p>
<p>입력받은 <span style = "background-color:	#E0E0E0;">3개의 숫자</span> 중 가장 작은 숫자를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>첫째 줄, 둘째 줄, 셋째 줄에 자연수를 입력받습니다.</p>
<h2>출력</h2>
<p>가장 작은 숫자를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>4</p>
<p>6</p>
<p>9</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>4</p>
</div>
'''
img_6104 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_6104 = [
    {'input' : [[12], [65], [34]], 'output' : [12]},
    {'input' : [[2134], [1243], [32]], 'output' : [32]},
    {'input' : [[452], [34], [6565]], 'output' : [34]}
]

question_6105 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>는 소풍에 놀러 온 학생 숫자이고, <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>는 관람차에 탈 수 있는 정원입니다. 소풍 온 학생들이 모두 관람차를 타려면 관람차는 몇 대가 필요할까요?</p>
<HR>
<h2>입력</h2>
<p>첫째 줄에는 소풍에 놀러 온 학생 숫자이고, 둘째 줄에는 관람차 정원 숫자가 입력됩니다.</p>
<h2>출력</h2>
<p>소풍에 놀러 온 학생들이 모두 관람차를 타기 위해서 필요한 관람차 개수</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>36</p>
<p>8</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>5</p>
</div>
'''
img_6105 = "https://github.com/GoHakNeung/python/blob/main/img_1107.jpg?raw=true"
answer_6105 = [
    {'input' : [[124], [12]], 'output' : [11]},
    {'input' : [[453], [34]], 'output' : [14]},
    {'input' : [[53], [7]], 'output' : [8]},
    {'input' : [[64], [8]], 'output' : [8]}
]



#예각,직각,둔각 알기
question_6201 ='''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>입력 받은 1개의 <span style = "background-color : #E0E0E0">숫자(각도)</span>가 예각인지, 직각인지, 둔각인지 출력하도록 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>1 ~ 179 사이 숫자가 입력됩니다.</p>
<h2> 출력
</h2>
<p>예각, 직각, 둔각 중 하나를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>56</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>예각</p>
</div>
'''
img_6201 = "https://github.com/GoHakNeung/python/blob/main/img_4201.jpg?raw=true"
answer_6201 = [
    {'input' : [[1]], 'output' : ['예각']},
    {'input' : [[89]], 'output' : ['예각']},
    {'input' : [[90]], 'output' : ['직각']},
    {'input' : [[91]], 'output' : ['둔각']},
    {'input' : [[179]], 'output' : ['둔각']}
]

#예각삼각형, 직각삼각형, 둔각삼각형
question_6202 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>입력 받은 <span style = "background-color : #E0E0E0">3개의 숫자(각도)</span>는 삼각형에서 세 각의 크기입니다. </p>
<p>삼각형은 예각삼각형인지 직각삼각형인지 둔각삼각형인지 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>삼각형 세 각의 크기가 줄바꿈하여 입력됩니다.</p>
<p>(단위는 생략되고 입력됩니다.)</p>
<h2>출력</h2>
<p>예각삼각형, 직각삼각형, 둔각삼각형 중 하나를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>43</p>
<p>17</p>
<p>120</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>둔각삼각형</p>
</div>'''
img_6202 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_6202 = [
    {'input' : [[65], [19], [96]], 'output' : ['둔각삼각형']},
    {'input' : [[90], [20], [70]], 'output' : ['직각삼각형']},
    {'input' : [[60], [70], [50]], 'output' : ['예각삼각형']}
]
#이등변 삼각형 가능/불가능

question_6203 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>입력 받은 <span style = "background-color:	#E0E0E0;">2개의 숫자(각도)</span>는 삼각형에서 두 각의 크기입니다. </p>
<p>이등변삼각형이 될 수 있으면 '가능'을 출력하고 이등변 삼각형이 될 수 없으면 '불가능'을 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>삼각형에서 두 각이  입력됩니다.</p>
<h2> 출력
</h2>
<p>가능 또는 불가능</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>50</p>
<p>80</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>가능</p>
</div>
'''

img_6203 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_6203 = [
    {'input' : [[80], [20]], 'output' : ['가능']},
    {'input' : [[90], [20]], 'output' : ['불가능']},
    {'input' : [[60], [70]], 'output' : ['불가능']}
]
#이등변 삼각형 가능/불가능

question_6301 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>입력받은 <span style = "background-color:	#E0E0E0;">3개의 숫자(각도)</span>로 삼각형을 만들 수 있으면 '가능'을 출력하고 만들 수 없으면 '불가능'을 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에는 첫 번째 숫자가 입력되고, 둘째 줄에는 두 번째 숫자가 입력되고 셋째 줄에는 세번째 숫자가 출력됩니다.</p>
<p>1 ~ 179 사이 숫자가 입력됩니다.</p>
<h2> 출력
</h2>
<p>가능 또는 불가능을 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>34</p>
<p>67</p>
<p>79</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>가능</p>
</div>
'''
img_6301 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_6301 = [
    {'input' : [[60], [32], [88]], 'output' : ['가능']},
    {'input' : [[35], [79], [153]], 'output' : ['불가능']},
    {'input' : [[1], [1], [178]], 'output' : ['가능']}
]

#이등변 삼각형 가능/불가능
question_6302 ='''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>숫자와 글자를 순서대로 입력받습니다.</p>
<p>입력받은 <span style = "background-color:	#E0E0E0;">십만 자리 숫자</span>를 입력받은 <span style = "background-color:	#E0E0E0;">글자</span>에 맞게 올림 또는 내림하여 만 자리까지 나타내는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 십만 자리 숫자가 입력되고, 둘째 줄에 올림 또는 내림이 입력됩니다.</p>
<h2> 출력
</h2>
<p>올림 또는 내림하여 만의 자리 까지 나타낸 수를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>123421</p>
<p>올림</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>130000</p>
</div>
'''
img_6302 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_6302 = [
    {'input' : [[781233], ['내림']], 'output' : [781233//10000*10000]},
    {'input' : [[312543], ['올림']], 'output' : [(312543//10000+1)*10000]},
    {'input' : [[465563], ['내림']], 'output' : [465563//10000*10000]}
]

#단위 바꾸기
question_6303 ='''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>숫자와 글자를 순서대로 입력받습니다.</p>
<p>m(미터)단위인 입력받은 <span style = "background-color:	#E0E0E0;">숫자</span>를 입력받은 <span style = "background-color:	#E0E0E0;">글자(단위)</span>에 맞게 바꾸는 프로그램을 만들어봅시다.</p>
<p>글자는 cm 또는 mm를 입력받습니다.</p>
<HR>
<h2>입력</h2>
<p>첫째 줄에 m 단위의 길이, 둘째 줄에 단위를 입력받습니다.</p>
<h2>출력</h2>
<p>입력 받은 숫자를 단위에 맞게 바꿔 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>25</p>
<p>cm</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>2500</p>
</div>
'''
img_6303 = "https://github.com/GoHakNeung/python/blob/main/img_4203.jpg?raw=true"
answer_6303 = [
    {'input' : [[50], ['cm']], 'output' : [5000]},
    {'input' : [[534], ['mm']], 'output' : [534000]},
    {'input' : [[1244], ['mm']], 'output' : [1244000]}
]

#약수
question_7101 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>2개의 숫자를 입력받습니다.</p>
<p>입력받은 <span style = "background-color:	#E0E0E0;">숫자</span>를 나누어 떨어지게 하는 숫자를 모두 출력하는 프로그램을 만들어봅시다.</p>
<p>작은 숫자부터 출력하도록 합니다.</p>
<HR>
<h2> 입력
</h2>
<p>1000000보다 작은 숫자가 입력됩니다.</p>
<h2> 출력
</h2>
<p>약수가 리스트로 출력됩니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>12</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>[1,2,3,4,6,12]</p>
</div>
'''
img_7101 = "https://github.com/GoHakNeung/python/blob/main/img_1109.jpg?raw=true"
answer_7101 = [
    {'input' : [[100]], 'output' : ['[1, 2, 4, 5, 10, 20, 25, 50, 100]']},
    {'input' : [[192382]], 'output' : ['[1, 2, 43, 86, 2237, 4474, 96191, 192382]']},
    {'input' : [[17]], 'output' : ['[1, 17]']}
]

#약수
question_7102 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>입력받은 <span style = "background-color:	#E0E0E0;">2개의 숫자</span>를 모두 나누어 떨어지게 하는 숫자를 리스트로 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 첫번째 숫자가, 둘째 줄에 두번째 숫자가 입력됩니다.</p>
<p>(2개의 숫자는 1000000보다 작은 숫자가 입력됩니다.)</p>
<h2> 출력
</h2>
<p>두 숫자를 모두 나누어 떨어지게 하는 숫자를 리스트로 출력합니다. 
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 20</p>
<p> 12</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>[1,2,4]</p>
</div>
'''
img_7102 = "https://github.com/GoHakNeung/python/blob/main/img_1109.jpg?raw=true"
answer_7102 = [
    {'input' : [[16], [40]], 'output' : ['[1, 2, 4, 8]']},
    {'input' : [[234], [654]], 'output' : ['[1, 2, 3, 6]']},
    {'input' : [[17], [532]], 'output' : ['[1]']}
]
#최대공약수
question_7103 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫 번째 숫자</span>는 색종이 수이고 <span style = "background-color:	#E0E0E0;">두 번째 숫자</span>는 색도화지 수입니다. </p> 
<p>최대한 많은 사람에게 남김없이 똑같이 나누어주려고 할 때, 최대 몇 명까지 나누어 줄 수 있는지 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>첫째 줄에 색종이 수가 입력되고 둘째 줄에 색도화지 수가 입력됩니다.</p>
<h2>출력</h2>
<p>나누어 줄 수 있는 사람 수가 출력됩니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>40</p>
<p>64</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>8</p>
</div>
'''
img_7103 = "https://github.com/GoHakNeung/python/blob/main/img_1109.jpg?raw=true"
answer_7103 = [
    {'input' : [[48], [52]], 'output' : [4]},
    {'input' : [[20], [35]], 'output' : [5]},
    {'input' : [[13], [84]], 'output' : [1]}
]

#배수
question_7104 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다.</p>
<p>입력받은 <span style = "background-color:	#E0E0E0;">2개 숫자</span>의 공배수를 리스트로 출력하는 프로그램을 만들어봅시다.</p>
<p>작은 숫자부터 10개를 출력하도록 합니다.</p>
<HR>
<h2>입력</h2>
<p>두 자연수를 줄바꿈하여 입력받습니다.</p>
<h2>출력</h2>
<p>10개의 공배수가 포함된 리스트를 출력합니다. </p>
<p>공배수는 작은 숫자부터 10개를 출력하도록 합니다. </p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>20</p>
<p>12</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>[60, 120, 180, 240, 300, 360, 420, 480, 540, 600]</p>
</div>'''
img_7104 = "https://github.com/GoHakNeung/python/blob/main/img_1109.jpg?raw=true"
answer_7104 = [
    {'input' : [[20], [35]], 'output' : ['[140, 280, 420, 560, 700, 840, 980]']},
    {'input' : [[12], [45]], 'output' : ['[180, 360, 540, 720, 900]']},
    {'input' : [[12], [30]], 'output' : ['[60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960]']}
]

#약수
question_7105 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2개의 숫자를 입력받습니다.</p>
<p>입력받은 <span style = "background-color:	#E0E0E0;">2개 숫자</span>의 최소공배수를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>두 자연수가 줄바꿈하여 입력됩니다.</p>
<h2>출력</h2>
<p>최소공배수를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>20</p>
<p>12</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>60</p>
</div>
<h2>
'''
img_7105 = "https://github.com/GoHakNeung/python/blob/main/img_1109.jpg?raw=true"
answer_7105 = [
    {'input' : [[20], [35]], 'output' : [140]},
    {'input' : [[48], [52]], 'output' : [624]},
    {'input' : [[231], [562]], 'output' : [129822]}
]

question_7501 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p><span style = "background-color : #E0E0E0">숫자 모음</span>을 리스트로 입력받습니다.</p>
<p>숫자 모음의 평균을 출력하는 프로그램을 만들어봅시다. </p>
<HR>
<h2>입력</h2>
<p>리스트를 입력받습니다.</p>
<h2>출력</h2>
<p>리스트에 저장된 숫자의 평균을 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>[4,6,9,12,5,2,6,4]</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>6.0</p>
</div>
'''
img_7501 = "https://github.com/GoHakNeung/python/blob/main/img_3502.jpg?raw=true"
answer_7501 = [
    {'input' : [[1, 2, 5, 4]], 'output' : [3.0]},
    {'input' : [[23, 5, 3, 6, 76, 12, 4, 342]], 'output' : [58.875]},
    {'input' : [[65, 12, 34, 6, 63, 2, 314, 1, 9, 5432]], 'output' : [593.8]}
]

question_7502 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>숫자 개수가 정해지지 않은 <span style = "background-color : #E0E0E0">숫자 모음</span>을 리스트로 입력받습니다.</p>
<p>숫자 모음에서 숫자 하나를 선택했을 때 짝수일 가능성을 구하는 프로그램을 만들어봅시다.</p>
<HR>
<h2>입력</h2>
<p>리스트를 입력받습니다.</p>
<h2>출력</h2>
<p>리스트에 저장된 숫자에서 하나의 숫자를 선택했을 때 짝수일 가능성을 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>입력 예시 </h2>
<p>[4, 61, 9, 12, 1, 43, 2, 8]</p>
</div>
<div style = "float:right;width:50%">
<h2>출력 예시 </h2>
<p>0.5</p>
</div>
'''
img_7502 = "https://github.com/GoHakNeung/python/blob/main/img_3502.jpg?raw=true"
answer_7502 = [
    {'input' : [[1, 2, 5, 4, 1, 4, 123, 4]], 'output' : [4/8]},
    {'input' : [[23, 51, 3, 43, 61, 123]], 'output' : [0/6]},
    {'input' : [[6550, 112152, 3144, 62, 12, 124, 142, 52, 98]], 'output' : [9/9]}
]


question_3100 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫번째 숫자</span>와 <span style = "background-color:	#E0E0E0;">두번째 숫자</span>를 곱한 결과를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 첫번째 숫자가, 둘째 줄에 두번째 숫자가 주어집니다.</p>
<p>(1000이하의 숫자가 입력됩니다.)</p>
<h2> 출력
</h2>
<p>첫번째 숫자와 두번째 숫자를 곱한 결과를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 342</p>
<p> 345</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>117990</p>
</div>
'''
img_3100 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_3100 = [
    {'input' : [[13], [21]], 'output' : [273]},
    {'input' : [[19], [212]], 'output' : [4028]},
    {'input' : [[234], [142]], 'output' : [33228]}
]

question_3000 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫번째 숫자</span>와 <span style = "background-color:	#E0E0E0;">두번째 숫자</span>를 곱한 결과를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 첫번째 숫자가, 둘째 줄에 두번째 숫자가 주어집니다.</p>
<p>(1000이하의 숫자가 입력됩니다.)</p>
<h2> 출력
</h2>
<p>첫번째 숫자와 두번째 숫자를 곱한 결과를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 342</p>
<p> 345</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>117990</p>
</div>
'''
img_3000 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_3000 = [
    {'input' : [[13, 21]], 'output' : [273]},
    {'input' : [[19, 212]], 'output' : [4028]},
    {'input' : [[234,142]], 'output' : [33228]}
]

question_3200 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫번째 숫자</span>와 <span style = "background-color:	#E0E0E0;">두번째 숫자</span>를 곱한 결과를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 첫번째 숫자가, 둘째 줄에 두번째 숫자가 주어집니다.</p>
<p>(1000이하의 숫자가 입력됩니다.)</p>
<h2> 출력
</h2>
<p>첫번째 숫자와 두번째 숫자를 곱한 결과를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 342</p>
<p> 345</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>117990</p>
</div>
'''
img_3200 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_3200 = [
    {'input' : [[13], [13, 21]], 'output' : [273]},
    {'input' : [[19], [19,212]], 'output' : [4028]},
    {'input' : [[234], [234,142]], 'output' : [33228]}
]

question_3300 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>2개의 숫자를 입력받습니다.</p>
<p><span style = "background-color:	#E0E0E0;">첫번째 숫자</span>와 <span style = "background-color:	#E0E0E0;">두번째 숫자</span>를 곱한 결과를 출력하는 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>첫째 줄에 첫번째 숫자가, 둘째 줄에 두번째 숫자가 주어집니다.</p>
<p>(1000이하의 숫자가 입력됩니다.)</p>
<h2> 출력
</h2>
<p>첫번째 숫자와 두번째 숫자를 곱한 결과를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 342</p>
<p> 345</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>117990</p>
</div>
'''
img_3300 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_3300 = [
    {'input' : [[13,21], [13]], 'output' : [273]},
    {'input' : [[19,212], [212]], 'output' : [4028]},
    {'input' : [[142,234], [142]], 'output' : [33228]}
]
#colabturtle test
question_6106 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>길이가 <span style = "background-color:	#E0E0E0;">100</span>인 정삼각형을 그려봅시다..</p>
<HR>
<h2> 입력 </h2>
<p>없음</p>
<h2> 출력 </h2>
<p>s.forward(), s.right()를 이용해서 그립니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>길이가 100인 정삼각형</p>
</div>
'''
img_6106 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_6106 = [
    {'input' : [[13,21], [13]], 'output' : ['t = Turtle(window)','t.width(3)', "t.color('red')", 'for i in range(3) : ', ' t.forward(100)', ' t.right(60)']}
]
question_6107 = '''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>길이가 <span style = "background-color:	#E0E0E0;">60</span>인 정육각형을 그려봅시다.</p>
<HR>
<h2> 입력 </h2>
<p>없음</p>
<h2> 출력 </h2>
<p>s.forward(), s.right()를 이용해서 그립니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p> 없음</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>길이가 60인 정삼각형</p>
</div>
'''
img_6107 = "https://github.com/GoHakNeung/python/blob/main/img_1102.jpg?raw=true"
answer_6107 = [
    {'input' : [[13,21], [13]], 'output' : ['t = Turtle(window)','t.width(3)', "t.color('red')", 'for i in range(6) : ', ' t.forward(60)', ' t.right(120)']}
]



question_8000 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>아래 표는 대전, 세종, 충남, 충북의 인구를 나타는 표입니다.</p>
<table border="1"
       cellspacing="0"
       width = 15%
       height = 10>
    <tr>
    	<td>대전</td>
      <td>세종</td>
      <td>충남</td>
      <td>충북</td>
    </tr>
    <tr>
    	<td>150만명</td>
      <td>37만명</td>
      <td>220만명</td>
      <td>160만명</td>      
</table>
<p>대전, 세종, 충남, 충북의 인구수를 원그래프로 나타내봅시다.</p>
<HR>
<h2>데이터</h2>
<p>대전, 세종, 충남, 충북의 인구수</p>
<h2>그래프</h2>
<p>세종시의 인구를 강조하기 위해 원 그래프에서 떨어져서 표시해봅시다.(0.3)</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>labels = ["대전", "세종", "충남" ,"충북"]</p>
<p>pop = [1500000, 370000, 2200000, 1600000]</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<p>label, 백분율이 표시되고 세종시가 강조된 원 그래프</p>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8000.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8000 = ''
question_review_8000 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>원 그래프
<input type='checkbox'/>label
<input type='checkbox'/>백분율
<input type='checkbox'/>explode
'''
answer_8000 = [
    {'input' : [[10]], 'output' : ['labels = ["대전", "세종", "충남" ,"충북"]','x = [1500000, 370000, 2200000, 1600000]','explode = [0,0.3,0,0]','plt.subplot(1,2,2)', 'A_pie=plt.pie(x, labels = labels, autopct = "%.f%%", explode = explode)', 'A_title=plt.title("충청도 인구")', 'plt.show()']}
]

question_8002 = '''scatter
'''
img_8002 = ''
question_review_8002 = ''' 
'''
answer_8002 = [
    {'input' : [[10]], 'output' : ["df = pd.read_csv('/content/jupyter_judge/csv_file/scatter1.csv')",'plt.subplot(1,2,2)',"A_scatter=plt.scatter(df['x'],df['y'])",'A_xlim=plt.xlim(0,100)','A_ylim=plt.ylim(0,100)',"A_title=plt.title('x,y의 산점도')", 'plt.show()']}
]

question_8003 = '''hist
'''
img_8003 = ''
question_review_8003 = ''' 
'''
answer_8003 = [
    {'input' : [[10]], 'output' : ["df = pd.read_csv('/content/jupyter_judge/csv_file/scatter1.csv')",'plt.subplot(1,2,2)',"A_hist=plt.hist(df['x'])",'A_title=plt.title("히스토그램")', 'plt.show()']}
]

question_8004 = '''boxplot
'''
img_8004 = ''
question_review_8004 = ''' 
'''
answer_8004 = [
    {'input' : [[10]], 'output' : ["df = pd.read_csv('/content/jupyter_judge/csv_file/scatter1.csv')",'plt.subplot(1,2,2)',"A_boxplot=plt.boxplot(df['x'])",'A_title=plt.title("박스플롯")', 'plt.show()']}
]



question_8005 = '''plot
'''
img_8005 = ''
question_review_8005 = ''' 
'''
answer_8005 = [
    {'input' : [[10]], 'output' : ['plt.subplot(1,2,2)', 'x = [1,2,3,4,5,6,7,8,9,10]', 'y = [1,3,5,7,8,9,1,2,3,4]', 'z = [2,4,1,2,5,6,2,3,1,2]', "A_plot=plt.plot(x, y, label='linear')", "A_plot=plt.plot(x, z, label='quadratic')", "A_xlabel=plt.xlabel('x label')", "A_ylabel=plt.ylabel('y label')", 'A_xlim=plt.xlim(0,15)', 'A_ylim=plt.ylim(0,10)', 'A_title=plt.title("Simple Plot")', 'A_legend=plt.legend()', 'plt.show()']}
]

question_8006 = '''hlines
'''
img_8006 = ''
question_review_8006 = ''' 
'''
answer_8006 = [
    {'input' : [[10]], 'output' : ['plt.subplot(1,2,2)', 'A_hlines=plt.hlines(1,20,25)', "A_title=plt.title('수평선')", 'plt.show()']}
]

question_8007 = '''vlines
'''
img_8007 = ''
question_review_8007 = ''' 
'''
answer_8007 = [
    {'input' : [[10]], 'output' : ['plt.subplot(1,2,2)', 'A_vlines=plt.vlines(1,20,25)', "A_title=plt.title('수직선')", 'plt.show()']}
]

question_8008 = '''bar
'''
img_8008 = ''
question_review_8008 = ''' 
'''
answer_8008 = [
    {'input' : [[10]], 'output' : ['plt.subplot(1,2,2)', 'a = [1,2,3,4,5]', 'b = [10, 12, 14, 13, 17]', 'A_bar=plt.bar(a,b)', 'A_ylim=plt.ylim(5, 20)', "A_title=plt.title('막대그래프')", 'plt.show()']}
]

question_8009 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>아래 데이터는 8일부터 14일까지 일별 최고기온과 아이스크림 판매량입니다.</p>
<p>일별 최고기온을 꺾은선 그래프로 나타내고 일별 아이스크림 판매량을 막대 그래프로 나타내봅시다.</p>
<HR>
<h2>데이터</h2>
<p>일별 최고기온</p>
<p>일별 아이스크림 판매량</p>
<h2>그래프</h2>
<p>y축 범위는 0 ~ 35로 합니다.</p>
<p>x축 이름은 일, y축 이름은 최고기온으로 합니다.</p>
<p>그래프 이름은 일별 최고기온으로 합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>t_day = ['8일','9일','10일','11일','12일','13일','14일']</p>
<p>max_temp = [30,29,33,32,29,34,31]</p>
<p>sell = [20, 22, 23, 23, 24, 24, 25]</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<p>막대그래프와 꺾은선그래프가 동시에 표현된 그래프</p>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8009.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8009 = ''
question_review_8009 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>막대 그래프
<input type='checkbox'/>꺽은선 그래프
<input type='checkbox'/>y축 범위
<input type='checkbox'/>title
<input type='checkbox'/>x축 이름, y축 이름
'''

answer_8009 = [
    {'input' : [[10]], 'output' : ['plt.subplot(1,2,2)', "t_day = ['8일','9일','10일','11일','12일','13일','14일']", 'max_temp = [30,29,33,32,29,34,31]', 'sell = [20, 22, 23, 23, 24, 24, 25]', 'A_plot=plt.plot(t_day, max_temp)', 'A_bar=plt.bar(t_day, sell)', "A_xlabel=plt.xlabel('일')", "A_ylabel=plt.ylabel('최고기온')", 'A_ylim=plt.ylim(0,35)', "A_title=plt.title('일별 최고기온')", 'plt.show()']}
]

question_8201 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>아래 표는 집에서 학교까지 가는 방법별 걸리는 시간은 다음과 같습니다.</p>
<table border="1"
       cellspacing="0"
       width = 30%
       height = 10>
    <tr>
    	<td>이동 수단</td>
      <td>자동차</td>
      <td>버스</td>
      <td>지하철</td>
      <td>버스와 지하철</td>
    </tr>
    <tr>
    	<td>소요 시간</td>
      <td>35분</td>
      <td>55분</td>
      <td>20분</td>      
      <td>30분</td>      
</table>
<p>집에서 학교까지 가는 이동 수단별 소요 시간을 막대그래프로 표현해봅시다.</p>
<HR>
<h2>데이터</h2>
<p>이동수단 별 걸리는 시간</p>
<h2>그래프</h2>
<p>막대그래프</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>way = ['자동차', '버스', '지하철', '버스와 지하철']</p>
<p>way_time = [35, 55, 20, 30]</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프프 예시 </h2>
<p>가로축 이름 : 이동수단</p>
<p>세로축 이름 : 소요시간</p>
<p>그래프 제목 : 이동수단 별 소요 시간</p>
</div>
'''
img_8201 = ''
question_review_8201 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>x축에 표시된 이름
<input type='checkbox'/>y축 값
<input type='checkbox'/>x축, y축 label
<input type='checkbox'/>그래프 제목
'''
answer_8201 = [
    {'input' : [], 'output' : ["plt.subplot(1,2,2)", "way = ['자동차', '버스', '지하철', '버스와 지하철']", "way_time = [35, 55, 20, 30]", "A_bar=plt.bar(way, way_time)", "A_xlabel=plt.xlabel('이동수단')", "A_ylabel=plt.ylabel('소요시간')", "A_title=plt.title('이동수단 별 소요 시간')", "plt.show()"]}
]

question_8203 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>A도시의 8월 8일부터 14일의 최고온도를 나타낸 자료입니다.</p>
<table border="1"
       cellspacing="0"
       width = 30%
       height = 10>
    <tr>
    	<td>일</td>
      <td>8일</td>
      <td>9일</td>
      <td>10일</td>
      <td>11일</td>
      <td>12일</td>
      <td>13일</td>
      <td>14일</td>
    </tr>
    <tr>
    	<td>기온</td>
      <td>30도</td>
      <td>29도</td>
      <td>33도</td>      
      <td>32도</td>      
      <td>29도</td>
      <td>34도</td>
      <td>31도</td>
</table>
<p>A도시의 8일부터 14일가지 최고기온을 꺽은선 그래프로 나타내봅시다.</p>
<HR>
<h2>데이터</h2>
<p>8일부터 14일까지 최고기온</p>
<h2>그래프</h2>
<p>y축 범위가 0 ~ 35사이인 꺾은선 그래프</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>t_day = [8,9,10,11,12,13,14]</p>
<p>max_temp = [30, 29, 33, 32, 29, 34, 31]</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<p>가로축 이름 : 일</p>
<p>세로축 이름 : 최고기온</p>
<p>세로축 범위 : 0 ~ 35</p>
<p>그래프 제목 : 일별 최고기온</p>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8203.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8203 = ''
question_review_8203 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>x축, y축 label
<input type='checkbox'/>y축 범위
<input type='checkbox'/>그래프 제목
'''
answer_8203 = [
    {'input' : [], 'output' : ["plt.subplot(1,2,2)", "t_day = [8,9,10,11,12,13,14]", "max_temp = [30, 29, 33, 32, 29, 34, 31]", "A_plot=plt.plot(t_day, max_temp)", "A_xlabel=plt.xlabel('일')", "A_ylabel=plt.ylabel('최고기온')", "A_title=plt.title('일별 최고기온')", "A_ylim=plt.ylim(0,35)", "plt.show()"]}
]

question_8206 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>아래 표는 대전, 세종, 충남, 충북의 인구를 나타는 표입니다.</p>
<table border="1"
       cellspacing="0"
       width = 30%
       height = 10>
    <tr>
    	<td>지역</td>
      <td>대전</td>
      <td>세종</td>
      <td>충남</td>
      <td>충북</td>
    </tr>
    <tr>
    	<td>인구</td>
      <td>1,500,000</td>
      <td>370,000</td>
      <td>2,220,000</td>      
      <td>1,600,000</td>      
</table>
<p>세종시의 인구를 강조해서 원 그래프로 나타내봅시다.</p>
<HR>
<h2>데이터</h2>
<p>충청도 지역별 인구</p>
<h2>그래프</h2>
<p>y세종시 인구가 강조(분리된)된 원 그래프</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>labels = [ ]</p>
<p>population = [ ]</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<p>분리된 정도 : 0.3</p>
<p>그래프 제목 : 일별 최고기온</p>
<p>백분율 : 소수점 첫째 자리까지 표시</p>
</div>
'''
img_8206 = ''
question_review_8206 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>원 그래프
<input type='checkbox'/>label
<input type='checkbox'/>백분율
<input type='checkbox'/>explode
<input type='checkbox'/>그래프 제목
'''
answer_8206 = [
    {'input' : [], 'output' : ["plt.subplot(1,2,2)", "labels = ['대전', '세종', '충남', '충북']", "population = [150, 37, 220, 160]", "explode = [0,0.3,0,0]", "plt.pie(labels = labels, x=population, explode = explode, autopct = '%.1f%%')", "plt.title('충청도 지역별 인구')", "plt.show()"]}
]

question_8208 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>push_up.csv 파일(파일경로:'/content/jupyter_judge/csv_file/push_up.csv')은 40명 학생의 팔굽혀펴기 기록이 있습니다. </p> 
<p>40명 학생의 팔굽혀펴기 결과를 히스토그램으로 나타내시오.</p>
<HR>
<h2>데이터</h2>
<p>40명 학생의 팔굽혀펴기 기록</p>
<h2>그래프</h2>
<p>히스토그램</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>csv 파일 속 데이터를 판다스를 이용해서 불러옵니다.</p>
<p>df = pd.read_csv('파일경로')</p>
<p>df.head(n=2)</p>
<table border="1"
       cellspacing="0"
       width = 30%
       height = 10>
    <tr>
    	<td>number</td>
      <td>push_up</td>
    </tr>
    <tr>
    	<td>1</td>
      <td>20</td>
    </tr>
    <tr>
    	<td>2</td>
      <td>14</td>
    </tr>
</table>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<p>계급 : 0~10, 10~20... 10간격</p>
<p>그래프 제목 : 팔굽혀펴기 분포포</p>
<p>그래프에 격자 표시</p>
</div>
'''
img_8208 = ''
question_review_8208 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>데이터프레임으로 그래프 작성
<input type='checkbox'/>히스토그램
<input type='checkbox'/>계급
<input type='checkbox'/>격자표시
<input type='checkbox'/>그래프 제목
'''
answer_8208 = [
    {'input' : [], 'output' : ["plt.subplot(1,2,2)","bins = [0,10,20,30,40,50,60,70]" ,"df = pd.read_csv('/content/jupyter_judge/csv_file/push_up.csv')" ,"plt.hist(df['push_up'], bins = bins)" ,"plt.grid()" ,"plt.title('팔굽혀펴기 분포도')", "plt.show()"]}
]

question_8211 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>다음은 학생 A가 10회에 걸쳐 화살을 쏘아 얻은 점수를 조사하여 만든 자료입니다.</p> 
<p>points = [9, 10, 8, 7, 9, 10, 6, 5, 10, 9]</p>
<p>회차별 점수를 막대그래프로 나타내고 평균에 해당하는 점수에 수평선을 추가하여 나타내봅시다.</p>
<HR>
<h2>데이터</h2>
<p>1~10회에서 얻은 점수</p>
<h2>그래프</h2>
<p>막대그래프와 수평선</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>데이터를 데이터 프레임으로 저장합니다.</p>
<p>df = pd.DataFrame({'col1' : [], 'col2' : []})</p>
<p>df_mean = __</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<p>회차별 점수를 나타내느 막대그래프</p>
<p>점수 평균에 해당하는 수평선</p>
<p>그래프에 격자 표시</p>
<p>x축, y축 label</p>
<p>x축, y축 label</p>
</div>
'''
img_8211 = ''
question_review_8211 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>데이터프레임으로 그래프 작성
<input type='checkbox'/>막대그래프
<input type='checkbox'/>평균 값에서 수평선
<input type='checkbox'/>격자표시
<input type='checkbox'/>그래프 제목
'''
answer_8211 = [
    {'input' : [], 'output' : ["plt.subplot(1,2,2)", "shoot = list(range(1,11,1))", "points = [9, 10, 8, 7, 9, 10, 6, 5, 10, 9]", "df = pd.DataFrame({", "    'shoot' : shoot,", "    'points' : points", "})", "df_mean = df['points'].mean()", "plt.bar(df['shoot'], df['points'])", "plt.hlines(df_mean, 0, 10)", "plt.grid()", "plt.show()"]}
]


question_8219 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>scatter1.csv 파일(파일경로:'/content/jupyter_judge/csv_file/scatter1.csv')은 x,y 값이 저장되어 있습니다. </p> 
<p>x,y를 산점도를 나타내봅시다. </p>
<HR>
<h2>데이터</h2>
<p>x,y 값</p>
<h2>그래프</h2>
<p>히스토그램</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>csv 파일 속 데이터를 판다스를 이용해서 불러옵니다.</p>
<p>df = pd.read_csv('파일경로')</p>
<p>df.head(n=2)</p>
<table border="1"
       cellspacing="0"
       width = 30%
       height = 10>
    <tr>
    	<td>x</td>
      <td>y</td>
    </tr>
    <tr>
    	<td>84</td>
      <td>69</td>
    </tr>
    <tr>
    	<td>54</td>
      <td>27</td>
    </tr>
</table>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<p>그래프 제목 : x,y 산점도</p>
<p>x,y 범위 : 0 ~ 100
<p>그래프에 격자 표시</p>
</div>
'''
img_8219 = ''
question_review_8219 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>데이터프레임으로 그래프 작성
<input type='checkbox'/>산점도
<input type='checkbox'/>x,y 범위
<input type='checkbox'/>그래프 제목
<input type='checkbox'/>상관관계가 있는 그래프일까요?
'''
answer_8219 = [
    {'input' : [], 'output' : ["plt.subplot(1,2,2)", "df = pd.read_csv('/content/jupyter_judge/csv_file/scatter1.csv')", "plt.scatter(df['x'], df['y'])", "plt.xlim(0,100)", "plt.ylim(0,100)", "plt.title('x,y의 산점도')", "plt.show()"]}
]

question_8220 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>scatter2.csv 파일(파일경로:'/content/jupyter_judge/csv_file/scatter2.csv')은 x,y 값이 저장되어 있습니다. </p> 
<p>x,y를 산점도를 나타내봅시다. </p>
<HR>
<h2>데이터</h2>
<p>x,y 값</p>
<h2>그래프</h2>
<p>히스토그램</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>csv 파일 속 데이터를 판다스를 이용해서 불러옵니다.</p>
<p>df = pd.read_csv('파일경로')</p>
<p>df.head(n=2)</p>
<table border="1"
       cellspacing="0"
       width = 30%
       height = 10>
    <tr>
    	<td>x</td>
      <td>y</td>
    </tr>
    <tr>
    	<td>19</td>
      <td>13</td>
    </tr>
    <tr>
    	<td>24</td>
      <td>30</td>
    </tr>
</table>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<p>그래프 제목 : x,y 산점도</p>
<p>x,y 범위 : 0 ~ 100
<p>그래프에 격자 표시</p>
</div>
'''
img_8220 = ''
question_review_8220 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>데이터프레임으로 그래프 작성
<input type='checkbox'/>산점도
<input type='checkbox'/>x,y 범위
<input type='checkbox'/>그래프 제목
<input type='checkbox'/>상관관계가 있는 그래프일까요?
'''
answer_8220 = [
    {'input' : [], 'output' : ["plt.subplot(1,2,2)", "df = pd.read_csv('/content/jupyter_judge/csv_file/scatter2.csv')", "plt.scatter(df['x'], df['y'])", "plt.xlim(0,100)", "plt.ylim(0,100)", "plt.title('x,y의 산점도')", "plt.show()"]}
]
question_8401 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p> 다음은 부산광역시 연도별 자동차 등록 대수와 관련된 공공데이터이다.</p>
<p><a href ="https://www.data.go.kr/data/15063675/fileData.do" target = 'blank'>부산광역시 자동차 등록 대수 공공데이터</a></p>
<p>부산광역시의 연도별 자동차 등록대수를 꺾은선 그래프로 나타내봅시다. 100만에 해당하는 숫자에 수평선을 빨간색으로 그려봅시다.</p>
<h2>데이터</h2>
<p>부산광역시 연도별 자동차 등록대수</p>
<h2>그래프</h2>
<p>연도별 자동차 등록 대수를 꺾은선 그래프로 나타냅니다.</p>
<p>100만에 해당하는 숫자에 1960~2022까지 빨간색 수평선을 그립니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/busan_car.csv')</p>
<p>'연도', '계' 열에 있는 데이터를 사용해봅시다.
<p>그래프 제목은 '연도별 부산시 자동차 등록대수'로 합니다.</p>
</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8401.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8401 = ''
question_review_8401 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>수평선
<input type='checkbox'/>제목
<input type='checkbox'/>데이터 프레임에서 열 선택
'''
answer_8401 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)","df = pd.read_csv('/content/jupyter_judge/csv_file/busan_car.csv')","A_plot=plt.plot(df['연도'], df['계'])", "A_hlines=plt.hlines(1000000,1960, 2022, color = 'red')", "A_title=plt.title('연도별 부산시 자동차 등록대수 변화')", "plt.show()"]}
]

question_8402 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2022년 10대 수출품과 수입품의 중량과 금액에 대한 데이터입니다.</p>
<p><a href ="https://tradedata.go.kr/cts/index.do" target = 'blank'>관세청 홈페이지</a></p>
<p>10대 수출품과 수입품에 대한 데이터를 원 그래프로 그려봅시다.</p>
<h2>데이터</h2>
<p>10대 수출입 품목 및 국가 무역통계</p>
<h2>그래프</h2>
<p>10대 수출품의 수출금액을 가지고 원그래프를 그립니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/trade.csv')</p>
<p>'품목명', '수출금액' 열에 있는 데이터를 사용해봅시다.</p>
<p>그래프 제목은 '2022년 10대 수출품'으로 합니다.</p>
</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8402.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8402 = ''
question_review_8402 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>원 그래프
<input type='checkbox'/>X값
<input type='checkbox'/>label
<input type='checkbox'/>제목
'''
answer_8402 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)","df = pd.read_csv('/content/jupyter_judge/csv_file/trade.csv')", "x = df['수출금액']", "labels = df['품목명']", "A_pie=plt.pie(x,labels = labels, autopct = '%.f%%')", "A_title=plt.title('2022년 10대 수출품')", "plt.show()"]}
]

question_8403 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<p>2022년 월별 온도와 월별로 발생한 식중독 발생 건수입니다.</p>
<p><a href ="https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70" target = 'blank'>기상청 홈페이지</a></p>
<p><a href ="http://www.foodsafetykorea.go.kr/portal/healthyfoodlife/foodPoisoningStat.do?menu_no=519&menu_grp=MENU_GRP02" target = 'blank'>식품의약안전처</a></p>
<p>2022년 월별 온도를 꺾은선 그래프로 나타내고, 월별 식중독 발생건수를 막대 그래프로 그려봅시다.</p>
<h2>데이터</h2>
<p>2022년 월별 평균 온도</p>
<p>2022년 월별 발생한 식중독 발생 건수</p>
<h2>그래프</h2>
<p>월별 온도는 꺾은선 그래프로 나타내고, 월별 식중독 발생 건수는 막대 그래프(빨간색)로 나타냅니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/food_poisoning.csv')</p>
<p>'month', 'outbreak', 'temp' 열에 있는 데이터를 사용해봅시다.</p>
<p>그래프 제목은 '식중독과 온도 그래프'</p>
</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8403.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8403 = ''
question_review_8403 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>막대 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
'''
answer_8403 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)","df = pd.read_csv('/content/jupyter_judge/csv_file/food_poisoning.csv')","A_plt=plt.plot(df.month, df.temp)", "A_bar=plt.bar(df.month, df.outbreak, color = 'red')", "A_title=plt.title('식중독과 온도 그래프')", "A_xlabel=plt.xlabel('월')", "plt.show()"]}
]

question_8501 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>음식물 쓰레기는 환경적인 문제와 경제적인 문제를 모두 가지고 있습니다.</p>
<p>다음 뉴스를 보고 음식물쓰레기의 문제점을 생각해봅시다.<a href ="http://www.greenpostkorea.co.kr/news/articleView.html?idxno=120801" target = 'blank'>음식물 쓰레기 관련 뉴스</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 경상남도는 경상남도 시군에서 발생한 <a href ="https://www.data.go.kr/data/15088741/fileData.do" target = 'blank'>1년간 음식물 쓰레기량(톤)</a>과 <a href ="https://bigdata.gyeongnam.go.kr/index.gn?menuCd=DOM_000000115001006000" target = 'blank'>인구 데이터</a>를 바탕으로 경상남도 시별 음식물 쓰레기량과 1인당 음식물 쓰레기량으로 구성되어 있습니다.</p>
<p>열 : city_province(시), emission(배출량), population(인구), emission_per_person(1인당 음식물 쓰레기 배출량) </p>
<h2>그래프</h2>
<p>경상남도 시에서 제공하는 시군구별 음식물 쓰레기 및 인구와 관련하여 막대 그래프로 그려봅시다.</p>
<p>그래프 제목 : '경상남도 시에서 발생하는 음식물 쓰레기량'</p>
<p>가로축 제목 : '경상남도 시'</p>
<p>세로축 제목 : '음식물 쓰레기량(톤)'</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/food_waste.csv')</p>
<p>city = data['city_province']</p>
<p>emission = data['emission']</p>

</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8501.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8501 = ''
question_review_8501 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>막대 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8501 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)","data = pd.read_csv('/content/jupyter_judge/csv_file/food_waste.csv')",
                                   "city = data['city_province']",
                                   "emission = data['emission']",
                                   "A_bar = plt.bar(city, emission)",
                                   "A_xlabel = plt.xlabel('경상남도 시')",
                                   "A_ylabel = plt.ylabel('음식물 쓰레기량(톤)')",
                                   "A_title = plt.title('경상남도 시에서 발생하는 음식물 쓰레기량')",
                                   "plt.show()"]}
]
question_8502 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>음식물 쓰레기는 환경적인 문제와 경제적인 문제를 모두 가지고 있습니다.</p>
<p>다음 뉴스를 보고 음식물쓰레기의 문제점을 생각해봅시다.<a href ="http://www.greenpostkorea.co.kr/news/articleView.html?idxno=120801" target = 'blank'>음식물 쓰레기 관련 뉴스</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 경상남도는 경상남도 시군에서 발생한 <a href ="https://www.data.go.kr/data/15088741/fileData.do" target = 'blank'>1년간 음식물 쓰레기량(톤)</a>과 <a href ="https://bigdata.gyeongnam.go.kr/index.gn?menuCd=DOM_000000115001006000" target = 'blank'>인구 데이터</a>를 바탕으로 경상남도 시별 음식물 쓰레기량과 1인당 음식물 쓰레기량으로 구성되어 있습니다.</p>
<p>열 : city_province(시), emission(배출량), population(인구), emission_per_person(1인당 음식물 쓰레기 배출량) </p>
<h2>그래프</h2>
<p>가로 축에는 경상남도 시 이름, 세로 축에는 1명당 발생하는 음식물 쓰레기량을 막대 그래프로 나타냅니다.</p>
<p>그래프 제목 : '경상남도 시에서 발생하는 1인당 음식물 쓰레기량'</p>
<p>가로축 제목 : '경상남도 시'</p>
<p>세로축 제목 : '1인당 발생하는 음식물 쓰레기량(단위 : 톤/명)'</p>
<p>색 : 초록색</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/food_waste.csv')</p>
<p>city = data['city_province']</p>
<p>emission_per_person = data['emission_per_person']</p>

</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8502.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8502 = ''
question_review_8502 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>막대 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8502 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                   "data = pd.read_csv('/content/jupyter_judge/csv_file/food_waste.csv')", 
                                   "city = data['city_province']", 
                                   "emission_per_person = data['emission_per_person']", 

                                   "A_bar = plt.bar(city, emission_per_person, color = 'green')", 
                                   "A_xlabel = plt.xlabel('경상남도 시')", 
                                   "A_ylabel = plt.ylabel('1인당 발생하는 음식물 쓰레기량(단위 : 톤/명)')",
                                   "A_title = plt.title('경상남도 시에서 발생하는 1인당 음식물 쓰레기량')",
                                   "plt.show()"]}
]
question_8503 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>사고가 발생한 다음 대처하는 것보다 중요한 것은 예방하는 것입니다. 코로나 19이후 학교에서 발생하는 사고가 늘어나고 있습니다. </p>
<p>학교에서 발생하는 다양하고 많은 사고를 알아보고 이를 예방하는 방법을 생각해봅시다.<a href ="https://munhwa.com/news/view.html?no=2023051901070821043001" target = 'blank'>학교 안전 사고 관련 뉴스</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 한국청소년활동진흥원에서 제공한 <a href ="https://www.data.go.kr/data/15076546/fileData.do" target = 'blank'>청소년 생활(학교) 사고 통계</a>입니다. 2012년부터 2022년까지 데이터이며, 학교급별, 부위별 안전사고 발생 현황으로 구성되어 있습니다.</p>
<p>열 : 연도, 학교급별, 머리(두부), 치아(구강), 흉복부, 팔, 손, 다리, 발, 기타</p>
<h2>그래프</h2>
<p>2022년 초등학교에서 발생한 안전사고 중 부위별 데이터를 막대그래프로 나타내봅시다.</p>
<p>그래프 제목 : '2022년 초등학교에서 발생한 부위별 안전사고</p>
<p>가로축 제목 : '신체 부위'</p>
<p>세로축 제목 : '발생 건수'</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>body_part = ['머리', '치아', '흉복부', '팔', '손', '다리', '팔', '기타']</p>
<p>count = [8943, 2096, 695, 3280, 14263, 3437, 12657, 1274]"</p>


</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8503.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8503 = ''
question_review_8503 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>막대 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8503 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)","data = pd.read_csv('/content/jupyter_judge/csv_file/food_waste.csv')",
                                  "body_part = ['머리', '치아', '흉복부', '팔', '손', '다리', '팔', '기타']",
                                  "count = [8943, 2096, 695, 3280, 14263, 3437, 12657, 1274]",
                                  "A_bar = plt.bar(body_part, count)",
                                  "A_xlabel = plt.xlabel('신체 부위')",
                                  "A_ylabel = plt.ylabel('발생 건수')",
                                  "A_title = plt.title('2022년 초등학교에서 발생한 부위별 안전사고')",
                                  "plt.show()"]

     }
]
question_8504 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>사고가 발생한 다음 대처하는 것보다 중요한 것은 예방하는 것입니다. 코로나 19이후 학교에서 발생하는 사고가 늘어나고 있습니다. </p>
<p>학교에서 발생하는 다양하고 많은 사고를 알아보고 이를 예방하는 방법을 생각해봅시다.<a href ="https://munhwa.com/news/view.html?no=2023051901070821043001" target = 'blank'>학교 안전 사고 관련 뉴스</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 한국청소년활동진흥원에서 제공한 <a href ="https://www.data.go.kr/data/15076546/fileData.do" target = 'blank'>청소년 생활(학교) 사고 통계</a>입니다. 2014년부터 2022년까지 데이터이며, 학교급별, 시간별 안전사고 발생 현황으로 구성되어 있습니다.</p>
<p>열 : 연도, 학교급별, 수업, 체육, 점심, 석식, 휴식_청소, 특별활동, 학교행사, 등하교, 기숙사, 기타</p>
<h2>그래프</h2>
<p>2022년 초등학교에서 발생한 안전사고 중 부위별 데이터를 막대그래프로 나타내봅시다.</p>
<p>그래프 제목 : '2022년 초등학교에서 발생한 시간별 안전사고</p>
<p>가로축 제목 : '장소'</p>
<p>세로축 제목 : '발생 건수'</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>time = ['수업', '체육', '점심', '휴식_청소', '특별활동', '학교행사', '등하교', '기타']</p>
<p>count = [7606, 17077, 11761, 8282, 953, 1628, 4086, 1355]</p>


</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8504.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8504 = ''
question_review_8504 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>막대 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8504 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)","data = pd.read_csv('/content/jupyter_judge/csv_file/food_waste.csv')",
                                  "time = ['수업', '체육', '점심', '휴식_청소', '특별활동', '학교행사', '등하교',  '기타']",
                                  "count = [7606, 17077, 11761,  8282, 953, 1628, 4086,  1355]",
                                  "plt.bar(time, count)",
                                  "plt.xlabel('장소')",
                                  "plt.ylabel('발생 건수')",
                                  "plt.title('2022년 초등학교에서 발생한 시간별 안전사고')",
                                  "plt.show()"]

     }
]



question_8511 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>2050년 탄소중립을 달성하기 위해 전력 생산의 많은 비중을 차지하는 화석연료를 재생에너지, 신에너지로의 전환 문제를 다루고 있는 신문기사입니다.</p>
<p>다음 뉴스를 보고 탄소중립과 발전하는데 사용하는 에너지원을 생각해봅시다. <a href ="https://www.etnews.com/20210416000107" target = 'blank'>발전 관련 뉴스</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 한전에서 제공하는 <a href ="https://epsis.kpx.or.kr/epsisnew/selectEkgeGepTotChart.do?menuId=060101" target = 'blank'>전원별 발전량</a>을 바탕으로 연도별, 전원별 발전량로 구성되어 있습니다.</p>
<p>열 : year(연도), thermal(화력), LNG(천연가스), nuclear(원자력), renewable(신재생), other(기타), individual(개별발전) </p>
<h2>그래프</h2>
<p>2022년 에너지원별 발전량을 막대그래프로 그려봅시다.</p>
<p>2022년 전원별 발전량을 가로 축에는 전원별 이름, 세로 축에는 발전량(MWh)으로 막대그래프로 나타내봅시다.</p>
<p>그래프 제목 : 에너지원별 발전량</p>
<p>가로축 제목 : 에너지원</p>
<p>세로축 제목 : 발전량(MWh)</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>energy_source = ['thermal', 'LNG', 'nuclear', 'renewable', 'other', 'individual']</p>
<p>amount = [188476694,123995839,176054012,47266256, 58156521, 30650791]</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8511.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8511 = ''
question_review_8511 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>막대 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8511 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                   "energy_source = ['thermal', 'LNG', 'nuclear', 'renewable', 'other', 'individual']",
                                   "amount = [188476694,123995839,176054012,47266256, 58156521, 30650791]",
                                   "A_bar = plt.bar(energy_source, amount)", 
                                   "A_xlabel = plt.xlabel('에너지원')", 
                                   "A_ylabel = plt.ylabel('발전량(MWh)')", 
                                   "A_title = plt.title('에너지원별 발전량')",
                                   "plt.show()"]}
]
question_8512 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>2050년 탄소중립을 달성하기 위해 전력 생산의 많은 비중을 차지하는 화석연료를 재생에너지, 신에너지로의 전환 문제를 다루고 있는 신문기사입니다.</p>
<p>다음 뉴스를 보고 탄소중립과 발전하는데 사용하는 에너지원을 생각해봅시다. <a href ="https://www.etnews.com/20210416000107" target = 'blank'>발전 관련 뉴스</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 한전에서 제공하는 <a href ="https://epsis.kpx.or.kr/epsisnew/selectEkgeGepTotChart.do?menuId=060101" target = 'blank'>전원별 발전량</a>을 바탕으로 연도별, 전원별 발전량로 구성되어 있습니다.</p>
<p>열 : year(연도), thermal(화력), LNG(천연가스), nuclear(원자력), renewable(신재생), other(기타), individual(개별발전) </p>
<h2>그래프</h2>
<p>가로 축에는 연도, 세로 축에는 신재생 에너지 발전량(MWh)으로 꺾은선 그래프를 나타냅니다.</p>
<p>그래프 제목 : 연도별 신재생 에너지 발전량</p>
<p>가로축 제목 : 연도</p>
<p>세로축 제목 : 신재생 에너지 발전량(MWh)</p>
<p>가로축 범위 : 2010 ~ 2022</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/output_by_the_material.csv')</p>
<p>year = data['year']</p>
<p>renewable = data['renewable]</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8512.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8512 = ''
question_review_8512 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
<input type='checkbox'/>xlim
'''
answer_8512 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                   "data = pd.read_csv('/content/jupyter_judge/csv_file/output_by_the_material.csv')", 
                                   "year_ = data['year']", 
                                   "renewable_ = data['renewable']", 
                                   "A_plot = plt.plot(year_, renewable_)", 
                                   "A_xlabel = plt.xlabel('연도')", 
                                   "A_ylabel = plt.ylabel('신재생 에너지 발전량(MWh)')", 
                                   "A_xlim = plt.xlim(2010,2022)", 
                                   "A_title = plt.title('연도별 신재생 에너지 발전량')", 
                                   "plt.show()"]}
]
question_8513 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>2050년 탄소중립을 달성하기 위해 전력 생산의 많은 비중을 차지하는 화석연료를 재생에너지, 신에너지로의 전환 문제를 다루고 있는 신문기사입니다.</p>
<p>다음 뉴스를 보고 탄소중립과 발전하는데 사용하는 에너지원을 생각해봅시다. <a href ="https://www.etnews.com/20210416000107" target = 'blank'>발전 관련 뉴스</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 한전에서 제공하는 <a href ="https://epsis.kpx.or.kr/epsisnew/selectEkgeGepTotChart.do?menuId=060101" target = 'blank'>전원별 발전량</a>을 바탕으로 연도별, 전원별 발전량로 구성되어 있습니다.</p>
<p>열 : year(연도), thermal(화력), LNG(천연가스), nuclear(원자력), renewable(신재생), other(기타), individual(개별발전) </p>
<h2>그래프</h2>
<p>가로 축에는 연도, 세로 축에는 화력 발전량(MWh)과 신재생 에너지 발전량(MWh)으로 꺾은선 그래프를 나타냅니다.</p>
<p>그래프 제목 : 연도별 신재생 및 화력 에너지 발전량</p>
<p>가로축 제목 : 연도</p>
<p>세로축 제목 : 에너지 발전량(MWh)</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/output_by_the_material.csv')</p>
<p>year = data['year']</p>
<p>renewable = data['renewable']</p>
<p>thermal = data['thermal']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8513.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8513 = ''
question_review_8513 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8513 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                   "data = pd.read_csv('/content/jupyter_judge/csv_file/output_by_the_material.csv')", 
                                   "year_ = data['year']", 
                                   "renewable_ = data['renewable']", 
                                   "thermal_ = data['thermal']", 
                                   "A_plot = plt.plot(year_, renewable_)", 
                                   "A_plot = plt.plot(year_, thermal_)", 
                                   "A_xlabel = plt.xlabel('연도')",
                                   "A_ylabel = plt.ylabel('에너지 발전량(MWh)')", 
                                   "A_title = plt.title('연도별 신재생 및 화력 에너지 발전량')", 
                                   "plt.show()"]}
]
question_8521 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>양성평등 사회로 나아가기 위한 방법 중 하나인 아빠의 육아와 관련된 신문기사입니다.</p>
<p>다음 뉴스를 보고 아빠의 육아와 양성평등을 생각해봅시다. <a href ="https://www.sisain.co.kr/news/articleView.html?idxno=49406" target = 'blank'>아빠의 육아</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 KOSIS에서 육아휴직과 관련하여 제공하는 <a href ="https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_CC2020B001&vw_cd=MT_ZTITLE&list_id=D_002_002_001&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE" target = 'blank'>출생아 100명당 출생아 부,모 중 육아휴직자</a>수입니다.</p>
<p>열 : year(연도), father(아빠의 육아휴직자 수), mother(엄마의 육아휴직자 수), total(합계) </p>
<h2>그래프</h2>
<p>연도별 엄마의 육아휴직자 수를 꺾은선 그래프로 나타내봅시다.</p>
<p>그래프 제목 : 출생아 100명당 엄마 육아휴직자 수의 연도별 변화</p>
<p>가로축 제목 : 연도</p>
<p>세로축 제목 : 육아휴직자 수(명)</p>
<p>label : mother</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/babybreak.csv')</p>
<p>year = data['year']</p>
<p>mother = data['mother']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8521.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8521 = ''
question_review_8521 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
<input type='checkbox'/>label
'''
answer_8521 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                   "year = data['year']",
                                   "data = pd.read_csv('/content/jupyter_judge/csv_file/babybreak.csv')", 
                                   "mother = data['mother']", 
                                   "A_plot = plt.plot(year, mother, label = 'mother')", 
                                   "A_xlabel = plt.xlabel('연도')", 
                                   "A_ylabel = plt.ylabel('육아휴직자 수(명)')", 
                                   "A_title = plt.title('출생아 100명당 엄마 육아휴직자 수의 연도별 변화')", 
                                   "plt.show()"]}
]
question_8522 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>양성평등 사회로 나아가기 위한 방법 중 하나인 아빠의 육아와 관련된 신문기사입니다.</p>
<p>다음 뉴스를 보고 아빠의 육아와 양성평등을 생각해봅시다. <a href ="https://www.sisain.co.kr/news/articleView.html?idxno=49406" target = 'blank'>아빠의 육아</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 KOSIS에서 육아휴직과 관련하여 제공하는 <a href ="https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_CC2020B001&vw_cd=MT_ZTITLE&list_id=D_002_002_001&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE" target = 'blank'>출생아 100명당 출생아 부,모 중 육아휴직자</a>수입니다.</p>
<p>열 : year(연도), father(아빠의 육아휴직자 수), mother(엄마의 육아휴직자 수), total(합계) </p>
<h2>그래프</h2>
<p>연도별 아빠의 육아휴직자 수를 꺾은선 그래프로 나타내봅시다.</p>
<p>그래프 제목 : 출생아 100명당 아빠 육아휴직자 수의 연도별 변화</p>
<p>가로축 제목 : 연도</p>
<p>세로축 제목 : 육아휴직자 수(명)</p>
<p>label : father</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/babybreak.csv')</p>
<p>year = data['year']</p>
<p>father = data['father']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8522.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8522 = ''
question_review_8522 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
<input type='checkbox'/>label
'''
answer_8522 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                   "data = pd.read_csv('/content/jupyter_judge/csv_file/babybreak.csv')", 
                                   "year = data['year']", 
                                   "father = data['father']", 
                                   "A_plot = plt.plot(year, father, label = 'father')", 
                                   "A_xlabel = plt.xlabel('연도')", 
                                   "A_ylabel = plt.ylabel('육아휴직자 수(명)')", 
                                   "A_title = plt.title('출생아 100명당 아빠 육아휴직자 수의 연도별 변화')", 
                                   "plt.show()"]}
]
question_8523 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>양성평등 사회로 나아가기 위한 방법 중 하나인 아빠의 육아와 관련된 신문기사입니다.</p>
<p>다음 뉴스를 보고 아빠의 육아와 양성평등을 생각해봅시다. <a href ="https://www.sisain.co.kr/news/articleView.html?idxno=49406" target = 'blank'>아빠의 육아</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 KOSIS에서 육아휴직과 관련하여 제공하는 <a href ="https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_CC2020B001&vw_cd=MT_ZTITLE&list_id=D_002_002_001&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE" target = 'blank'>출생아 100명당 출생아 부,모 중 육아휴직자</a>수입니다.</p>
<p>열 : year(연도), father(아빠의 육아휴직자 수), mother(엄마의 육아휴직자 수), total(합계) </p>
<h2>그래프</h2>
<p>연도별 엄마와 아빠의 육아휴직자 수를 꺾은선 그래프로 나타내봅시다.</p>
<p>그래프 제목 : 연도별 출생아 100명당 육아휴직자 수</p>
<p>가로축 제목 : 연도</p>
<p>세로축 제목 : 육아휴직자 수(명)</p>
<p>label : mother, father이며 그래프에 범례를 표시합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/babybreak.csv')</p>
<p>year = data['year']</p>
<p>mother = data['mother']</p>
<p>father = data['father']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8523.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8523 = ''
question_review_8523 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
<input type='checkbox'/>label
'''
answer_8523 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                   "data = pd.read_csv('/content/jupyter_judge/csv_file/babybreak.csv')", 
                                   "year = data['year']", 
                                   "mother = data['mother']", 
                                   "father = data['father']", 
                                   "A_plot = plt.plot(year, mother, label = 'mother')", 
                                   "A_plot = plt.plot(year, father, label = 'father')", 
                                   "A_xlabel = plt.xlabel('연도')", 
                                   "A_ylabel = plt.ylabel('육아휴직자 수(명)')", 
                                   "A_legend = plt.legend()", 
                                   "A_title= plt.title('연도별 출생아 100명당 육아휴직자 수')", 
                                   "plt.show()"]}
]
question_8524 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>초등학교에서는 대체로 여자 아이가 남자 아이보다 더 크지만 중학교 이후부터는 남자 아이가 여자 아이보다 더 큽니다.</p>
<p>이는 남자 아이와 여자 아이의 성장 속도가 다르기 때문입니다.<a href ="http://www.bosa.co.kr/news/articleView.html?idxno=2160542" target = 'blank'>남자 아이와 여자 아이의 성장 속도 관련 뉴스</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 교육부에서 제공한 <a href ="https://www.data.go.kr/data/15051014/fileData.do" target = 'blank'>학교건강검사 조사결과</a>입니다. 만6세부터 만18세까지 성별 키와 몸무게 데이터로 구성되어 있습니다.</p>
<p>열 : 나이, 성별, 키(cm), 몸무게(kg)</p>
<h2>그래프</h2>

<p>나이별 남성의 키 변화를 꺾은선 그래프로 나태내봅시다.</p>
<p>그래프 제목 : 나이에 따른 남성의 키</p>
<p>가로축 제목 : 나이</p>
<p>세로축 제목 : 키(cm)</p>
<p>label : 남성</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')</p>
<p>data_man = data[data['성별'] == '남']</p>
<p>man_height = data_man['키(cm)']</p>
</p>age = data_man['나이']</p>

</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8524.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8524 = ''
question_review_8524 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
<input type='checkbox'/>legend
'''
answer_8524 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)","data = pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')",
                                  "data_man = data[data['성별'] == '남']",
                                  "man_height = data_man['키(cm)']",
                                  "age = data_man['나이']",
                                  "A_plot = plt.plot(age, man_height, label = '남')",
                                  "A_xlabel = plt.xlabel('나이')",
                                  "A_ylabel = plt.ylabel('키(cm)')",
                                  "A_title = plt.title('나이에 따른 남성의 키')",
                                  "A_legned = plt.legend()",
                                  "plt.show()"]

     }
]
question_8525 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>초등학교에서는 대체로 여자 아이가 남자 아이보다 더 크지만 중학교 이후부터는 남자 아이가 여자 아이보다 더 큽니다.</p>
<p>이는 남자 아이와 여자 아이의 성장 속도가 다르기 때문입니다.<a href ="http://www.bosa.co.kr/news/articleView.html?idxno=2160542" target = 'blank'>남자 아이와 여자 아이의 성장 속도 관련 뉴스</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 교육부에서 제공한 <a href ="https://www.data.go.kr/data/15051014/fileData.do" target = 'blank'>학교건강검사 조사결과</a>입니다. 만6세부터 만18세까지 성별 키와 몸무게 데이터로 구성되어 있습니다.</p>
<p>열 : 나이, 성별, 키(cm), 몸무게(kg)</p>
<h2>그래프</h2>

<p>나이별 여성의 키 변화를 꺾은선 그래프로 나태내봅시다.</p>
<p>그래프 제목 : 나이에 따른 여성의 키</p>
<p>가로축 제목 : 나이</p>
<p>세로축 제목 : 키(cm)</p>
<p>label : 여성</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')</p>
<p>data_woman = data[data['성별'] == '여']</p>
<p>woman_height = data_woman['키(cm)']</p>
</p>age = data_woman['나이']</p>

</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8525.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8525 = ''
question_review_8525 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
<input type='checkbox'/>legend
'''
answer_8525 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)","data = pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')",
                                  "data_woman = data[data['성별'] == '여']",
                                  "woman_height = data_woman['키(cm)']",
                                  "age = data_woman['나이']",
                                  "A_plot = plt.plot(age, woman_height, label = '여')",
                                  "A_xlabel = plt.xlabel('나이')",
                                  "A_ylabel = plt.ylabel('키(cm)')",
                                  "A_title = plt.title('나이에 따른 여성의 키')",
                                  "A_legned = plt.legend()",
                                  "plt.show()"]

     }
]
question_8526 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>초등학교에서는 대체로 여자 아이가 남자 아이보다 더 크지만 중학교 이후부터는 남자 아이가 여자 아이보다 더 큽니다.</p>
<p>이는 남자 아이와 여자 아이의 성장 속도가 다르기 때문입니다.<a href ="http://www.bosa.co.kr/news/articleView.html?idxno=2160542" target = 'blank'>남자 아이와 여자 아이의 성장 속도 관련 뉴스</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 교육부에서 제공한 <a href ="https://www.data.go.kr/data/15051014/fileData.do" target = 'blank'>학교건강검사 조사결과</a>입니다. 만6세부터 만18세까지 성별 키와 몸무게 데이터로 구성되어 있습니다.</p>
<p>열 : 나이, 성별, 키(cm), 몸무게(kg)</p>
<h2>그래프</h2>

<p>나이별 남성과 여성의 키 변화를 꺾은선 그래프로 나태내봅시다.</p>
<p>그래프 제목 : 나이에 따른 남성, 여성의 키</p>
<p>가로축 제목 : 나이</p>
<p>세로축 제목 : 키(cm)</p>
<p>label : 남성, 여성</p>
<p>color : 남성은 파랑, 여성은 빨강</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')</p>
<p>data_man = data[data['성별'] == '남']</p>
<p>man_height = data_man['키(cm)']</p>
<p>data_woman = data[data['성별'] == '여']</p>
<p>woman_height = data_woman['키(cm)']</p>
</p>age = data_man['나이']</p>

</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8526.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8526 = ''
question_review_8526 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
<input type='checkbox'/>color
<input type='checkbox'/>legend
'''
answer_8526 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)","data = pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')",
                                  "data_man = data[data['성별'] == '남']",
                                  "man_height = data_man['키(cm)']",
                                  "data_woman = data[data['성별'] == '여']",
                                  "woman_height = data_woman['키(cm)']",
                                  "age = data_man['나이']",
                                  "A_plot = plt.plot(age, man_height, label = '남', color = 'blue')",
                                  "A_plot = plt.plot(age, woman_height, label = '여', color = 'red')",
                                  "A_xlabel = plt.xlabel('나이')",
                                  "A_ylabel = plt.ylabel('키(cm)')",
                                  "A_title = plt.title('나이에 따른 남성, 여성의 키')",
                                  "A_legned = plt.legend()",
                                  "plt.show()"]

     }
]




question_8531 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>코로나 19로 인한 발생한 학습 결손을 해결하기 위해 늘어나고 있는 사교육비와 관련된 신문기사입니다.</p>
<p>다음 뉴스를 보고 코로나와 사교육비를 생각해봅시다. <a href ="https://www.yna.co.kr/view/AKR20230307079000530" target = 'blank'>늘어나는 사교육비</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 KOSIS에서 사교육비 실태를 조사하여 제공하는 <a href ="https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE003&vw_cd=MT_ZTITLE&list_id=H1_10_003&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_ZTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do" target = 'blank'>연도별 학교급별 사교육비 총액</a>에서 초등학교만 나타낸 데이터입니다.</p>
<p>열 : 연도, 초등학교 과목, 중학교 과목, 고등학교 과목 등</p>
<h2>그래프</h2>
<p>2022년의 초등학교, 중학교, 고등학교 사교육비를 원그래프로 나타내봅시다.</p>
<p>그래프 제목 : 학교급별 사교육비 총액</p>
<p>백분율을 넣습니다.</p>
<p>초등학교 부분을 분리하여 강조합니다.(explode = [0.1, 0, 0])</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>school = ['초등학교', '중학교', '고등학교']</p>
<p>amount = [119055, 70832, 69651]
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8531.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8531 = ''
question_review_8531 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>원 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>autopct
<input type='checkbox'/>explode
'''
answer_8531 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                   "school = ['초등학교', '중학교', '고등학교']", 
                                   "amount = [119055, 70832, 69651]", 
                                   "A_pie = plt.pie(amount, labels = school, explode = [0.1, 0, 0], autopct = '%1.f%%')", 
                                   "A_title = plt.title('학교급별 사교육비 총액')", 
                                   "plt.show()"                                   ]}
]
question_8532 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>코로나 19로 인한 발생한 학습 결손을 해결하기 위해 늘어나고 있는 사교육비와 관련된 신문기사입니다.</p>
<p>다음 뉴스를 보고 코로나와 사교육비를 생각해봅시다. <a href ="https://www.yna.co.kr/view/AKR20230307079000530" target = 'blank'>늘어나는 사교육비</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 KOSIS에서 사교육비 실태를 조사하여 제공하는 <a href ="https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE003&vw_cd=MT_ZTITLE&list_id=H1_10_003&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_ZTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do" target = 'blank'>연도별 학교급별 사교육비 총액</a>에서 초등학교만 나타낸 데이터입니다.</p>
<p>열 : 연도, 초등학교 과목, 중학교 과목, 고등학교 과목 등</p>
<h2>그래프</h2>
<p>2022년의 초등학교 과목별 사교육비 총액을 원그래프로 나타내봅시다.</p>
<p>그래프 제목 : 2022년 초등학교 과목별 사교육비</p>
<p>백분율을 넣습니다.(autopct = '%1.f%%')</p>
<p>일반교과 부분을 분리하여 강조합니다.(explode = [0.1, 0, 0, 0])</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>subject = ['일반교과', '예체능', '취업', '진로']</p>
<p>price_sub = [74849, 43973, 0, 233]</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8532.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8532 = ''
question_review_8532 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>원 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>autopct
<input type='checkbox'/>explode
'''
answer_8532 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                  "subject = ['일반교과', '예체능', '취업', '진로']", 
                                  "price_sub = [74849, 43973, 0, 233]", 
                                  "A_pie = plt.pie(price_sub, labels = subject, explode = [0.1, 0, 0, 0], autopct = '%1.f%%')", 
                                  "A_title = plt.title('2022년 초등학교 과목별 사교육비')", 
                                  "plt.show()"                                   ]}
]
question_8533 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>코로나 19로 인한 발생한 학습 결손을 해결하기 위해 늘어나고 있는 사교육비와 관련된 신문기사입니다.</p>
<p>다음 뉴스를 보고 코로나와 사교육비를 생각해봅시다. <a href ="https://www.yna.co.kr/view/AKR20230307079000530" target = 'blank'>늘어나는 사교육비</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 KOSIS에서 사교육비 실태를 조사하여 제공하는 <a href ="https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE003&vw_cd=MT_ZTITLE&list_id=H1_10_003&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_ZTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do" target = 'blank'>연도별 학교급별 사교육비 총액</a>에서 초등학교만 나타낸 데이터입니다.</p>
<p>열 : 연도, 초등학교 과목, 중학교 과목, 고등학교 과목 등</p>
<h2>그래프</h2>
<p>2022년의 초등학교 일반교과의 과목별 사교육비 총액을 원그래프로 나타내봅시다.</p>
<p>그래프 제목 : 2022년 초등학교 일반과목 과목별 사교육비</p>
<p>백분율을 넣습니다.(autopct = '%1.f%%')</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>gen_subject = ['국어' ,'영어', '수학', '사회과학', '논술', '컴퓨터', '제2외국어']</p>
<p>gen_price = [7082, 34525, 22585, 2989, 5398, 914, 1357]</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8533.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8533 = ''
question_review_8533 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>원 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>autopct
'''
answer_8533 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                  "gen_subject = ['국어' ,'영어', '수학', '사회과학', '논술', '컴퓨터', '제2외국어']", 
                                  "gen_price = [7082, 34525, 22585, 2989, 5398, 914, 1357]", 
                                  "A_pie = plt.pie(gen_price, labels = gen_subject, autopct = '%1.f%%')", 
                                  "A_title = plt.title('2022년 초등학교 일반과목 과목별 사교육비')", 
                                  "plt.show()"                                   ]}
]
question_8534 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>코로나 19로 인한 발생한 학습 결손을 해결하기 위해 늘어나고 있는 사교육비와 관련된 신문기사입니다.</p>
<p>다음 뉴스를 보고 코로나와 사교육비를 생각해봅시다. <a href ="https://www.yna.co.kr/view/AKR20230307079000530" target = 'blank'>늘어나는 사교육비</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 KOSIS에서 사교육비 실태를 조사하여 제공하는 <a href ="https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE003&vw_cd=MT_ZTITLE&list_id=H1_10_003&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_ZTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do" target = 'blank'>연도별 학교급별 사교육비 총액</a>에서 초등학교만 나타낸 데이터입니다.</p>
<p>열 : 연도, 초등학교 과목, 중학교 과목, 고등학교 과목 등</p>
<h2>그래프</h2>
<p>연도별 초등학교 사교육비 총액을 꺾은선 그래프로 나타내봅시다.</p>
<p>그래프 제목 : 연도별 초등학교 사교육비 총액</p>
<p>가로축 제목 : 연도</p>
<p>세로축 제목 : 사교육비(억원)</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/private_education_expense.csv')</p>
<p>year = data['연도']</p>
<p>ele = data['초등학교_전체']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8534.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8534 = ''
question_review_8534 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>꺾은선 그래프
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
<input type='checkbox'/>title
'''
answer_8534 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/private_education_expense.csv')",
                                  "year = data['연도']", 
                                  "total_ele = data['초등학교_전체']", 
                                  "A_plot = plt.plot(year, total_ele)", 
                                  "A_title = plt.title('연도별 초등학교 사교육비 총액')", 
                                  "A_xlabel = plt.xlabel('연도')", 
                                  "A_ylabel = plt.ylabel('사교육비(억원)')", 
                                  "plt.show()"                                   ]}
]
question_8541 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>교통사고로 인해 발생하는 사회비용(사상자의 물리적 손실비용과 정신적 고통 비용)을 다루는 신문기사입니다.</p>
<p>다음 뉴스를 보고 지역별 교통사고 현황과 그 이유를 생각해봅시다. <a href ="https://www.etoday.co.kr/news/view/1912232" target = 'blank'>지역별로 차이나는 교통사고</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 교통사고분석시스템(TAAS)에서 제공하는 <a href ="https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE003&vw_cd=MT_ZTITLE&list_id=H1_10_003&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_ZTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do" target = 'blank'>인구 10만명당 교통사고</a>에 권역을 추가했습니다.</p>
<p>열 : city_province(시도 이름), metropolitan_city(권역 이름),accident(교통사고 발생건수), death(교통사고 사망자 수)</p>
<p>기존 데이터에서 권역(metropolitan_city)을 추가하고 부상자 수를 삭제함</p>

<h2>그래프</h2>
<p>경상도에서 발생한 교통사고 사망자 수를 막대그래프로 나타내봅시다. </p>
<p>그래프 제목 : 경상도에서 발생하는 인구 10만명당 교통사고 사망자 수</p>
<p>가로축 제목 : 경상도 시도(명)</p>
<p>세로축 제목 : 사망자 수</p>

<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/car_accident.csv')</p>
<p>data_city = data[data['metropolitan_city'] == '경상도']</p>
<p>city_province = data_city['city_province']</p>
<p>death = data_city['death']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8541.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8541 = ''
question_review_8541 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>막대 그래프
<input type='checkbox'/>제목
<input type='checkbox'/>가로축 이름
<input type='checkbox'/>세로축 이름

'''
answer_8541 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/car_accident.csv')", 
                                  "data_city = data[data['metropolitan_city'] == '경상도']", 
                                  "city_province = data_city['city_province']", 
                                  "death = data_city['death']", 
                                  "A_bar = plt.bar(city_province, death)", 
                                  "A_xlabel = plt.xlabel('경상도 시도(명)')",
                                  "A_ylabel = plt.ylabel('사망자 수')",
                                  "A_title = plt.title('경상도에서 발생하는 인구 10만명당 교통사고 사망자 수')", 
                                  "plt.show()"                                   ]}
]
question_8542 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>교통사고로 인해 발생하는 사회비용(사상자의 물리적 손실비용과 정신적 고통 비용)을 다루는 신문기사입니다.</p>
<p>다음 뉴스를 보고 지역별 교통사고 현황과 그 이유를 생각해봅시다. <a href ="https://www.etoday.co.kr/news/view/1912232" target = 'blank'>지역별로 차이나는 교통사고</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 교통사고분석시스템(TAAS)에서 제공하는 <a href ="https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE003&vw_cd=MT_ZTITLE&list_id=H1_10_003&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_ZTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do" target = 'blank'>인구 10만명당 교통사고</a>에 권역을 추가했습니다.</p>
<p>열 : city_province(시도 이름), metropolitan_city(권역 이름), accident(교통사고 발생건수), death(교통사고 사망자 수)</p>
<p>기존 데이터에서 권역(metropolitan_city)을 추가하고 부상자 수를 삭제함</p>
<h2>그래프</h2>
<p>17개 시도에서 발생한 교통사고 사망자 수를 히스토그램으로 나타내봅시다.</p>
<p>계급의 크기는 1이며, 계급은 bins = [2,3,4,5,6,7,8,9,10,11,12]입니다.</p>
<p>그래프 제목 : 17개 시도에서 발생한 인구 10만명당 교통사고 사망자 히스토그램</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/car_accident.csv')</p>
<p>death = data['death']
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8542.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8542 = ''
question_review_8542 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>히스토그램
<input type='checkbox'/>bins
'''
answer_8542 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/car_accident.csv')", 
                                  "death = data['death']", 
                                  "A_hist = plt.hist(death, bins = [2,3,4,5,6,7,8,9,10,11,12])", 
                                  "A_xlabel = plt.xlabel('사망자 수(명)')", 
                                  "A_title = plt.title('17개 시도에서 발생한 인구 10만명당 교통사고 사망자 히스토그램')", 
                                  "plt.show()"                                   ]}
]
question_8543 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>평균에 가까운 값은 많이 관찰 되고, 평균에서 멀어지는 값은 적게 관찰 되는 것을 경험상 알 수 있습니다.</p>
<p>예를 들어 키가 평균인 사람은 많지만, 키가 엄청 크거나 엄청 작은 사람은 매우 적습니다. 이는 정규분포로 나타낼 수 있습니다. <a href ="https://terms.naver.com/entry.naver?docId=3569149&cid=58944&categoryId=58970" target = 'blank'>정규 분포</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 교육부에서 제공한 <a href ="https://www.data.go.kr/data/15100360/fileData.do" target = 'blank'>학교건강검사 표본조사</a>입니다. 초1부터 고3까지 9만명의 건강 데이터로 구성되어 있습니다.</p>
<p>열 : 도시구분, 시도, 학교급, 학년, 성별, 키, 몸무게</p>
<p>문제에서는 전처리한 데이터를 제공합니다.</p>
<h2>그래프</h2>
<p>중3 학생의 키를 히스토그램으로 나타내봅시다.</p>
<p>그래프 제목 : 중3학생의 키</p>
<p>가로축 제목 : 키(cm)</p>
<p>구간 : 12</p>
<p>범위 : 130 ~ 190</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/total_checkup.csv')</p>
<p>data_mid = data[data['학년']=='중3']['키']</p>

</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8543.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8543 = ''
question_review_8543 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>히스토그램
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>bins
<input type='checkbox'/>range
'''
answer_8543 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/total_checkup.csv')",
                                  "data_mid = data[data['학년']=='중3']['키']",
                                  "A_hist = plt.hist(data_mid,bins = 12, range = [130, 190])",
                                  "A_title = plt.title('중3학생의 키')",
                                  "A_xlabel = plt.xlabel('키(cm)')",
                                  "plt.show()"]

     }
]
question_8544 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>평균에 가까운 값은 많이 관찰 되고, 평균에서 멀어지는 값은 적게 관찰 되는 것을 경험상 알 수 있습니다.</p>
<p>예를 들어 키가 평균인 사람은 많지만, 키가 엄청 크거나 엄청 작은 사람은 매우 적습니다. 이는 정규분포로 나타낼 수 있습니다. <a href ="https://terms.naver.com/entry.naver?docId=3569149&cid=58944&categoryId=58970" target = 'blank'>정규 분포</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 교육부에서 제공한 <a href ="https://www.data.go.kr/data/15100360/fileData.do" target = 'blank'>학교건강검사 표본조사</a>입니다. 초1부터 고3까지 9만명의 건강 데이터로 구성되어 있습니다.</p>
<p>열 : 도시구분, 시도, 학교급, 학년, 성별, 키, 몸무게</p>
<p>문제에서는 전처리한 데이터를 제공합니다.</p>
<h2>그래프</h2>
<p>중3 학생의 몸무게를 히스토그램으로 나타내봅시다.</p>
<p>그래프 제목 : 중3학생의 몸무게</p>
<p>가로축 제목 : 몸무게(kg)</p>
<p>구간 : 14</p>
<p>범위 : 30 ~ 100</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/total_checkup.csv')</p>
<p>data_mid = data[data['학년']=='중3']['몸무게']</p>

</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8544.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8544 = ''
question_review_8544 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>히스토그램
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>bins
<input type='checkbox'/>range
'''
answer_8544 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)","data = pd.read_csv('/content/jupyter_judge/csv_file/total_checkup.csv')",
                                  "data_mid = data[data['학년']=='중3']",
                                  "A_hist = plt.hist(data_mid['몸무게'],bins = 14, range = [30, 100])",
                                  "A_title = plt.title('중3학생의 몸무게')",
                                  "A_xlabel = plt.xlabel('몸무게(kg)')",
                                  "plt.show()"]

     }
]
question_8545 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>평균에 가까운 값은 많이 관찰 되고, 평균에서 멀어지는 값은 적게 관찰 되는 것을 경험상 알 수 있습니다.</p>
<p>예를 들어 키가 평균인 사람은 많지만, 키가 엄청 크거나 엄청 작은 사람은 매우 적습니다. 이는 정규분포로 나타낼 수 있습니다. <a href ="https://terms.naver.com/entry.naver?docId=3569149&cid=58944&categoryId=58970" target = 'blank'>정규 분포</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 교육부에서 제공한 <a href ="https://www.data.go.kr/data/15100360/fileData.do" target = 'blank'>학교건강검사 표본조사</a>입니다. 초1부터 고3까지 9만명의 건강 데이터로 구성되어 있습니다.</p>
<p>열 : 도시구분, 시도, 학교급, 학년, 성별, 키, 몸무게</p>
<p>문제에서는 전처리한 데이터를 제공합니다.</p>
<h2>그래프</h2>
<p>중3 학생의 키를 나타낸 히스토그램에 평균 키를 나타내봅시다.</p>
<p>그래프 제목 : 중3학생의 키</p>
<p>가로축 제목 : 키(cm)</p>
<p>히스토그램 구간 : 12</p>
<p>히스토그램 범위 : 130 ~ 190</p>
<p>수직선 x 위치 : 중3 학생 키의 평균</p>
<p>수직선 y 범위 : 0 ~ 2000</p>
<p>수직선 label : 평균 키</p>
<p>수직선 색 : red</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/total_checkup.csv')</p>
<p>data_mid = data[data['학년']=='중3']['키']</p>
<p>data_mid_mean = data_mid.mean()</p>

</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8545.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8545 = ''
question_review_8545 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>히스토그램
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>bins
<input type='checkbox'/>range
<input type='checkbox'/>수직선 범위
<input type='checkbox'/>수직선 색
<input type='checkbox'/>수직선 label
'''
answer_8545 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)","data = pd.read_csv('/content/jupyter_judge/csv_file/total_checkup.csv')",
                                  "data_mid = data[data['학년']=='중3']['키']",
                                  "data_mid_mean = data_mid.mean()",
                                  "A_hist = plt.hist(data_mid,bins = 12, range = [130, 190])",
                                  "A_vlines = plt.vlines(data_mid_mean, 0, 2000, color = 'red', label = '평균 키')",
                                  "A_title = plt.title('중3학생의 키')",
                                  "A_xlabel = plt.xlabel('키(cm)')",
                                  "A_legend = plt.legend()",
                                  "plt.show()"]

     }
]

question_8551 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>영영화를 관객수로만 평가하는 것이 아니라 상영횟수도 고려해야 한다는 신문기사입니다.</p>
<p>다음 뉴스를 보고 영화의 인기를 어떻게 평가하면 좋을지 생각해봅시다. <a href ="https://m.tf.co.kr/amp/entertain/1698743.htm" target = 'blank'>영화 관객수와 영화 상영횟수</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 영화관입장권통합전산망(KOBIS)에서 제공하는 <a href ="https://www.kobis.or.kr/kobis/business/stat/boxs/findFormerBoxOfficeList.do" target = 'blank'>역대 박스오피스</a>에서 1000만 관객을 돌파한 영화로 구성했습니다.</p>
<p>열 : rank(순위), movie(영화제목), sales(매출액), audiences(관객수), total_screen(상영 스크린수), total_showing(상영횟수), sales_per_showing(1회 상영당 매출액), audience_per_showing(1회 상영당 관객수)</p>
<p>기존 데이터에서 개봉일을 제거하고 1회 상영당 매출액, 1회 상영당 관객수를 추가했습니다.</p>
<h2>그래프</h2>
<p>1000만 관객을 넘은 영화를 대상으로 100만명을 단위로 한 히스토그램을 나타내봅시다.</p>
<p>그래프 제목 : 1000만 관객을 넘은 영화의 히스토그램</p>
<p>계급의 크기는 1000000</p>
<p>구간은 8(bins = 8), 범위는 10000000~18000000입니다.(range = (10000000, 18000000))</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/movie_audience.csv')</p>
<p>movie_audience = data['audiences']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8551.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8551 = ''
question_review_8551 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>히스토그램
<input type='checkbox'/>bins
<input type='checkbox'/>range
'''
answer_8551 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/movie_audience.csv')",
                                  "movie_audience = data['audiences']",
                                  "A_hist = plt.hist(movie_audience, bins = 8, range = (10000000, 18000000))",
                                  "A_title = plt.title('1000만 관객을 넘은 영화의 히스토그램')",
                                  "A_xlabel = plt.xlabel('관객수(명)')",
                                  "plt.show()"                                   ]}
]
question_8552 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>영화를 관객수로만 평가하는 것이 아니라 상영횟수도 고려해야 한다는 신문기사입니다.</p>
<p>다음 뉴스를 보고 영화의 인기를 어떻게 평가하면 좋을지 생각해봅시다. <a href ="https://m.tf.co.kr/amp/entertain/1698743.htm" target = 'blank'>영화 관객수와 영화 상영횟수</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 영화관입장권통합전산망(KOBIS)에서 제공하는 <a href ="https://www.kobis.or.kr/kobis/business/stat/boxs/findFormerBoxOfficeList.do" target = 'blank'>역대 박스오피스</a>에서 1000만 관객을 돌파한 영화로 구성했습니다.</p>
<p>열 : rank(순위), movie(영화제목), sales(매출액), audiences(관객수), total_screen(상영 스크린수), total_showing(상영횟수), sales_per_showing(1회 상영당 매출액), audience_per_showing(1회 상영당 관객수)</p>
<p>기존 데이터에서 개봉일을 제거하고 1회 상영당 매출액, 1회 상영당 관객수를 추가했습니다.</p>
<h2>그래프</h2>
<p>1000만 관객을 넘은 영화 중 1회 상영당 관객수가 상위 15개의 영화에 대해서 1회 상영당 관객수를 세로 막대그래프로 나타내봅시다.</p>
<p>그래프 제목 : 1000만 관객 넘은 영화 중 1회 상영당 관객</p>
<p>가로축 이름 : 1회 상영당 관객수</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/movie_audience.csv')</p>
<p>data = data.sort_values('audience_per_showing', ascending = False)[:15]</p>
<p>audience_per_showing = data['audience_per_showing']</p>
<p>movie = data['movie']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8552.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8552 = ''
question_review_8552 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>세로 막대그래프
<input type='checkbox'/>title
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8552 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/movie_audience.csv')",
                                  "data = data.sort_values('audience_per_showing', ascending = False)[:15]",
                                  "audience_per_showing = data['audience_per_showing']",
                                  "movie = data['movie']",
                                  "A_barh = plt.barh(movie, audience_per_showing)",
                                  "A_title = plt.title('1000만 관객 넘은 영화 중 1회 상영당 관객')",
                                  "A_xlabel = plt.xlabel('1회 상영당 관객수')",
                                  "plt.show()"                                   ]}
]
question_8561 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>지하철 역중에서 사고가 많이 나는 역과 사고 유형을 조사한 신문기사 입니다.</p>
<p>이용객이 많은 역 중 하나인 사당역에서 언제 사고가 많이 발생할지 생각해봅시다. <a href ="https://biz.sbs.co.kr/article/20000136368" target = 'blank'>출퇴근길에 특히 조심해야 할 역은?</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 서울교통공사가 제공하는 <a href ="https://www.data.go.kr/data/15071311/fileData.do" target = 'blank'>요일별, 시간대별, 지하철 역별 혼잡도</a>에서 요일별 사당역 데이터로 구성했습니다.</p>
<p>서울교통공사 1-8호선 30분 단위 평균 혼잡도로 30분간 지나는 열차들의 평균 혼잡도(정원대비 승차인원으로, 승차인과 좌석수가 일치할 경우를 혼잡도 34%로 산정) 입니다.(단위: %)</p>
<p>열 : weekday_inner(평일 내선), weekday_outer(평일 외선), sat_inner(토요일 내선), sat_outer(토요일 외선), holiday_inner(공휴일 내선), holiday_outer(공휴일 외선)</p>
<h2>그래프</h2>
<p>평일 사당역 내선의 혼잡도를 히스토그램과 혼잡도의 평균을 수직선으로 나타내봅시다.</p>
<p>그래프 제목 : 평일 사당역 내선의 혼잡도 히스토그램 </p>
<p>가로축 이름 : 혼잡도(%)</p>
<p>세로축 이름 : 도수</p>
<p>수직선 x좌표 : 혼잡도의 평균</p>
<p>수직선의 y좌표 범위 : 0~12
<p>수직선의 label : 평균
<p>수직선의 색 : 빨간색</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/subway_congestion.csv')</p>
<p>weekday_inner= data['weekday_inner']</p>
<p>weekday_inner_mean = weekday_inner.mean()
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8561.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8561 = ''
question_review_8561 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>히스토그램
<input type='checkbox'/>vlines
<input type='checkbox'/>vlines 범위
<input type='checkbox'/>가로축 이름
<input type='checkbox'/>세로축 이름
<input type='checkbox'/>label과 legend
'''
answer_8561 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/subway_congestion.csv')", 
                                  "weekday_inner= data['weekday_inner']", 
                                  "weekday_inner_mean = weekday_inner.mean()", 
                                  "A_hist = plt.hist(weekday_inner)",
                                  "A_vlines = plt.vlines(weekday_inner_mean, 0, 12, color = 'red', label = '평균')",
                                  "A_xlabel = plt.xlabel('혼잡도(%)')",
                                  "A_title = plt.title('평일 사당역 내선의 혼잡도 히스토그램')",
                                  "A_legend = plt.legend()",
                                  "plt.show()"                                   ]}
]
question_8562 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>지하철 역중에서 사고가 많이 나는 역과 사고 유형을 조사한 신문기사 입니다.</p>
<p>이용객이 많은 역 중 하나인 사당역에서 언제 사고가 많이 발생할지 생각해봅시다. <a href ="https://biz.sbs.co.kr/article/20000136368" target = 'blank'>출퇴근길에 특히 조심해야 할 역은?</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 서울교통공사가 제공하는 <a href ="https://www.data.go.kr/data/15071311/fileData.do" target = 'blank'>요일별, 시간대별, 지하철 역별 혼잡도</a>에서 요일별 사당역 데이터로 구성했습니다.</p>
<p>서울교통공사 1-8호선 30분 단위 평균 혼잡도로 30분간 지나는 열차들의 평균 혼잡도(정원대비 승차인원으로, 승차인과 좌석수가 일치할 경우를 혼잡도 34%로 산정) 입니다.(단위: %)</p>
<p>열 : weekday_inner(평일 내선), weekday_outer(평일 외선), sat_inner(토요일 내선), sat_outer(토요일 외선), holiday_inner(공휴일 내선), holiday_outer(공휴일 외선)</p>
<h2>그래프</h2>
<p>평일 사당역 내선과 외선의 상자그림을 나타내봅시다.</p>
<p>그래프 제목 : 평일 사당역 내선, 외선 상자그림 </p>
<p>가로축 이름 : 내선, 외선</p>
<p>세로축 이름 : 혼잡도(%)</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/subway_congestion.csv')</p>
<p>weekday_inner = data['weekday_inner']</p>
<p>weekday_outer = data['weekday_outer']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8562.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8562 = ''
question_review_8562 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>내선과 외선의 boxplot
'''
answer_8562 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                   "data = pd.read_csv('/content/jupyter_judge/csv_file/subway_congestion.csv')", 
                                  "weekday_inner = data['weekday_inner']",
                                  "weekday_outer = data['weekday_outer']", 
                                  "A_boxplot = plt.boxplot([weekday_inner, weekday_outer], labels = ['내선', '외선'])", 
                                  "A_title = plt.title('평일 사당역 내선, 외선 상자그림')", 
                                  "A_ylabel = plt.ylabel('혼잡도(%)')", 
                                  "plt.show()"]}
]
question_8563 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>지하철 역중에서 사고가 많이 나는 역과 사고 유형을 조사한 신문기사 입니다.</p>
<p>이용객이 많은 역 중 하나인 사당역에서 언제 사고가 많이 발생할지 생각해봅시다. <a href ="https://biz.sbs.co.kr/article/20000136368" target = 'blank'>출퇴근길에 특히 조심해야 할 역은?</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 서울교통공사가 제공하는 <a href ="https://www.data.go.kr/data/15071311/fileData.do" target = 'blank'>요일별, 시간대별, 지하철 역별 혼잡도</a>에서 요일별 사당역 데이터로 구성했습니다.</p>
<p>서울교통공사 1-8호선 30분 단위 평균 혼잡도로 30분간 지나는 열차들의 평균 혼잡도(정원대비 승차인원으로, 승차인과 좌석수가 일치할 경우를 혼잡도 34%로 산정) 입니다.(단위: %)</p>
<p>열 : weekday_inner(평일 내선), weekday_outer(평일 외선), sat_inner(토요일 내선), sat_outer(토요일 외선), holiday_inner(공휴일 내선), holiday_outer(공휴일 외선)</p>
<h2>그래프</h2>
<p>평일 사당역 내선의 시간대별 혼잡도 세로 막대그래프를 나타내봅시다.</p>
<p>그래프 제목 : 시간대별 내선 혼잡도</p>
<p>가로축 제목 : 혼잡도(%)</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/subway_congestion.csv')</p>
<p>weekday_inner = data['weekday_inner']</p>
<p>subway_time = data['time']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8563.png?raw=true" width = 150% height = 150%>
</div>
'''

img_8563 = ''
question_review_8563 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>막대그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8563 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/subway_congestion.csv')", 
                                  "weekday_inner = data['weekday_inner']", 
                                  "subway_time = data['time']", 
                                  "A_barh = plt.barh(subway_time, weekday_inner)", 
                                  "A_title = plt.title('시간대별 내선 혼잡도')", 
                                  "A_xlabel = plt.xlabel('혼잡도(%)')", 
                                  "plt.show()"                                   ]}
]
question_8564 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>지하철 역중에서 사고가 많이 나는 역과 사고 유형을 조사한 신문기사 입니다.</p>
<p>이용객이 많은 역 중 하나인 사당역에서 언제 사고가 많이 발생할지 생각해봅시다. <a href ="https://biz.sbs.co.kr/article/20000136368" target = 'blank'>출퇴근길에 특히 조심해야 할 역은?</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 서울교통공사가 제공하는 <a href ="https://www.data.go.kr/data/15071311/fileData.do" target = 'blank'>요일별, 시간대별, 지하철 역별 혼잡도</a>에서 요일별 사당역 데이터로 구성했습니다.</p>
<p>서울교통공사 1-8호선 30분 단위 평균 혼잡도로 30분간 지나는 열차들의 평균 혼잡도(정원대비 승차인원으로, 승차인과 좌석수가 일치할 경우를 혼잡도 34%로 산정) 입니다.(단위: %)</p>
<p>열 : weekday_inner(평일 내선), weekday_outer(평일 외선), sat_inner(토요일 내선), sat_outer(토요일 외선), holiday_inner(공휴일 내선), holiday_outer(공휴일 외선)</p>
<h2>그래프</h2>
<p>평일 사당역 외선의 시간대별 혼잡도 세로 막대그래프를 나타내봅시다.</p>
<p>그래프 제목 : 평일 시간대별 외선 혼잡도</p>
<p>가로축 제목 : 혼잡도(%)</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/subway_congestion.csv')</p>
<p>weekday_inner = data['weekday_outer']</p>
<p>subway_time = data['time']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8564.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8564 = ''
question_review_8564 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>막대그래프
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8564 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/subway_congestion.csv')", 
                                  "weekday_outer = data['weekday_outer']", 
                                  "subway_time = data['time']", 
                                  "A_barh = plt.barh(subway_time, weekday_outer)", 
                                  "A_xlabel = plt.xlabel('혼잡도(%)')", 
                                  "A_title = plt.title('평일 시간대별 외선 혼잡도')", 
                                  "plt.show()"                                   ]}
]
question_8571 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>다음은 따릉이 대여건수에 영향을 주는 것을 조사한 신문기사 입니다.</p>
<p>따릉이 대여건수에 영향을 주는 것은 무엇일지 생각해봅시다. <a href ="https://www.newspim.com/news/view/20221114000868" target = 'blank'>따릉이 대여와 관련있는 것은?</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 서울특별시에서 제공하는 <a href ="https://www.data.go.kr/data/15051873/fileData.do" target = 'blank'>따릉이 대여건수</a>와 기상청에서 제공하는 <a href ="https://data.kma.go.kr/cmmn/main.do" target = 'blank'>서울특별시 기상정보(온도, 습도, 미세먼지)</a>로 구성했습니다.</p>
<p>열 : day(일), rent(대여건수), humidity(습도), temperature(온도), dust(미세먼지)</p>
<p>문제에서 제공하는 데이터는 공공데이터를 정리하여 2022년 1월부터 12월까지 서울시 공공자전거 대여건수와 습도, 기온, 미세먼지 농도로 재구성</p>
<h2>그래프</h2>
<p>일별 대여건수를 상자그림으로 나타내봅시다</p>
<p>그래프 제목 : 서울시 공공자전거 대여건수 상자그림 </p>
<p>가로축 이름 : 대여</p>
<p>세로축 이름 : 대여건수(건)</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')</p>
<p>rent = data['rent']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8571.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8571 = ''
question_review_8571 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>boxplot
<input type='checkbox'/>title
<input type='checkbox'/>ylabel
'''
answer_8571 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')", 
                                  "rent = data['rent']", 
                                  "rent_mean = data['rent'].mean()", 
                                  "plt.boxplot(rent, labels = ['대여건수'])", 
                                  "A_title = plt.title('서울시 공공자전거 대여건수 상자그림')", 
                                  "A_ylabel = plt.ylabel('대여건수(건)')", 
                                  "plt.show()"                                   ]}
]
question_8572 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>다음은 따릉이 대여건수에 영향을 주는 것을 조사한 신문기사 입니다.</p>
<p>따릉이 대여건수에 영향을 주는 것은 무엇일지 생각해봅시다. <a href ="https://www.newspim.com/news/view/20221114000868" target = 'blank'>따릉이 대여와 관련있는 것은?</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 서울특별시에서 제공하는 <a href ="https://www.data.go.kr/data/15051873/fileData.do" target = 'blank'>따릉이 대여건수</a>와 기상청에서 제공하는 <a href ="https://data.kma.go.kr/cmmn/main.do" target = 'blank'>서울특별시 기상정보(온도, 습도, 미세먼지)</a>로 구성했습니다.</p>
<p>열 : day(일), rent(대여건수), humidity(습도), temperature(온도), dust(미세먼지)</p>
<p>문제에서 제공하는 데이터는 공공데이터를 정리하여 2022년 1월부터 12월까지 서울시 공공자전거 대여건수와 습도, 기온, 미세먼지 농도로 재구성</p>
<h2>그래프</h2>
<p>서울시 공공자전거 대여건수를 히스토그램으로 나타내고 평균을 수직선으로 나타내봅시다.</p>
<p>그래프 제목 : 서울시 공공자전거 대여건수 히스토그램 </p>
<p>세로축 이름 : 도수</p>
<p>수직선 범위 : 0 ~ 60</p>
<p>수직선 색 : 빨강</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')</p>
<p>rent = data['rent']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8572.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8572 = ''
question_review_8572 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>히스토그램
<input type='checkbox'/>title
<input type='checkbox'/>ylabel
'''
answer_8572 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')", 
                                  "rent = data['rent']", 
                                  "rent_mean = data['rent'].mean()",
                                  "A_hist = plt.hist(rent)",
                                  "A_title = plt.title('서울시 공공자전거 대여건수 히스토그램')", 
                                  "A_ylabel = plt.ylabel('도수')", 
                                  "A_xlabel = plt.xlabel('대여건수')", 
                                  "A_vlines = plt.vlines(rent_mean, 0, 60, color = 'red', label = '평균')", 
                                  "A_legend = plt.legend()", 
                                  "plt.show()"                                   ]}
]
question_8573 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>다음은 따릉이 대여건수에 영향을 주는 것을 조사한 신문기사 입니다.</p>
<p>따릉이 대여건수에 영향을 주는 것은 무엇일지 생각해봅시다. <a href ="https://www.newspim.com/news/view/20221114000868" target = 'blank'>따릉이 대여와 관련있는 것은?</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 서울특별시에서 제공하는 <a href ="https://www.data.go.kr/data/15051873/fileData.do" target = 'blank'>따릉이 대여건수</a>와 기상청에서 제공하는 <a href ="https://data.kma.go.kr/cmmn/main.do" target = 'blank'>서울특별시 기상정보(온도, 습도, 미세먼지)</a>로 구성했습니다.</p>
<p>열 : day(일), rent(대여건수), humidity(습도), temperature(온도), dust(미세먼지)</p>
<p>문제에서 제공하는 데이터는 공공데이터를 정리하여 2022년 1월부터 12월까지 서울시 공공자전거 대여건수와 습도, 기온, 미세먼지 농도로 재구성</p>
<h2>그래프</h2>
<p>일별 대여건수와 온도의 산점도를 나타내봅시다.</p>

<p>그래프 제목 : 대여건수와 온도의 관계  </p>
<p>가로축 이름 : 대여건수</p>
<p>세로축 이름 : 온도</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')</p>
<p>rent = data['rent']</p>
<p>temperature = data['temperature']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8573.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8573 = ''
question_review_8573 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>산점도
<input type='checkbox'/>회귀선
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8573 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')", 
                                  "rent = data['rent']", 
                                  "temperature = data['temperature']", 
                                  "A_scatter = plt.scatter(rent, temperature)", 
                                  "A_title = plt.title('대여건수와 온도의 관계')", 
                                  "A_xlabel = plt.xlabel('대여건수')", 
                                  "A_ylabel = plt.ylabel('온도')", 
                                  "plt.show()"                                   ]}
]
question_8574 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>다음은 따릉이 대여건수에 영향을 주는 것을 조사한 신문기사 입니다.</p>
<p>따릉이 대여건수에 영향을 주는 것은 무엇일지 생각해봅시다. <a href ="https://www.newspim.com/news/view/20221114000868" target = 'blank'>따릉이 대여와 관련있는 것은?</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 서울특별시에서 제공하는 <a href ="https://www.data.go.kr/data/15051873/fileData.do" target = 'blank'>따릉이 대여건수</a>와 기상청에서 제공하는 <a href ="https://data.kma.go.kr/cmmn/main.do" target = 'blank'>서울특별시 기상정보(온도, 습도, 미세먼지)</a>로 구성했습니다.</p>
<p>열 : day(일), rent(대여건수), humidity(습도), temperature(온도), dust(미세먼지)</p>
<p>문제에서 제공하는 데이터는 공공데이터를 정리하여 2022년 1월부터 12월까지 서울시 공공자전거 대여건수와 습도, 기온, 미세먼지 농도로 재구성</p>
<h2>그래프</h2>
<p>일별 대여건수와 미세먼지의 산점도를 나타내봅시다.</p>
<p>그래프 제목 : 대여건수와 미세먼지 농도와의 관계  </p>
<p>가로축 이름 : 대여건수</p>
<p>세로축 이름 : 미세먼지 농도</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')</p>
<p>rent = data['rent']</p>
<p>dust = data['dust']</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8574.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8574= ''
question_review_8574 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>산점도
<input type='checkbox'/>회귀선
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8574 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')", 
                                  "rent = data['rent']", 
                                  "dust = data['dust']", 
                                  "A_scatter = plt.scatter(rent, dust)", 
                                  "A_title = plt.title('대여건수와 미세먼지 농도와의 관계')", 
                                  "A_xlabel = plt.xlabel('대여건수')", 
                                  "A_ylabel = plt.ylabel('미세먼지 농도')", 
                                  "plt.show()"]}
]
question_8581 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>청년층은 도시로 이동하고 시골은 고령화가 심화되는 문제를 제시한 신문기사입니다.</p>
<p>도시가 고령화되면 어떤 특징이 있을지 생각해봅시다. <a href ="https://www.ajunews.com/view/20201117125912110" target = 'blank'>고령 인구 늘어나는 시골</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 국민연금공단에서 제공하는 <a href ="https://www.data.go.kr/data/3046077/fileData.do" target = 'blank'>지역가입자 평균소득월액</a>과 행정안전부에서 제공하는 <a href ="https://www.data.go.kr/data/15099158/fileData.do" target = 'blank'>지역별 성별 연령별 주민등록 인구수</a>에서 지역별 평균소득월액과 유소년인구, 생산가능인구, 고령인구로 구성했습니다.</p>
<p>열 : city_province(시도), district(시군구), income(평균소득), total_population(총 인구), youth_population(유소년 인구), production_population(생산가능 인구), old_population(고령 인구), youth_percentage(유소년 인구 비율), production_percentage(생산가능 인구 비율), old_percentage(고령 인구 비율)</p>
<p>국민연금 지역가입자의 평균소득월액과 지역별 인구 및 백분율을 합쳐 재구성하였다.</p>
<h2>그래프</h2>
<p>평균소득월액을 히스토그램으로 나타내고, 평균소득월액의 평균에 해당하는 부분에 수직선을 그려봅시다.</p>
<p>그래프 제목 : 지역별 평균소득월액 히스토그램 </p>
<p>가로축 이름 : 평균소득월액</p>
<p>세로축 이름 : 도수</p>
<p>수직선 x좌표 : 평균소득월액</p>
<p>수직선의 y좌표 범위 : 0~50</p>
<p>수직선의 색 : 빨간색</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/income_and_population.csv')</p>
<p>income = data['income']</p>
<p>income_mean = income.mean()</p>
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8581.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8581= ''
question_review_8581 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>히스토그램
<input type='checkbox'/>vlines
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8581 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)",
                                   "data = pd.read_csv('/content/jupyter_judge/csv_file/income_and_population.csv')", 
                                  "income = data['income']", 
                                  "income_mean = income.mean()",
                                  "A_hist = plt.hist(income)",
                                  "A_vlines = plt.vlines(income_mean, 0, 60, color = 'red', label = '평균')", 
                                  "A_legend = plt.legend()", 
                                  "A_title = plt.title('지역별 평균소득월액 히스토그램')", 
                                  "A_xlabel = plt.xlabel('소득월액')", 
                                  "A_ylabel = plt.ylabel('도수')", 
                                  "plt.show()"]}
]
question_8582 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>청년층은 도시로 이동하고 시골은 고령화가 심화되는 문제를 제시한 신문기사입니다.</p>
<p>도시가 고령화되면 어떤 특징이 있을지 생각해봅시다. <a href ="https://www.ajunews.com/view/20201117125912110" target = 'blank'>고령 인구 늘어나는 시골</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 국민연금공단에서 제공하는 <a href ="https://www.data.go.kr/data/3046077/fileData.do" target = 'blank'>지역가입자 평균소득월액</a>과 행정안전부에서 제공하는 <a href ="https://www.data.go.kr/data/15099158/fileData.do" target = 'blank'>지역별 성별 연령별 주민등록 인구수</a>에서 지역별 평균소득월액과 유소년인구, 생산가능인구, 고령인구로 구성했습니다.</p>
<p>열 : city_province(시도), district(시군구), income(평균소득), total_population(총 인구), youth_population(유소년 인구), production_population(생산가능 인구), old_population(고령 인구), youth_percentage(유소년 인구 비율), production_percentage(생산가능 인구 비율), old_percentage(고령 인구 비율)</p>
<p>국민연금 지역가입자의 평균소득월액과 지역별 인구 및 백분율을 합쳐 재구성하였다.</p>
<h2>그래프</h2>
<p>평균소득월액과 생산가능인구 백분율의 산점도를 나타내봅시다.</p>
<p>그래프 제목 : 지역별 평균소득월액과 생산가능 인구 관계 </p>
<p>가로축 이름 : 평균소득월액</p>
<p>세로축 이름 : 생산가능인구 백분율(%)</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/income_and_population.csv')</p>
<p>income = data['income']</p>
<p>production_percentage = data['production_percentage']
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8582.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8582= ''
question_review_8582 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>산점도
<input type='checkbox'/>회귀선
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8582 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/income_and_population.csv')",
                                  "income = data['income']",
                                  "production_percentage = data['production_percentage']",
                                  "A_scatter = plt.scatter(income, production_percentage)",
                                  "A_title = plt.title('지역별 평균소득월액과 생산가능 인구 관계')",
                                  "A_xlabel = plt.xlabel('평균소득월액')",
                                  "A_ylabel = plt.ylabel('생산가능인구 백분율(%)')",
                                  "plt.show()"                                   ]}
]
question_8583 = '''<h1 style = "background-color:yellow; ">문제 설명</h1>
<h2>관련 뉴스</h2>
<p>청년층은 도시로 이동하고 시골은 고령화가 심화되는 문제를 제시한 신문기사입니다.</p>
<p>도시가 고령화되면 어떤 특징이 있을지 생각해봅시다. <a href ="https://www.ajunews.com/view/20201117125912110" target = 'blank'>고령 인구 늘어나는 시골</a></p>
<hr>
<h2>데이터</h2>
<p>문제에서 제공하는 데이터는 국민연금공단에서 제공하는 <a href ="https://www.data.go.kr/data/3046077/fileData.do" target = 'blank'>지역가입자 평균소득월액</a>과 행정안전부에서 제공하는 <a href ="https://www.data.go.kr/data/15099158/fileData.do" target = 'blank'>지역별 성별 연령별 주민등록 인구수</a>에서 지역별 평균소득월액과 유소년인구, 생산가능인구, 고령인구로 구성했습니다.</p>
<p>열 : city_province(시도), district(시군구), income(평균소득), total_population(총 인구), youth_population(유소년 인구), production_population(생산가능 인구), old_population(고령 인구), youth_percentage(유소년 인구 비율), production_percentage(생산가능 인구 비율), old_percentage(고령 인구 비율)</p>
<p>국민연금 지역가입자의 평균소득월액과 지역별 인구 및 백분율을 합쳐 재구성하였다.</p>
<h2>그래프</h2>
<p>평균소득월액과 노령인구 백분율의 산점도를 나타내봅시다.</p>
<p>그래프 제목 : 지역별 평균소득월액과 노령인구 관계 </p>
<p>가로축 이름 : 평균소득월액</p>
<p>세로축 이름 : 노령인구 백분율(%)</p>
<HR>
<div style = "float:left;width:50%">
<h2>데이터 예시 </h2>
<p>data = pd.read_csv('/content/jupyter_judge/csv_file/income_and_population.csv')</p>
<p>income = data['income']</p>
<p>old_percentage = data['old_percentage']
</div>
<div style = "float:right;width:50%">
<h2>그래프 예시 </h2>
<img src="https://github.com/GoHakNeung/jupyter_judge/blob/main/graph/answer_8583.png?raw=true" width = 150% height = 150%>
</div>
'''
img_8583= ''
question_review_8583 = '''
<h3> 아래 요소들이 그래프에 반영되었는지 확인해봅시다.</h3>
<input type='checkbox'/>산점도
<input type='checkbox'/>회귀선
<input type='checkbox'/>제목
<input type='checkbox'/>xlabel
<input type='checkbox'/>ylabel
'''
answer_8583 = [
    {'input' : [[10]], 'output' : ["plt.subplot(1,2,2)", 
                                  "data = pd.read_csv('/content/jupyter_judge/csv_file/income_and_population.csv')",
                                  "income = data['income']",
                                  "old_percentage = data['old_percentage']", 
                                  "A_scatter = plt.scatter(income, old_percentage)", 
                                  "A_title = plt.title('지역별 평균소득월액과 노령인구 관계')", 
                                  "A_xlabel = plt.xlabel('평균소득월액')", 
                                  "A_ylabel = plt.ylabel('노령인구 백분율(%)')", 
                                  "plt.show()"                                   ]}
]


### DPAA 문제
##8601 데이터 프레임 만들기
table_8601 = pd.DataFrame({'Apples' : [30, 34, 21,22,54, 23, 43], 'Bananas' : [21, 12, 43, 23, 33, 56,23]})
table_html_8601 = table_8601.to_html(max_rows = 10, max_cols = 10)
question_8601 =f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<p>DataFrame을 만들어서 df 변수에 입력해봅시다. </p>
<p>Apples 열 : 30, 34, 21, 22, 54, 23, 43 | Bananas 열 : 21, 12, 43, 23, 33, 56, 23</p>
<HR>
<div style = "float:left;width:50%">
<h2> 예시 </h2>
<p>{table_html_8601}<p>
</div>
'''
#정답데이터
answer_8601 = [
    {'input' : [[10]], 'output' : ["df_answer = pd.DataFrame({'Apples' : [30, 34, 21,22,54, 23, 43], 'Bananas' : [21, 12, 43, 23, 33, 56,23]})"
                                  ]}
]
#이미지
img_8601 =''

##8602 외부데이터 불러와서 데이터 프레임 만들기
table_8602 = pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')
table_html_8602 = table_8602.to_html(max_rows = 10, max_cols = 10)
question_8602 =f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<p>csv_file 폴더에 있는 checkup.csv 파일을 df 변수에 입력해봅시다.</p>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/checkup.csv")</h3>
<HR>
<div style = "float:left;width:50%">
<h2> 예시 </h2>
<p>{table_html_8602}<p>
</div>
'''
#정답데이터
answer_8602 = [
    {'input' : [[10]], 'output' : ["df_answer = pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')"]}
]
#이미지
img_8602 =''

##8603 문제
table_8603 = pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")
table_html_8603 = table_8603.to_html(max_rows = 10, max_cols = 10)
pre_table_8603 = table_8603.head()
pre_table_html_8603 = pre_table_8603.to_html(max_rows = 10, max_cols = 10)
question_8603 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")</h3>
<p>csv_file 폴더에 있는 bike_seoul.csv 파일을 Dataframe으로 불러와서 head() 값을 df 변수에 입력해봅시다.</p>

<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8603}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8603}
</div>
'''
answer_8603 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')",
                              "df_answer = data.head()"]}
]
img_8603 =''

##8604문제
table_8604 = pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")
table_html_8604 = table_8604.to_html(max_rows = 10, max_cols = 10)
pre_table_8604 = table_8604.tail()
pre_table_html_8604 = pre_table_8604.to_html(max_rows = 10, max_cols = 10)
question_8604 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")</h3>
<p>csv_file 폴더에 있는 bike_seoul.csv 파일을 Dataframe으로 불러와서 tail() 값을 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8604}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8604}
</div>
'''
#모범답안
answer_8604 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')",
                              "df_answer = data.tail()"]}
]
#이미지 힌트
img_8604 =''

##8605 문제
table_8605 = pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")
table_html_8605 = table_8605.to_html(max_rows = 10, max_cols = 10)
pre_table_8605 = table_8605.describe()
pre_table_html_8605 = pre_table_8605.to_html(max_rows = 10, max_cols = 10)
question_8605 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")</h3>
<p>csv_file 폴더에 있는 bike_seoul.csv 파일을 Dataframe으로 불러와서 describe()한 결과를 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8605}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8605}
</div>
'''
#모범답안
answer_8605 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')",
                              "df_answer = data.describe()"]}
]
img_8605 =''

##8606 문제
table_8606 = pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")
table_html_8606 = table_8606.to_html(max_rows = 10, max_cols = 10)
pre_table_8606 = table_8606.sort_values(by = 'rent', ascending = False)
pre_table_html_8606 = pre_table_8606.to_html(max_rows = 10, max_cols = 10)
question_8606 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")</h3>
<p>csv_file 폴더에 있는 bike_seoul.csv 파일을 Dataframe으로 불러와서 'rent'열을 내림차순으로 정렬한 결과를 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8606}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8606}
</div>
'''
#모범답안
answer_8606 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')",
                              "df_answer = data.sort_values(by = 'rent', ascending = False)"]}
]
img_8606 =''

##8607 문제
table_8607 = pd.read_csv("/content/jupyter_judge/csv_file/total_checkup.csv")
table_html_8607 = table_8607.to_html(max_rows = 10, max_cols = 10)
pre_table_8607 = table_8607.groupby('학년')[['키', '몸무게']].min()
pre_table_html_8607 = pre_table_8607.to_html(max_rows = 10, max_cols = 10)
question_8607 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/total_checkup.csv")</h3>
<p>csv_file 폴더에 있는 total_check.csv 파일을 Dataframe으로 불러와서 '학년'열을 groupby 합니다.</p>
<p>'키'와 '몸무게'의 열의 최소값을 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8607}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8607}
</div>
'''
#모범답안
answer_8607 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/total_checkup.csv')",
                              "df_answer = data.groupby('학년')[['키', '몸무게']].min()"]}
]
img_8607 =''

##8608 문제
table_8608 = pd.read_csv("/content/jupyter_judge/csv_file/total_checkup.csv")
table_html_8608 = table_8608.to_html(max_rows = 10, max_cols = 10)
pre_table_8608 = table_8608.groupby('학년')[['키', '몸무게']].max()
pre_table_html_8608 = pre_table_8608.to_html(max_rows = 10, max_cols = 10)
question_8608 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/total_checkup.csv")</h3>
<p>csv_file 폴더에 있는 total_check.csv 파일을 Dataframe으로 불러와서 '학년'열을 groupby 합니다.</p>
<p>'키'와 '몸무게'의 열의 최대대값을 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8608}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8608}
</div>
'''
#모범답안
answer_8608 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/total_checkup.csv')",
                              "df_answer = data.groupby('학년')[['키', '몸무게']].max()"]}
]
img_8608 =''

##8609 문제
table_8609 = pd.read_csv("/content/jupyter_judge/csv_file/total_checkup.csv")
table_html_8609 = table_8609.to_html(max_rows = 10, max_cols = 10)
pre_table_8609 = table_8609.groupby('시도')[['키', '몸무게']].mean()
pre_table_html_8609 = pre_table_8609.to_html(max_rows = 10, max_cols = 10)
question_8609 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/total_checkup.csv")</h3>
<p>csv_file 폴더에 있는 total_check.csv 파일을 Dataframe으로 불러와서 '시도'열을 groupby 합니다.</p>
<p>'키'와 '몸무게'의 열의 평값을 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8609}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8609}
</div>
'''
#모범답안
answer_8609 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/total_checkup.csv')",
                              "df_answer = data.groupby('시도')[['키', '몸무게']].mean()"]}
]
img_8609 =''

##8610 문제
table_8610 = pd.read_csv("/content/jupyter_judge/csv_file/movie_audience.csv")
table_html_8610 = table_8610.to_html(max_rows = 10, max_cols = 5)
pre_table_8610 = table_8610.loc[:,['movie', 'audiences']]
pre_table_html_8610 = pre_table_8610.to_html(max_rows = 10, max_cols = 5)
question_8610 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/movie_audience.csv")</h3>
<p>csv_file 폴더에 있는 movie_audience.csv 파일을 Dataframe으로 불러옵니다.</p>
<p>'movie'와 'audiences'의 열을 df 변수에에 입력해봅시다.</p>
<p>Let's save only 'movie' and 'audience' in the movie_audience.csv file in df.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8610}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8610}
</div>
'''
answer_8610 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/movie_audience.csv')",
                              "df_answer = data.loc[:,['movie', 'audiences']]"]}
]
img_8610 =''

##8611 문제
table_8611 = pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")
table_html_8611 = table_8611.to_html(max_rows = 10, max_cols = 10)
pre_table_8611 = table_8611.iloc[:,1:]
pre_table_html_8611 = pre_table_8611.to_html(max_rows = 10, max_cols = 10)
question_8611 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")</h3>
<p>csv_file 폴더에 있는 bike_seoul.csv 파일을 Dataframe으로 불러옵니다.</p>
<p>'day'의 열을 제외하고 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8611}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8611}
</div>
'''
answer_8611 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')",
                              "df_answer = data.iloc[:,1:]"]}
]
img_8611 =''

##8612문제
table_8612 = pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")
table_html_8612 = table_8612.to_html(max_rows = 10, max_cols = 10)
table_8612 = table_8612.iloc[:,1:]
pre_table_8612 = (table_8612-table_8612.min()) / (table_8612.max() - table_8612.min())
pre_table_html_8612 = pre_table_8612.to_html(max_rows = 10, max_cols = 10)
question_8612 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")</h3>
<p>csv_file 폴더에 있는 bike_seoul.csv 파일을 Dataframe으로 불러옵니다.</p>
<p>'day'의 열을 제외합니다. </p>
<p>각각의 값을 0 ~ 1 사이 값으로 변환하여 df 변수에 입력해봅시다.</p>
<p>참고 (value - min) / (max - min)</p>

<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8612}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8612}
</div>
'''
answer_8612 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')",
                               "data = data.iloc[:,1:]",
                              "df_answer = (data-data.min()) / (data.max() - data.min())"]}
]
img_8612 =''

##8613 문제
table_8613 = pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")
table_html_8613 = table_8613.to_html(max_rows = 10, max_cols = 10)
table_8613 = table_8613.iloc[:,1:]
pre_table_8613 = (table_8613-table_8613.mean()) / (table_8613.std())
pre_table_html_8613 = pre_table_8613.to_html(max_rows = 10, max_cols = 10)
question_8613 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")</h3>
<p>csv_file 폴더에 있는 bike_seoul.csv 파일을 Dataframe으로 불러옵니다.</p>
<p>'day'의 열을 제외합니다. </p>
<p>각각의 값을 정규화하여 df 변수에 입력해봅시다.</p>
<p>참고 (value -mean) / (std)</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8613}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8613}
</div>
'''
answer_8613 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')",
                               "data = data.iloc[:,1:]",
                               "df_answer = (data-data.mean()) / (data.std())"]}
]
img_8613 =''

##8614 문제
table_8614 = pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")
table_html_8614 = table_8614.to_html(max_rows = 10, max_cols = 10)
pre_table_8614 = table_8614[table_8614['rent']>180000]
pre_table_html_8614 = pre_table_8614.to_html(max_rows = 10, max_cols = 10)
question_8614 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul.csv")</h3>
<p>csv_file 폴더에 있는 bike_seoul.csv 파일을 Dataframe으로 불러옵니다.</p>
<p>'rent'열에 값이 180000 초과인 값만 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8614}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8614}
</div>
'''
answer_8614 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul.csv')",
                              "df_answer = data[data['rent']>180000]"]}
]
img_8614 =''

##8615 문제
table_8615 = pd.read_csv("/content/jupyter_judge/csv_file/checkup.csv")
table_html_8615 = table_8615.to_html(max_rows = 10, max_cols = 10)
pre_table_8615 = table_8615[table_8615['성별']=='남']
pre_table_html_8615 = pre_table_8615.to_html(max_rows = 10, max_cols = 10)
question_8615 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/checkup.csv")</h3>
<p>csv_file 폴더에 있는 checkup.csv 파일을 Dataframe으로 불러옵니다.</p>
<p>'성별'열에 값이 '남'인 값만 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8615}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8615}
</div>
'''
answer_8615 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/checkup.csv')",
                              "df_answer = data[data['성별']=='남']"]}
]
img_8615 =''  

##8616 문제
table_8616 = pd.read_csv("/content/jupyter_judge/csv_file/missing_data.csv")
table_html_8616 = table_8616.to_html(max_rows = 10, max_cols = 10)
pre_table_8616 = table_8616.fillna(value = table_8616['D'].mean())
pre_table_html_8616 = pre_table_8616.to_html(max_rows = 10, max_cols = 10)
question_8616 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/missing_data.csv")</h3>
<p>csv_file 폴더에 있는 missing_data.csv 파일을 Dataframe으로 불러옵니다.</p>
<p>NaN인 대신에 'D'열의 평균을 채워서 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8616}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8616}
</div>
'''
answer_8616 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/missing_data.csv')",
                              "df_answer = data.fillna(value = data['D'].mean())"]}
]
img_8616 =''

##8617 문제
table_8617 = pd.read_csv("/content/jupyter_judge/csv_file/missing_data.csv")
table_html_8617 = table_8617.to_html(max_rows = 10, max_cols = 10)
pre_table_8617 = table_8617.dropna()
pre_table_html_8617 = pre_table_8617.to_html(max_rows = 10, max_cols = 10)
question_8617 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/missing_data.csv")</h3>
<p>csv_file 폴더에 있는 missing_data.csv 파일을 Dataframe으로 불러옵니다.</p>
<p>NaN이 있는 행을 삭제하여 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8617}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8617}
</div>
'''
answer_8617 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/missing_data.csv')",
                              "df_answer = data.dropna()"]}
]
img_8617 =''

##8618 문제
table1_8618 = pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul_1to6.csv")
table2_8618 = pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul_7to12.csv")
table1_html_8618 = table1_8618.to_html(max_rows = 5, max_cols = 10)
table2_html_8618 = table2_8618.to_html(max_rows = 5, max_cols = 10)

pre_table_8618 = pd.concat([table1_8618, table2_8618], ignore_index = True)
pre_table_html_8618 = pre_table_8618.to_html(max_rows = 10, max_cols = 10)
question_8618 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data1=pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul_1to6.csv")</h3>
<h3 = "white-space: pre-wrap;">data2=pd.read_csv("/content/jupyter_judge/csv_file/bike_seoul_7to12.csv")</h3>
<p>csv_file 폴더에 있는 bike_seoul_1to6.csv, bike_seoul_7to12.csv 파일을 Dataframe으로 불러옵니다.</p>
<p>두 개의 Dataframe을 합쳐서(concat) df 변수에 입력해봅시다.</p>
<p>(index는 ignore 합니다.)</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table1_html_8618}<p>
<p>{table2_html_8618}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8618}
</div>
'''
answer_8618 = [
    {'input' : [], 'output' : ["data1=pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul_1to6.csv')",
                               "data2=pd.read_csv('/content/jupyter_judge/csv_file/bike_seoul_7to12.csv')",
                              "df_answer = pd.concat([data1, data2], ignore_index=True)"]}
]
img_8618 =''

##8619문제
table1_8619 = pd.read_csv("/content/jupyter_judge/csv_file/merge1.csv")
table2_8619 = pd.read_csv("/content/jupyter_judge/csv_file/merge2.csv")
table1_html_8619 = table1_8619.to_html(max_rows = 10, max_cols = 5)
table2_html_8619 = table2_8619.to_html(max_rows = 10, max_cols = 5)

pre_table_8619 = pd.merge(table1_8619, table2_8619, on = ['key1', 'key2'])
pre_table_html_8619 = pre_table_8619.to_html(max_rows = 10, max_cols = 10)
question_8619 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data1=pd.read_csv("/content/jupyter_judge/csv_file/merge1.csv")</h3>
<h3 = "white-space: pre-wrap;">data2=pd.read_csv("/content/jupyter_judge/csv_file/merge2.csv")</h3>
<p>csv_file 폴더에 있는 merge1.csv, merge2.csv 파일을 Dataframe으로 불러옵니다.</p>
<p>두 개의 Dataframe을 key1, key2를 기준으로 합치고(merge), df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table1_html_8619}<p>
<p>{table2_html_8619}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8619}
</div>
'''
answer_8619 = [
    {'input' : [], 'output' : ["data1=pd.read_csv('/content/jupyter_judge/csv_file/merge1.csv')",
                               "data2=pd.read_csv('/content/jupyter_judge/csv_file/merge2.csv')",
                              "df_answer = pd.merge(table1_8619, table2_8619, on = ['key1', 'key2'])"]}
]
img_8619 =''

##8620문제
table_8620 = pd.read_pickle("/content/jupyter_judge/csv_file/multiindex.pkl")
table_html_8620 = table_8620.to_html(max_rows = 10, max_cols = 10)

pre_table_8620 = table_8620.stack()
pre_table_html_8620 = pre_table_8620.to_frame().to_html(max_rows = 10, max_cols = 10)
question_8620 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_pickle("/content/jupyter_judge/csv_file/multiindex.pkl")</h3>
<p>csv_file 폴더에 있는 multiindex.pkl 파일을 Dataframe으로 불러옵니다.</p>
<p>Dataframe을 stack 하여 df 변수에 입력해봅시다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8620}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8620}
</div>
'''
answer_8620 = [
    {'input' : [], 'output' : ["data=pd.read_pickle('/content/jupyter_judge/csv_file/multiindex.pkl')",
                              "df_answer = data.stack()"]}
]
img_8620 =''

##8621문제
table_8621 = pd.read_csv('/content/jupyter_judge/csv_file/pivot_table.csv')
table_html_8621 = table_8621.to_html(max_rows = 10, max_cols = 10)

pre_table_8621 = pd.pivot_table(table_8621, values = 'D', index = ['A', 'B'], columns = ['C'])
pre_table_html_8621 = pre_table_8621.to_html(max_rows = 10, max_cols = 10)
question_8621 = f''' <h2 style = "background-color:yellow; ">문제 설명</h2>
<h3 = "white-space: pre-wrap;">data=pd.read_csv("/content/jupyter_judge/csv_file/pivot_table.csv")</h3>
<p>csv_file 폴더에 있는 pivot_table.csv 파일을 Dataframe으로 불러옵니다.</p>
<p>1. Dataframe을 pivot_table을 만들어서 df 변수에 입력해봅시다.</p>
<p>2. 'A', 'B'열을 index로 합니다.</p>
<p>3. 'C'열을 coloumn으로 합니다. </p>
<p>4. 'D'열을 값으로 합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 전처리 전 데이터 </h2>
<p>{table_html_8621}<p>
</div>
<div style = "float:right;width:50%">
<h2> 전처리 후 데이터 </h2>
{pre_table_html_8621}
</div>
'''
answer_8621 = [
    {'input' : [], 'output' : ["data=pd.read_csv('/content/jupyter_judge/csv_file/pivot_table.csv')",
                              "df_answer =pd.pivot_table(table_8621, values = 'D', index = ['A', 'B'], columns = ['C'])"]}
]
img_8621 =''

#메타데이터
test_set = [
#입력,변수,출력_수와 연산산
    {'test_file' : '_1101.py', 'answer' : answer_1101, 'question' : question_1101, 'img' : img_1101},
    {'test_file' : '_1102.py', 'answer' : answer_1102, 'question' : question_1102, 'img' : img_1102},   
    {'test_file' : '_1103.py', 'answer' : answer_1103, 'question' : question_1103, 'img' : img_1103},
    {'test_file' : '_1201.py', 'answer' : answer_1201, 'question' : question_1201, 'img' : img_1201},
    {'test_file' : '_1202.py', 'answer' : answer_1202, 'question' : question_1202, 'img' : img_1202},
    {'test_file' : '_1203.py', 'answer' : answer_1203, 'question' : question_1203, 'img' : img_1203},
    {'test_file' : '_1204.py', 'answer' : answer_1204, 'question' : question_1204, 'img' : img_1204},
#입력,변수,출력_측정정
    {'test_file' : '_2401.py', 'answer' : answer_2401, 'question' : question_2401, 'img' : img_2401},
    {'test_file' : '_2402.py', 'answer' : answer_2402, 'question' : question_2402, 'img' : img_2402},
    {'test_file' : '_2403.py', 'answer' : answer_2403, 'question' : question_2403, 'img' : img_2403},
    {'test_file' : '_2404.py', 'answer' : answer_2404, 'question' : question_2404, 'img' : img_2404},


    {'test_file' : '_3101.py', 'answer' : answer_3101, 'question' : question_3101, 'img' : img_3101},
    {'test_file' : '_3102.py', 'answer' : answer_3102, 'question' : question_3102, 'img' : img_3102},
    {'test_file' : '_3103.py', 'answer' : answer_3103, 'question' : question_3103, 'img' : img_3103},
    {'test_file' : '_3104.py', 'answer' : answer_3104, 'question' : question_3104, 'img' : img_3104},
    #3105문제는 조건으로 옮김.
    {'test_file' : '_3106.py', 'answer' : answer_3106, 'question' : question_3106, 'img' : img_3106},
    {'test_file' : '_3107.py', 'answer' : answer_3107, 'question' : question_3107, 'img' : img_3107},    
    {'test_file' : '_3108.py', 'answer' : answer_3108, 'question' : question_3108, 'img' : img_3108},

    {'test_file' : '_3301.py', 'answer' : answer_3301, 'question' : question_3301, 'img' : img_3301},
    {'test_file' : '_3302.py', 'answer' : answer_3302, 'question' : question_3302, 'img' : img_3302},
    {'test_file' : '_3303.py', 'answer' : answer_3303, 'question' : question_3303, 'img' : img_3303},
    {'test_file' : '_3304.py', 'answer' : answer_3304, 'question' : question_3304, 'img' : img_3304},
    {'test_file' : '_3305.py', 'answer' : answer_3305, 'question' : question_3305, 'img' : img_3305},
    {'test_file' : '_3306.py', 'answer' : answer_3306, 'question' : question_3306, 'img' : img_3306},
    {'test_file' : '_3307.py', 'answer' : answer_3307, 'question' : question_3307, 'img' : img_3307},
    {'test_file' : '_3308.py', 'answer' : answer_3308, 'question' : question_3308, 'img' : img_3308},
    {'test_file' : '_3309.py', 'answer' : answer_3309, 'question' : question_3309, 'img' : img_3309},
    {'test_file' : '_3310.py', 'answer' : answer_3310, 'question' : question_3310, 'img' : img_3310},
    {'test_file' : '_3311.py', 'answer' : answer_3311, 'question' : question_3311, 'img' : img_3311},
    {'test_file' : '_3312.py', 'answer' : answer_3312, 'question' : question_3312, 'img' : img_3312},
    {'test_file' : '_3313.py', 'answer' : answer_3313, 'question' : question_3313, 'img' : img_3313},
    {'test_file' : '_3314.py', 'answer' : answer_3314, 'question' : question_3314, 'img' : img_3314},

    {'test_file' : '_3401.py', 'answer' : answer_3401, 'question' : question_3401, 'img' : img_3401},
    {'test_file' : '_3402.py', 'answer' : answer_3402, 'question' : question_3402, 'img' : img_3402},
    {'test_file' : '_3403.py', 'answer' : answer_3403, 'question' : question_3403, 'img' : img_3403},    
#입력,변수,출력_자료와가능성
    {'test_file' : '_4101.py', 'answer' : answer_4101, 'question' : question_4101, 'img' : img_4101},
    {'test_file' : '_4102.py', 'answer' : answer_4102, 'question' : question_4102, 'img' : img_4102},
    {'test_file' : '_4103.py', 'answer' : answer_4103, 'question' : question_4103, 'img' : img_4103},
    {'test_file' : '_4104.py', 'answer' : answer_4104, 'question' : question_4104, 'img' : img_4104},
    {'test_file' : '_4105.py', 'answer' : answer_4105, 'question' : question_4105, 'img' : img_4105},
    {'test_file' : '_4106.py', 'answer' : answer_4106, 'question' : question_4106, 'img' : img_4106},
    {'test_file' : '_4107.py', 'answer' : answer_4107, 'question' : question_4107, 'img' : img_4107},
    
    {'test_file' : '_5101.py', 'answer' : answer_5101, 'question' : question_5101, 'img' : img_5101},
    {'test_file' : '_5102.py', 'answer' : answer_5102, 'question' : question_5102, 'img' : img_5102},
    {'test_file' : '_5103.py', 'answer' : answer_5103, 'question' : question_5103, 'img' : img_5103},
    {'test_file' : '_5104.py', 'answer' : answer_5104, 'question' : question_5104, 'img' : img_5104},
    {'test_file' : '_5105.py', 'answer' : answer_5105, 'question' : question_5105, 'img' : img_5105},        
    #colabturtle test
    {'test_file' : '_5201.py', 'answer' : answer_5201, 'question' : question_5201, 'img' : img_5201},     
    {'test_file' : '_5202.py', 'answer' : answer_5202, 'question' : question_5202, 'img' : img_5202},        
    {'test_file' : '_5203.py', 'answer' : answer_5203, 'question' : question_5203, 'img' : img_5203},     
    {'test_file' : '_5204.py', 'answer' : answer_5204, 'question' : question_5204, 'img' : img_5204},          
    {'test_file' : '_5205.py', 'answer' : answer_5205, 'question' : question_5205, 'img' : img_5205},
    {'test_file' : '_5206.py', 'answer' : answer_5206, 'question' : question_5206, 'img' : img_5206},       

    {'test_file' : '_6101.py', 'answer' : answer_6101, 'question' : question_6101, 'img' : img_6101},
    {'test_file' : '_6102.py', 'answer' : answer_6102, 'question' : question_6102, 'img' : img_6102},   
    {'test_file' : '_6103.py', 'answer' : answer_6103, 'question' : question_6103, 'img' : img_6103},
    {'test_file' : '_6104.py', 'answer' : answer_6104, 'question' : question_6104, 'img' : img_6104},
    {'test_file' : '_6105.py', 'answer' : answer_6105, 'question' : question_6105, 'img' : img_6105},  
    {'test_file' : '_6201.py', 'answer' : answer_6201, 'question' : question_6201, 'img' : img_6201},
    {'test_file' : '_6202.py', 'answer' : answer_6202, 'question' : question_6202, 'img' : img_6202},
    {'test_file' : '_6203.py', 'answer' : answer_6203, 'question' : question_6203, 'img' : img_6203},   
    {'test_file' : '_6301.py', 'answer' : answer_6301, 'question' : question_6301, 'img' : img_6301},
    {'test_file' : '_6302.py', 'answer' : answer_6302, 'question' : question_6302, 'img' : img_6302},
    {'test_file' : '_6303.py', 'answer' : answer_6303, 'question' : question_6303, 'img' : img_6303},

 
    
    {'test_file' : '_7101.py', 'answer' : answer_7101, 'question' : question_7101, 'img' : img_7101},
    {'test_file' : '_7102.py', 'answer' : answer_7102, 'question' : question_7102, 'img' : img_7102},
    {'test_file' : '_7103.py', 'answer' : answer_7103, 'question' : question_7103, 'img' : img_7103},
    {'test_file' : '_7104.py', 'answer' : answer_7104, 'question' : question_7104, 'img' : img_7104},
    {'test_file' : '_7105.py', 'answer' : answer_7105, 'question' : question_7105, 'img' : img_7105},
    {'test_file' : '_7501.py', 'answer' : answer_7501, 'question' : question_7501, 'img' : img_7501},
    {'test_file' : '_7502.py', 'answer' : answer_7502, 'question' : question_7502, 'img' : img_7502},       
    
    {'test_file' : '_3000.py', 'answer' : answer_3000, 'question' : question_3000, 'img' : img_3000},        
    {'test_file' : '_3100.py', 'answer' : answer_3100, 'question' : question_3100, 'img' : img_3100},    
    {'test_file' : '_3200.py', 'answer' : answer_3200, 'question' : question_3200, 'img' : img_3200},    
    {'test_file' : '_3300.py', 'answer' : answer_3300, 'question' : question_3300, 'img' : img_3300},       
  
    #테스트를 위함.
    {'test_file' : '_8000.py', 'answer' : answer_8000, 'question' : question_8000, 'img' : img_8000},  
    {'test_file' : '_8002.py', 'answer' : answer_8002, 'question' : question_8002, 'img' : img_8002},   
    {'test_file' : '_8003.py', 'answer' : answer_8003, 'question' : question_8003, 'img' : img_8003},   
    {'test_file' : '_8004.py', 'answer' : answer_8004, 'question' : question_8004, 'img' : img_8004},
    {'test_file' : '_8005.py', 'answer' : answer_8005, 'question' : question_8005, 'img' : img_8005},
    {'test_file' : '_8006.py', 'answer' : answer_8006, 'question' : question_8006, 'img' : img_8006},
    {'test_file' : '_8007.py', 'answer' : answer_8007, 'question' : question_8007, 'img' : img_8007},
    {'test_file' : '_8008.py', 'answer' : answer_8008, 'question' : question_8008, 'img' : img_8008},
    {'test_file' : '_8009.py', 'answer' : answer_8009, 'question' : question_8009, 'img' : img_8009},     
  
  
    #plot_check() 문제 모음
    {'test_file' : '_8201.py', 'answer' : answer_8201, 'question' : question_8201, 'img' : img_8201},        
    {'test_file' : '_8203.py', 'answer' : answer_8203, 'question' : question_8203, 'img' : img_8203},    
    {'test_file' : '_8206.py', 'answer' : answer_8206, 'question' : question_8206, 'img' : img_8206},    
    {'test_file' : '_8208.py', 'answer' : answer_8208, 'question' : question_8208, 'img' : img_8208},        
    {'test_file' : '_8211.py', 'answer' : answer_8211, 'question' : question_8211, 'img' : img_8211},      
    {'test_file' : '_8219.py', 'answer' : answer_8219, 'question' : question_8219, 'img' : img_8219},        
    {'test_file' : '_8220.py', 'answer' : answer_8220, 'question' : question_8220, 'img' : img_8220},         
    {'test_file' : '_8401.py', 'answer' : answer_8401, 'question' : question_8401, 'img' : img_8401},      
    {'test_file' : '_8402.py', 'answer' : answer_8402, 'question' : question_8402, 'img' : img_8402},        
    {'test_file' : '_8403.py', 'answer' : answer_8403, 'question' : question_8403, 'img' : img_8403},        

    {'test_file' : '_8501.py', 'answer' : answer_8501, 'question' : question_8501, 'img' : img_8501},        
    {'test_file' : '_8502.py', 'answer' : answer_8502, 'question' : question_8502, 'img' : img_8502},    
    {'test_file' : '_8503.py', 'answer' : answer_8503, 'question' : question_8503, 'img' : img_8503},        
    {'test_file' : '_8504.py', 'answer' : answer_8504, 'question' : question_8504, 'img' : img_8504},    
  
    {'test_file' : '_8511.py', 'answer' : answer_8511, 'question' : question_8511, 'img' : img_8511},    
    {'test_file' : '_8512.py', 'answer' : answer_8512, 'question' : question_8512, 'img' : img_8512},        
    {'test_file' : '_8513.py', 'answer' : answer_8513, 'question' : question_8513, 'img' : img_8513},      
    {'test_file' : '_8521.py', 'answer' : answer_8521, 'question' : question_8521, 'img' : img_8521},        
    {'test_file' : '_8522.py', 'answer' : answer_8522, 'question' : question_8522, 'img' : img_8522},         
    {'test_file' : '_8523.py', 'answer' : answer_8523, 'question' : question_8523, 'img' : img_8523},   
    {'test_file' : '_8524.py', 'answer' : answer_8524, 'question' : question_8524, 'img' : img_8524},        
    {'test_file' : '_8525.py', 'answer' : answer_8525, 'question' : question_8525, 'img' : img_8525},         
    {'test_file' : '_8526.py', 'answer' : answer_8526, 'question' : question_8526, 'img' : img_8526},   

  
    {'test_file' : '_8531.py', 'answer' : answer_8531, 'question' : question_8531, 'img' : img_8531},        
    {'test_file' : '_8532.py', 'answer' : answer_8532, 'question' : question_8532, 'img' : img_8532},        
    {'test_file' : '_8533.py', 'answer' : answer_8533, 'question' : question_8533, 'img' : img_8533},        
    {'test_file' : '_8534.py', 'answer' : answer_8534, 'question' : question_8534, 'img' : img_8534},    
    {'test_file' : '_8541.py', 'answer' : answer_8541, 'question' : question_8541, 'img' : img_8541},    
    {'test_file' : '_8542.py', 'answer' : answer_8542, 'question' : question_8542, 'img' : img_8542},        
    {'test_file' : '_8543.py', 'answer' : answer_8543, 'question' : question_8543, 'img' : img_8543},    
    {'test_file' : '_8544.py', 'answer' : answer_8544, 'question' : question_8544, 'img' : img_8544},   
    {'test_file' : '_8545.py', 'answer' : answer_8545, 'question' : question_8545, 'img' : img_8545},   
  
    {'test_file' : '_8551.py', 'answer' : answer_8551, 'question' : question_8551, 'img' : img_8551},      
    {'test_file' : '_8552.py', 'answer' : answer_8552, 'question' : question_8552, 'img' : img_8552},        
    {'test_file' : '_8561.py', 'answer' : answer_8561, 'question' : question_8561, 'img' : img_8561},         
    {'test_file' : '_8562.py', 'answer' : answer_8562, 'question' : question_8562, 'img' : img_8562},      
    {'test_file' : '_8563.py', 'answer' : answer_8563, 'question' : question_8563, 'img' : img_8563},        
    {'test_file' : '_8564.py', 'answer' : answer_8564, 'question' : question_8564, 'img' : img_8564},          
    {'test_file' : '_8571.py', 'answer' : answer_8571, 'question' : question_8571, 'img' : img_8571},         
    {'test_file' : '_8572.py', 'answer' : answer_8572, 'question' : question_8572, 'img' : img_8572},      
    {'test_file' : '_8573.py', 'answer' : answer_8573, 'question' : question_8573, 'img' : img_8573},        
    {'test_file' : '_8574.py', 'answer' : answer_8574, 'question' : question_8574, 'img' : img_8574},         
    {'test_file' : '_8581.py', 'answer' : answer_8581, 'question' : question_8581, 'img' : img_8581},         
    {'test_file' : '_8582.py', 'answer' : answer_8582, 'question' : question_8582, 'img' : img_8582},      
    {'test_file' : '_8583.py', 'answer' : answer_8583, 'question' : question_8583, 'img' : img_8583},        
    #판다스 평가 문제
    {'test_file' : '_8601.py', 'answer' : answer_8601, 'question' : question_8601, 'img' : img_8601},
    {'test_file' : '_8602.py', 'answer' : answer_8602, 'question' : question_8602, 'img' : img_8602},
    {'test_file' : '_8603.py', 'answer' : answer_8603, 'question' : question_8603, 'img' : img_8603},
    {'test_file' : '_8604.py', 'answer' : answer_8604, 'question' : question_8604, 'img' : img_8604}, 
    {'test_file' : '_8605.py', 'answer' : answer_8605, 'question' : question_8605, 'img' : img_8605}, 
    {'test_file' : '_8606.py', 'answer' : answer_8606, 'question' : question_8606, 'img' : img_8606}, 
    {'test_file' : '_8607.py', 'answer' : answer_8607, 'question' : question_8607, 'img' : img_8607}, 
    {'test_file' : '_8608.py', 'answer' : answer_8608, 'question' : question_8608, 'img' : img_8608}, 
    {'test_file' : '_8609.py', 'answer' : answer_8609, 'question' : question_8609, 'img' : img_8609}, 
    {'test_file' : '_8610.py', 'answer' : answer_8610, 'question' : question_8610, 'img' : img_8610}, 
    {'test_file' : '_8611.py', 'answer' : answer_8611, 'question' : question_8611, 'img' : img_8611}, 
    {'test_file' : '_8612.py', 'answer' : answer_8612, 'question' : question_8612, 'img' : img_8612}, 
    {'test_file' : '_8613.py', 'answer' : answer_8613, 'question' : question_8613, 'img' : img_8613}, 
    {'test_file' : '_8614.py', 'answer' : answer_8614, 'question' : question_8614, 'img' : img_8614}, 
    {'test_file' : '_8615.py', 'answer' : answer_8615, 'question' : question_8615, 'img' : img_8615}, 
    {'test_file' : '_8616.py', 'answer' : answer_8616, 'question' : question_8616, 'img' : img_8616},   
    {'test_file' : '_8617.py', 'answer' : answer_8617, 'question' : question_8617, 'img' : img_8617}, 
    {'test_file' : '_8618.py', 'answer' : answer_8618, 'question' : question_8618, 'img' : img_8618}, 
    {'test_file' : '_8619.py', 'answer' : answer_8619, 'question' : question_8619, 'img' : img_8619}, 
    {'test_file' : '_8620.py', 'answer' : answer_8620, 'question' : question_8620, 'img' : img_8620}, 
    {'test_file' : '_8621.py', 'answer' : answer_8621, 'question' : question_8621, 'img' : img_8621},     
]

from jupyter_judge.code_check import *
