# %%
def fizzbuzz(var):
    '''
    var % 15 = 0 : FizzBuzz
    var % 5 == 0 : Buzz
    var % 3 = 0 : Fizz
    else : var
    '''
    if var % 15 == 0:
        return "FizzBuzz"
    elif var % 5 == 0:
        return "Fizz"
    elif var % 3 == 0:
        return "Buzz"
    else:
        return var

while True:
    try:
        var = int(input("整数を入力して下さい。\n"))
    except KeyboardInterrupt:
        print("終了しました。")
        break
    except:
        continue
    else:
        result = fizzbuzz(var)
        print(result)
        break

# %%
