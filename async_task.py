async def greetting(name):
    return 'hello ' + name


def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as err1:
        return err1.value


async def other():
    a = ["richie", "joss", "ronal"]
    for x in a:
        print(await greetting(x))


async def fib(n):
    if n < 2:
        return 1
    else:
        return await fib(n-1) + await fib(n-2)


async def serie_fib(n1):
    for n in range(n1):
        print(await fib(n))

print(run(greetting('Ariza la pajiza')))
run(other())
print('========= fibonacci number 8 ============')
print(run(fib(8)))

print('========= fibonacci serie 30 ============')
run(serie_fib(30))
