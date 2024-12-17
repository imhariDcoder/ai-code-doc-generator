import ast

def generate_function(name, args, body):
  """Generates a Python function definition as an AST node."""
  func_args = ast.arguments(
      posonlyargs=[],
      args=[ast.arg(arg=arg) for arg in args],
      kwonlyargs=[],
      kw_defaults=[],
      defaults=[],
  )
  func_body = [ast.Expr(value=ast.Constant(value=body))] 
  func_def = ast.FunctionDef(
      name=name, args=func_args, body=func_body, decorator_list=[]
  )
  return func_def

# Example usage:
func_node = generate_function("add_numbers", ["x", "y"], "return x + y")
func_code = ast.unparse(func_node)
print(func_code)  # Output: def add_numbers(x, y): return x + y