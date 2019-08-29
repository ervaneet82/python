def outer():
  x = "python"
  def inner():
    print(x)
  return inner

fn = outer()
fn()

