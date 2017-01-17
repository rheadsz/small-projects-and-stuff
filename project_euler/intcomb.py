
val_list = []

def int_comb():
    for x in range(2,101):
        for i in range(2,101):
            #print(x**i,'({})'.format(x))
            val_list.append(x**i)
    return sorted(set(val_list))


def self_power():
    return sum([x**x for x in range(1,1001)])


if __name__ == '__main__':
    print(self_power())
