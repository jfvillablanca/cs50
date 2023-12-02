operand_1, operation, operand_2 = input("Expression: ").split()
match operation:
    case "+":
        print(f"{float(operand_1) + float(operand_2)}")
    case "-":
        print(f"{float(operand_1) - float(operand_2)}")
    case "*":
        print(f"{float(operand_1) * float(operand_2)}")
    case "/":
        print(f"{float(operand_1) / float(operand_2)}")
