# app.py 계획

## 목적
할 일을 우선순위 순서로 보여 주는 Python CLI 앱(app.py)을 만든다. 외부 의존성은 추가하지 않고 표준 라이브러리만 쓴다.

## 읽은 파일
- AGENTS.md
- 프로젝트 폴더 목록: AGENTS.md만 있음. app.py, 데이터 파일, 테스트, pyproject.toml은 없어서 기존 코드 스타일은 확인할 수 없음.

## 만들거나 수정할 파일
- 새로 만들기: app.py (단일 파일, 표준 라이브러리만 사용)
- 수정·삭제하는 기존 파일: 없음
- 데이터 파일(예: todos.json)은 질문 1의 답을 받은 뒤에 결정

## 구현할 함수
- `load_todos()`: 할 일 불러오기
- `sort_by_priority(todos)`: 우선순위 순 정렬. 같은 우선순위는 입력 순서 유지
- `format_todo(todo)`: 한 줄 출력 문자열 만들기
- `show_todos(todos)`: 정렬한 목록 출력
- `main()`: 진입점
- 저장·추가 기능을 넣기로 하면 `save_todos()`, `add_todo()` 추가. 기존 데이터 파일을 덮어쓰기 전에는 먼저 확인을 받음

## 실행할 확인 명령 (uv)
```
uv --version
uv run python --version
uv run app.py
uv run python -m unittest   # 테스트 파일이 생기는 경우에만
```
외부 의존성을 추가하지 않으므로 `uv add`는 쓰지 않음. pyproject.toml이 없으면 `uv run`은 임시 환경으로 실행됨.

## 결정이 필요한 질문
1. 데이터는 어떻게 저장할까? 코드 안 샘플 데이터, JSON 파일, 실행 중 입력 중에서 선택. 이미 쓰는 할 일 데이터 파일이 있으면 위치도 확인
2. 기능 범위: 목록 보기만 / 추가·완료·삭제까지
3. 우선순위 표현: 숫자(1이 가장 높음) / 높음·중간·낮음
4. 출력은 한국어인가? 번호·우선순위·제목 외에 마감일 같은 필드가 필요한가?
5. test_app.py 추가를 허용하는가? (AGENTS.md상 요청 밖 파일 추가 금지)
6. pyproject.toml을 만들어 uv 프로젝트로 구성할까, `uv run app.py`만 쓸까?
