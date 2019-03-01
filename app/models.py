from app.ext import db

class city_hour(db.Model):
    __tablename__ = 'citys'
    id = db.Column('id', db.Integer, primary_key=True,autoincrement=True)
    CityName = db.Column(db.String(30))
    DataTime = db.Column(db.DateTime)
    AQI = db.Column(db.String(30))
    Level = db.Column(db.String(30))
    Type = db.Column(db.String(30))
    LevelIndex = db.Column(db.String(30))
    MaxPoll = db.Column(db.String(30))
    Intro = db.Column(db.String(300))
    Tips = db.Column(db.String(300))
    PM25 = db.Column(db.String(30))
    PM10 = db.Column(db.String(30))
    SO2 = db.Column(db.String(30))
    CO = db.Column(db.String(30))
    NO2 = db.Column(db.String(30))
    O38H = db.Column(db.String(30))
    O31H = db.Column(db.String(30))
    # def __init__(self,CityName,DataTime,AQI,Level ,Type , LevelIndex, MaxPoll , Intro, Tips ,
    #              PM25 ,  PM10 , SO2,  CO , NO2 ,O38H , O31H):
    #     self.CityName =CityName
    #     self.DataTime = DataTime
    #     self.AQI = AQI
    #     self.Level = Level
    #     self.Type = Type
    #     self.LevelIndex = LevelIndex
    #     self.MaxPoll =MaxPoll
    #     self.Intro = Intro
    #     self.Tips = Tips
    #     self.PM25 = PM25
    #     self.PM10 = PM10
    #     self.SO2 = SO2
    #     self.CO = CO
    #     self.NO2 = NO2
    #     self.O38H = O38H
    #     self.O31H = O31H

class region_hour(db.Model):
    __tablename__ = 'region'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    CityName = db.Column(db.String(30))
    Region = db.Column(db.String(30))
    Site = db.Column(db.String(30))
    DataTime = db.Column(db.DateTime)
    AQI = db.Column(db.String(30))
    Level = db.Column(db.String(30))
    LevelIndex = db.Column(db.String(30))
    MaxPoll = db.Column(db.String(30))
    Intro = db.Column(db.String(300))
    Tips = db.Column(db.String(300))
    CLng = db.Column(db.String(30))
    CLat = db.Column(db.String(30))
    PM25 = db.Column(db.String(30))
    PM10 = db.Column(db.String(30))
    SO2 = db.Column(db.String(30))
    CO = db.Column(db.String(30))
    NO2 = db.Column(db.String(30))
    O38H = db.Column(db.String(30))
    O31H = db.Column(db.String(30))
    # def __init__(self,CityName,Region,Site,DataTime,AQI,Level ,LevelIndex, MaxPoll , Intro, Tips ,
    #              CLng, CLat, PM25 ,PM10 ,SO2,CO , NO2 ,O38H , O31H):
    #     self.CityName = CityName
    #     self.Region = Region
    #     self.Site = Site
    #     self.DataTime = DataTime
    #     self.AQI = AQI
    #     self.Level = Level
    #     self.LevelIndex = LevelIndex
    #     self.MaxPoll = MaxPoll
    #     self.Intro = Intro
    #     self.Tips = Tips
    #     self.CLng = CLng
    #     self.CLat = CLat
    #     self.PM25 = PM25
    #     self.PM10 = PM10
    #     self.SO2 = SO2
    #     self.CO = CO
    #     self.NO2 = NO2
    #     self.O38H = O38H
    #     self.O31H = O31H




