import pyethereum
import pytest

t = pyethereum.tester
s = t.state()
c = s.contract("salaried_corp.se")

def initialize_contract(key, ether):
    s.mine(1)
    print "Initialized contract with %i ether" % ether
    return s.send(key, c, ether)

def transfer(key, sh_address, num_shares):
    s.mine(1)
    print "\nTransfered %i shares..." % num_shares
    return s.send(key, c, 0, [1, sh_address, num_shares])


def check_share_balances():
    s.mine(1)
    print "\nShare balances (shares):"
    print "%i\t%i" % (
            s.send(t.k2, c, 0, [2])[0],
            s.send(t.k1, c, 0, [2])[0])

def pay_dividends(admin_key):
    div = s.send(admin_key, c, 0, [3])
    s.mine(1)
    print "\nPaid %i in dividends to shareholders" % div[0]

def pay_salaries(admin_key):
    s.mine(1)
    return s.send(admin_key, c, 0, [6])

def make_profit(ether):
    s.mine(1)
    print "\nMade %i profit" % ether
    return s.send(t.k9, c, ether, [3])

def print_account_balances():
    print "Account balances (Ether)"
    print "%i\t%i" % (
            s.block.get_balance(t.a2) - initial[0],
            s.block.get_balance(t.a1) - initial[1])
 
def set_salary(key, worker_address, daily_salary):
    s.mine(1)
    return s.send(key, c, 0, [4, worker_address, daily_salary])

def check_salary(key):
    s.mine(1)
    return s.send(t.k2, c, 0, [7])

initialize_contract(t.k9, 10**9)
set_salary(t.k9, t.a2, 10000)
set_salary(t.k9, t.a3, 10000)

salary = check_salary(t.k2)[0]
assert salary == 10000

bal_before = pay_salaries(t.k9)
s.mine(61)
bal_after = pay_salaries(t.k9)
print bal_before
print bal_after
assert (bal_before[0] - bal_after[0]) == 2*salary

print pay_salaries(t.k9)
s.mine(61)
print pay_salaries(t.k9)
s.mine(61)
print pay_salaries(t.k9)
