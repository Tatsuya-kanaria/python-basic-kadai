# %%

def area_of_trapezoid(top, bottom, height):
    '''
    台形の面積（cm2）を返す
    top: 上辺(cm)
    bottom: 下辺(cm)
    height: 高さ(cm)

    公式：台形の面積 =（上辺＋下辺）× 高さ ÷ 2

    return: '{} cm2'.format(area)
    '''

    area = (top + bottom) * height / 2
    return '{} cm2'.format(area)

area =  area_of_trapezoid(top=10, bottom=20, height=5)

print(area)



# %%
