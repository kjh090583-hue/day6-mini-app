import argparse

TODOS = [
    ("주간 보고서 초안 작성", "high", False),
    ("회의 자료 작성", "middle", False),
    ("책상 정리", "low", False),
    ("이메일 답장", "high", True),
]

PRIORITY_ORDER = {"high": 0, "middle": 1, "low": 2}


def sorted_todos(todos, include_done=False):
    shown = [todo for todo in todos if include_done or not todo[2]]
    return sorted(shown, key=lambda todo: PRIORITY_ORDER[todo[1]])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="완료한 일도 함께 보여 줍니다")
    args = parser.parse_args()

    for title, priority, done in sorted_todos(TODOS, args.all):
        suffix = " (완료)" if done else ""
        print(f"[{priority.upper()}] {title}{suffix}")


if __name__ == "__main__":
    main()
