import pyethereum

t = pyethereum.tester
s = t.state()
c = s.contract("corp.se")

def initialize_contract(ether):
    s.mine(1)
    s.send(t.k2, c, ether)
    print "Initialized contract with %i ether" % ether


def transfer(key, sh_address, num_shares):
    s.mine(1)
    print s.send(key, c, 0, [1, sh_address, num_shares])
    print "\nTransfered %i shares..." % num_shares


def check_share_balances():
    s.mine(1)
    print "\nShare balances (shares):"
    print "%i\t%i" % (
            s.send(t.k2, c, 0, [2])[0],
            s.send(t.k1, c, 0, [2])[0])

def pay_dividends():
    div = s.send(t.k2, c, 0, [3])
    s.mine(1)
    print "\nPaid %i in dividends to shareholders" % div[0]

def make_profit(ether):
    s.mine(1)
    s.send(t.k9, c, ether, [3])
    print "\nMade %i profit" % ether

def print_account_balances():
    print "Account balances (Ether)"
    print "%i\t%i" % (
            s.block.get_balance(t.a2) - initial[0],
            s.block.get_balance(t.a1) - initial[1])
    
initialize_contract(10**9)
transfer(t.k2, t.a1, 30000)
initial = [
    s.block.get_balance(t.a2),
    s.block.get_balance(t.a1)]

check_share_balances()
print_account_balances()

pay_dividends()
print_account_balances()

make_profit(200000000)
pay_dividends()
print_account_balances()


transfer(t.k1, t.a2, 10000)
check_share_balances()
make_profit(100000000)
pay_dividends()
print_account_balances()

