calls = -1
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(a):
    b = str(len(a))
    c = a.upper()
    d = a.lower()
    g = list({b, c, d})
    list.sort(g)
    count_calls()
    return g
def is_contains(a, b):
    count_calls()
    e = a.lower()
    c = [d.lower() for d in b]
    f = c.__contains__(e)
    return f
print(string_info('Bananananza'))
print(string_info('Bomberrshshtrase'))
print(string_info('Amore'))
print(is_contains('Flower', ['FloWeR', 'FLOW', 'shOwer']))
print(is_contains('Ass', ['aSSeTs', 'SEC']))
print(is_contains('Bitch', ['BleACh', 'BeACH', 'witcH', 'bItCh']))
print(count_calls())
