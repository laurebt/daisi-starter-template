def hello(name="Daisi"):
  return f"Hello {name}!"

def app():
  st.write(hello())

if __name__ == '__main__':
  app()
