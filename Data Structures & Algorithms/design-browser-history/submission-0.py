class ListNode:
    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        print(f'Setting homepage as {homepage}')
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        print(f'Visiting {url}')
        temp = ListNode(url, next=None, prev=self.current)
        
        self.current.next = temp
        self.current = self.current.next
        self.tail = self.current

    def back(self, steps: int) -> str:
        print(f'Going back {steps} in history')
        print(f'Current node => {self.current.val}')
        for _ in range(steps):
            if self.current.prev is None:
                break
            self.current = self.current.prev
            print(f'Current node => {self.current.val}')

        return self.current.val

    def forward(self, steps: int) -> str:
        print(f'Going forward {steps} in history')
        print(f'Current node => {self.current.val}')
        for _ in range(steps):
            if self.current.next is None:
                break
            self.current = self.current.next
            print(f'Current node => {self.current.val}')

        return self.current.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)