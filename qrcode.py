from MyQR import myqr

"""生成动态图二维码"""
"""version int，控制边长，范围是1到40，数字越大边长越大,默认边长是取决于你输入的信息的长度和使用的纠错等级"""
"""level str，控制纠错水平，范围是L、M、Q、H，从左到右依次升高，默认纠错等级为'H'"""
myqr.run(
    words='https://github.com/yinian0110',
    picture='mao.gif',
    colorized=True,  # True：彩色，False：黑白
    save_name='D:\\python\\qrcode\\test.gif'
)