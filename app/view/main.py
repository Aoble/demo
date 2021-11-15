from flask import Blueprint, render_template
from app.models import *
from sqlalchemy import *

main = Blueprint('main', __name__)


@main.route('/')
def index():
    one = hz_1()
    two = hz_2()
    three = hz_3()
    four = hz_4()
    five = hz_5()
    six = hz_6()
    return render_template('index.html', one=one, two=two, three=three, four=four, five=five, six=six)


def hz_1():
    sql1 = '''SELECT case a.`商户业务包` 
    when 'GKA' THEN '大客户' 
    when 'BL' THEN '白领' 
    when 'SIG' THEN '小客户' 
    when 'GX' THEN '高校' 
    when 'FML' THEN '家庭' 
    when 'OTH' THEN '其他' END as '客户',COUNT(a.`商户业务包`) as '数量' 
    FROM distribution_platform a join store_basic_informations b 
    on a.restaurant_inside_id = b.restaurant_inside_id WHERE b.city_name="北京市" GROUP BY a.`商户业务包` ORDER BY 数量 desc;'''
    a = db.session.execute(sql1).fetchall()
    sql2 = '''SELECT case a.`商户业务包` 
    when 'GKA' THEN '大客户' 
    when 'BL' THEN '白领' 
    when 'SIG' THEN '小客户' 
    when 'GX' THEN '高校' 
    when 'FML' THEN '家庭' 
    when 'OTH' THEN '其他' END as '客户',COUNT(a.`商户业务包`) as '数量' 
    FROM distribution_platform a join store_basic_informations b 
    on a.restaurant_inside_id = b.restaurant_inside_id WHERE b.city_name="广州市" GROUP BY a.`商户业务包` ORDER BY 数量 desc;'''
    b = db.session.execute(sql2).fetchall()
    for i in range(len(a)):
        print("==北京：", i+1, ".商户业务包：", a[i][0], "商家数量：", a[i][1], "家===")
    for i in range(len(b)):
        print("==广州：", i+1, ".商户业务包：", b[i][0], "商家数量：", b[i][1], "家===")
    data1 = []
    pi = {}
    for i in a:
        pi['name'] = i[0]
        pi['value'] = i[1]
        data1.append(pi.copy())
    data2 = []
    pe = {}
    for i in b:
        pe['name'] = i[0]
        pe['value'] = i[1]
        data2.append(pe.copy())
    data = [data1, data2]
    return data


def hz_2():
    sql = '''SELECT case `商户业务包` 
    when 'GKA' THEN '大客户' 
    when 'BL' THEN '白领' 
    when 'SIG' THEN '小客户' 
    when 'GX' THEN '高校' 
    when 'FML' THEN '家庭' 
    when 'OTH' THEN '其他' END as '客户',`差评数`,`好评数`,`评价数` FROM distribution_platform GROUP BY `商户业务包` ORDER BY `评价数` desc;'''
    a = db.session.execute(sql).fetchall()
    for i in range(len(a)):
        print("==", i + 1, "商户业务包：", a[i][0], "，差评数：", a[i][1], "条，好评数：", a[i][2], "条===")
    data = [[x[0] for x in a], [int(x[1]) for x in a], [int(x[2]) for x in a]]
    return data


def hz_3():
    sql = '''SELECT a.`商户业务包`,a.`商户投诉数`+a.`商户投诉数` as '投诉' 
    FROM distribution_platform a join store_basic_informations b on a.restaurant_inside_id = b.restaurant_inside_id 
    WHERE b.city_name="北京市" GROUP BY a.`商户业务包` ORDER BY 投诉 desc;'''
    a = db.session.execute(sql).fetchall()
    for i in range(len(a)):
        print("==商户业务包：", a[i][0], ",  投诉数量：", a[i][1], "家===")
    data = []
    pi = {}
    for i in a:
        pi['name'] = i[0]
        pi['value'] = i[1]
        data.append(pi.copy())
    return data


def hz_4():
    a = db.session.query(Store_basic_informations.location, func.count(Store_basic_informations.platform_A_restid),
                         Store_basic_informations.latitude, Store_basic_informations.longitude)\
        .group_by(Store_basic_informations.location).all()
    for i in range(len(a)):
        print("==", i + 1, ": 商圈 ", a[i][0], "=商家数为", a[i][1], "个===")
    data = []
    for i in a:
        data.append([i[3], i[2], i[0], i[1]])
    return data


def hz_5():
    a = db.session.query(Store_basic_informations.platform_A_restid, Store_basic_informations.A_rst_name,
                         Store_basic_informations.A_day_30_cnt).order_by(
        Store_basic_informations.A_day_30_cnt.desc()).limit(10)
    b = db.session.query(Store_basic_informations.platform_B_restid, Store_basic_informations.B_rst_name,
                         Store_basic_informations.B_day_30_cnt).order_by(
        Store_basic_informations.B_day_30_cnt.desc()).limit(10)
    for i in range(0, 10):
        print("==商家标识 id:", a[i][0], a[i][1], "，Platform-A, 销量为", a[i][2], "===")
    for i in range(0, 10):
        print("==商家标识 id:", b[i][0], b[i][1], "，Platform-B, 销量为", b[i][2], "===")
    data = [x[0] for x in a], [x[2] for x in a], [x[0] for x in b], [x[2] for x in b]
    return data


def hz_6():
    sql = """select elt(interval(营业时长,0,4,6,8,12),'4小时以内','4~6小时','6-8小时','8~12小时','12小时以上') as i ,count(*) 
    from `distribution_platform` group by i order by count(*) desc;"""
    a = db.session.execute(sql).fetchall()
    for i in range(len(a)):
        print("==区间“", a[i][0], "”，商家", a[i][1], "个===")
    data = [[x[0] for x in a], [x[1] for x in a]]
    return data
