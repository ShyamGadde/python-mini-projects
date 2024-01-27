import argparse


def arithmetic_formatter(problems, display_answer=False):
    total_prob = len(problems)

    if total_prob > 5:
        return "Error: Too many problems."

    prob_lst = [problem.split() for problem in problems]

    op1_lst = [problem[0] for problem in prob_lst]
    operators = [problem[1] for problem in prob_lst]
    op2_lst = [problem[2] for problem in prob_lst]

    for operator in operators:
        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

    try:
        int_op1 = [int(op) for op in op1_lst]
        int_op2 = [int(op) for op in op2_lst]
    except ValueError:
        return "Error: Numbers must only contain digits."

    op1_digits = [len(op) for op in op1_lst]
    op2_digits = [len(op) for op in op2_lst]

    if max(op1_digits + op2_digits) > 4:
        return "Error: Numbers cannot be more than four digits."

    spacing = [max(op1_digits[i], op2_digits[i]) + 1 for i in range(total_prob)]

    row1 = "    ".join([f" {op1_lst[i].rjust(spacing[i])}" for i in range(total_prob)])

    row2 = "    ".join(
        [operators[i] + op2_lst[i].rjust(spacing[i]) for i in range(total_prob)]
    )

    row3 = "    ".join(["-" * (spacing[i] + 1) for i in range(total_prob)])

    arranged_problems = "\n".join([row1, row2, row3])

    if display_answer:
        answers = [
            int_op1[i] + int_op2[i] if operators[i] == "+" else int_op1[i] - int_op2[i]
            for i in range(total_prob)
        ]
        row4 = "    ".join(
            [f" {str(answers[i]).rjust(spacing[i])}" for i in range(total_prob)]
        )
        arranged_problems = "\n".join([arranged_problems, row4])

    return arranged_problems


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This tool formats arithmetic problems for better readability. It takes a list of arithmetic problems and optionally displays their answers.",
        epilog="""Example:
        Command: python arithmetic-formatter.py '32 + 698' '3801 - 2' '45 + 43' '123 + 49' --display_answer
        Output:
           32      3801      45      123
        + 698    -    2    + 43    +  49
        -----    ------    ----    -----
          730      3799      88      172
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "problems", nargs="+", help="Arithmetic problems to be formatted."
    )
    parser.add_argument(
        "-d",
        "--display_answer",
        action="store_true",
        help="Display the answers of the problems.",
    )
    args = parser.parse_args()

    print(arithmetic_formatter(args.problems, args.display_answer))
