value=float(input('请输入长度：'))
unit=input('请输入单位：')
if unit=='in' or unit=='英寸':
    print('%f英寸=%f厘米'%(value,value*2.54))
elif unit=='cm' or unit=='厘米':
    print('%f厘米=%f英寸'%(value,value/2.54))