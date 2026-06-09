def main():
    print("Hello from llmops-api!")


if __name__ == "__main__":
    main()
from injector import Injector, inject

class A:
    name: str = "LLMOps"

@inject
class B:
    def __init__(self, a: A):
        self.a = a
    def print(self):
        print(f"{self.a.name}")
