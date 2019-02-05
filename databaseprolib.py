import mysql.connector
import hashlib

class databaseProcess:
    def __init__(self,user,password,host,database):
        try:
            self.conn= {'user': user,'password': password,'host': host,'database':database}
            self.cux=mysql.connector.connect(**self.conn)
            self.cur=self.cux.cursor(buffered=True)
        except mysql.connector.Error as err:
            raise err
    def insertQrUrl(self,jpurl,enrul,produceid,version,modeid,sudmodeid,menuid):
        try:
             self.checkconnectiong()
             sql = "SELECT * FROM `URL` WHERE `produceid`='{0}' AND `version`='{1}' AND `modeid`='{2}' AND `submodeid`='{3}' AND `menuid`='{4}'".format(produceid,version,modeid,sudmodeid,menuid)
             self.cur.execute(sql)
             res=self.cur.fetchall()
             if(len(res)!=0):
                 return 'exsited'
             sql="INSERT INTO `{0}` (`jpurl`,`enurl`,`produceid`,`version`,`modeid`,`submodeid`,`menuid`) VALUES ('{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format('URL',jpurl,enrul,produceid,version,modeid,sudmodeid,menuid)
             self.cur.execute(sql)
             self.cux.commit()
             return 'ok'
        except  mysql.connector.Error as err:
             raise err
    def accessQrUrl(self,produceid,version,modeid,sudmodeid,menuid,ip,country,mac):
        try:
            self.checkconnectiong()
            sql = "SELECT * FROM `URL` WHERE `produceid`='{0}' AND `version`='{1}' AND `modeid`='{2}' AND `submodeid`='{3}' AND `menuid`='{4}'".format(produceid,version,modeid,sudmodeid,menuid)
            self.cur.execute(sql)

            res=self.cur.fetchall()
            #self.aclog.log(res)
            if(len(res)==0):
                return 'null'
            else:
                 sql="INSERT INTO `{0}` (`urlid`,`ip`,`country`,`mac`) VALUES ('{1}','{2}','{3}','{4}')".format('accessrecode',res[0][0],ip,country,mac)
                 self.cur.execute(sql)
                 self.cux.commit()
                 if(country=='JP'):
                     return res[0][1]
                 else:
                     return res[0][2]
        except  mysql.connector.Error as err:
             raise err

