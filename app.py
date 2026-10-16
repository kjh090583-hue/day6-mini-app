TODOS = [
    ("주간 보고서 초안 작성", "high", False),
    ("회의 자료 작성", "middle", False),
    ("책상 정리", "low", False),
    ("이메일 답장", "high", True),
]

PRIORITY_ORDER = {"high": 0, "middle": 1, "low": 2}


def pending_sorted(todos):
    pending = [todo for todo in todos if not todo[2]]
    return sorted(pending, key=lambda todo: PRIORITY_ORDER[todo[1]])


def main():
    for title, priority, _ in pending_sorted(TODOS):
        print(f"{title} ({priority})")


if __name__ == "__main__":
    main()
