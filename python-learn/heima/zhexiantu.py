import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts
def main():
    #打开文件
    f_us=open("python-learn\heima\Info\美国.txt","r",encoding="utf-8")
    f_jp=open("python-learn\heima\Info\日本.txt","r",encoding="utf-8")
    f_in=open("python-learn\heima\Info\印度.txt","r",encoding="utf-8")
    #读取数据
    us_data=f_us.read()
    jp_data=f_jp.read()    
    in_data=f_in.read()
    #去掉开头不规范的数据
    us_data=us_data.replace("jsonp_1629344292311_69436(","")
    jp_data=jp_data.replace("jsonp_1629350871167_29498(","")
    in_data=in_data.replace("jsonp_1629350745930_63180(","")
    #去掉结尾不规范的数据
    us_data=us_data[:-2]
    jp_data=jp_data[:-2]
    in_data=in_data[:-2]
    #数据转换为字典
    us_dict=json.loads(us_data)
    jp_dict=json.loads(jp_data)
    in_dict=json.loads(in_data)
    #获取数据
    us_trend=us_dict['data'][0]['trend']
    jp_trend=jp_dict['data'][0]['trend']
    in_trend=in_dict['data'][0]['trend']
    #获取x轴
    us_x_date=us_trend['updateDate'][:314]
    jp_x_date=jp_trend['updateDate'][:314]
    in_x_date=in_trend['updateDate'][:314]
    #获取y轴
    us_y_data=us_trend['list'][0]['data'][:314]
    jp_y_data=jp_trend['list'][0]['data'][:314]
    in_y_data=in_trend['list'][0]['data'][:314]
    #创建折线图
    line=Line()
    line.add_xaxis(us_x_date)
    line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
    line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
    line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))
    line.set_global_opts(
        title_opts=TitleOpts(title="全球疫情趋势",pos_left="center",pos_bottom="1%")
    )
    line.render("python-learn\heima\Info\疫情趋势.html")
    
if __name__ == "__main__":
    main()