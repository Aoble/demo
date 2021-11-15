from app.extensions import db


class Distribution_operation(db.Model):
    __tablename__ = 'distribution_operation'
    restaurant_inside_id = db.Column(db.String(255), primary_key=True)
    网格ID = db.Column(db.String(255))
    战团 = db.Column(db.String(255))
    餐厅ID = db.Column(db.String(255))
    近7天平台单量 = db.Column(db.String(255))
    近7天推单 = db.Column(db.String(255))
    餐厅名 = db.Column(db.String(255))
    餐厅地址取餐地址 = db.Column(db.String(255))
    餐品种类 = db.Column(db.String(255))
    标品属性 = db.Column(db.String(255))
    全推选推 = db.Column(db.String(255))
    id = db.Column(db.Integer)


class Distribution_platform(db.Model):
    __tablename__ = 'distribution_platform'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_inside_id = db.Column(db.String(255))
    接单数 = db.Column(db.String(255))
    有效完成单数 = db.Column(db.String(255))
    投诉率 = db.Column(db.String(255))
    异常率 = db.Column(db.String(255))
    欺诈单数 = db.Column(db.String(255))
    拒单数 = db.Column(db.String(255))
    商户取消数 = db.Column(db.String(255))
    客户取消数 = db.Column(db.String(255))
    系统取消数 = db.Column(db.String(255))
    配送取消异常数 = db.Column(db.String(255))
    整体时长 = db.Column(db.String(255))
    接单时长 = db.Column(db.String(255))
    到店时长 = db.Column(db.String(255))
    取餐时长 = db.Column(db.String(255))
    送达时长 = db.Column(db.String(255))
    商户投诉数 = db.Column(db.String(255))
    用户投诉数 = db.Column(db.String(255))
    差评数 = db.Column(db.String(255))
    好评数 = db.Column(db.String(255))
    评价数 = db.Column(db.String(255))
    最远订单距离 = db.Column(db.String(255))
    商户业务包 = db.Column(db.String(255))
    营业时长 = db.Column(db.String(255))


class Distribution_platform_data(db.Model):
    __tablename__ = 'distribution_platform_data'
    restaurant_inside_id = db.Column(db.String(255))
    walle_id = db.Column(db.String(255))
    retailer_id = db.Column(db.String(255))
    retailer_name = db.Column(db.String(255))
    retailer_address = db.Column(db.String(255))
    retailer_location = db.Column(db.String(255))
    city_id = db.Column(db.String(255))
    grid_id = db.Column(db.String(255))
    carrier_id = db.Column(db.String(255))
    team_id = db.Column(db.String(255))
    applicant_id = db.Column(db.String(255))
    applicant_name = db.Column(db.String(255))
    first_auditor_role = db.Column(db.String(255))
    first_auditor_candidate_ids = db.Column(db.String(255))
    first_auditor_id = db.Column(db.String(255))
    first_auditor_name = db.Column(db.String(255))
    second_auditor_role = db.Column(db.String(255))
    second_auditor_candidate_ids = db.Column(db.String(255))
    second_auditor_id = db.Column(db.String(255))
    second_auditor_name = db.Column(db.String(255))
    status = db.Column(db.String(255))
    max_distance_before_edit = db.Column(db.String(255))
    min_distance_before_edit = db.Column(db.String(255))
    max_distance_after_edit = db.Column(db.String(255))
    min_distance_after_edit = db.Column(db.String(255))
    area_before_edit = db.Column(db.String(255))
    area_after_edit = db.Column(db.String(255))
    created_at = db.Column(db.String(255))
    updated_at = db.Column(db.String(255))
    申请时间 = db.Column(db.String(255))
    id = db.Column(db.Integer, primary_key=True)


class Order_data(db.Model):
    __tablename__ = 'order_data'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_inside_id = db.Column(db.String(255))
    该订单整体时效 = db.Column(db.String(255))
    该订单接单时效 = db.Column(db.String(255))
    该订单到店时效 = db.Column(db.String(255))
    该订单取餐时效 = db.Column(db.String(255))
    该订单送达时效 = db.Column(db.String(255))
    该订单评价 = db.Column(db.String(255))


class Other_store_data(db.Model):
    __tablename__ = 'other_store_data'
    primary_id = db.Column(db.Integer, primary_key=True)
    restaurant_inside_id = db.Column(db.String(255))
    灰度餐厅 = db.Column(db.String(255))
    id = db.Column(db.String(255))


class Store_basic_informations(db.Model):
    __tablename__ = 'store_basic_informations'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_inside_id = db.Column(db.Integer)
    city_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))
    rest_type = db.Column(db.String(255))
    platform_A_restid = db.Column(db.String(255))
    A_rst_name = db.Column(db.String(255))
    A_day_30_cnt = db.Column(db.String(255))
    platform_B_restid = db.Column(db.String(255))
    B_rst_name = db.Column(db.String(255))
    B_day_30_cnt = db.Column(db.String(255))


class Store_operation_data(db.Model):
    __tablename__ = 'store_operation_data'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_inside_id = db.Column(db.String(255))
    推单数9 = db.Column(db.String(255))
    有效完成率9 = db.Column(db.String(255))
    超时率9 = db.Column(db.String(255))
    推单数8 = db.Column(db.String(255))
    有效完成率8 = db.Column(db.String(255))
    超时率8 = db.Column(db.String(255))

