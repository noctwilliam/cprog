import re

def parse_equation(equation):
    # Tokenize the equation using regular expressions
    tokens = re.findall(r'\d+|\w+|[()+*/-]', equation)
    return tokens

def build_expression_tree(tokens):
    operators = {'+', '-', '*', '/'}
    stack = []
    root = None

    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                operator = stack.pop()
                operand2 = stack.pop()
                operand1 = stack.pop()
                node = {'type': 'operator', 'value': operator, 'left': operand1, 'right': operand2}
                stack.append(node)
            stack.pop()  # Discard '('
        elif token in operators:
            stack.append(token)
        else:
            node = {'type': 'variable', 'value': token}
            stack.append(node)

    if stack:
        root = stack.pop()

    return root

def evaluate_expression_tree(node, variable_values):
    if node['type'] == 'variable':
        return variable_values[node['value']]
    else:
        left = evaluate_expression_tree(node['left'], variable_values)
        right = evaluate_expression_tree(node['right'], variable_values)
        operator = node['value']
        
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right

def solve_equation(equation):
    tokens = parse_equation(equation)
    expression_tree = build_expression_tree(tokens)

    variables = set(token for token in tokens if re.match(r'\w+', token))
    variable_values = {}

    for variable in variables:
        value = float(input(f"Enter the value for variable {variable}: "))
        variable_values[variable] = value

    solution = {}
    for variable in variables:
        variable_values[variable] = evaluate_expression_tree(expression_tree, variable_values)
        solution[variable] = variable_values[variable]

    return solution

# Example usage
equation = "(a + b) * (c - d) = e * f"
solution = solve_equation(equation)
print(solution)