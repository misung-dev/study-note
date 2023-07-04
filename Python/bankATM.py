class Account:

  def __init__(self, name, amount):
    self.owner = name
    self.balance = amount

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print("잔액 부족")

  def print_balance(self):
    print("잔액:", self.balance)


def atm():
  accounts = {}
  currentName = None

  def validateAtmMenuNum(menuNum):
    menuNumList = ["1", "2", "3", "4"]

    if menuNum in menuNumList:
      return True
    else:
      return False

  def getCurrentName(name):
    nonlocal currentName

    if name == "_":
      return currentName
    else:
      currentName = name
      return name

  while True:
    print("계좌개설/1 입금/2 출금/3 잔액조회/4")
    menuNum = input("메뉴 번호를 입력하세요 >>> ")
    print("이름을 이미 입력한 고객께서는 이름 대신 _를 입력하시면 됩니다.")

    if validateAtmMenuNum(menuNum):
      menuNum = int(menuNum)
    else:
      print("메뉴를 잘못 선택하였으니 다시 입력해주세요.")
      continue

    if menuNum == 1:
      name, amount = input("이름/개설금액: ").split("/")
      currentName = name
      amount = int(amount)

      if name in accounts:
        print("계좌가 이미 개설되어 있습니다")
      else:
        account = Account(name, amount)
        accounts[name] = account
    elif menuNum == 2:
      name, amount = input("이름/입금액: ").split("/")
      name = getCurrentName(name)
      amount = int(amount)

      if name in accounts:
        account = accounts[name]
        account.deposit(amount)
      else:
        print("계좌를 먼저 개설하시오.")
    elif menuNum == 3:
      name, amount = input("이름/출금액: ").split("/")
      name = getCurrentName(name)
      amount = int(amount)

      if name in accounts:
        account = accounts[name]
        account.withdraw(amount)
      else:
        print("계좌를 먼저 개설하시오.")
    elif menuNum == 4:
      name = input("이름: ")
      name = getCurrentName(name)

      if name in accounts:
        account = accounts[name]
        account.print_balance()
      else:
        print("계좌를 먼저 개설하시오.")


atm()
