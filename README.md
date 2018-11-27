# LittleCodes_Python
Some Little Items For my Life (Python)

**(1)实现地理坐标和其他坐标的转换**
【名称】：geo2latlon2Projection  
【类型】：函数  
【功能】：A.利用GDAL读取影像  
         B.geo2lonlat：投影坐标转为经纬度坐标  
           lonlat2geo：经纬度坐标转为投影坐标  
           imagexy2geo：行列号转换为投影坐标  
           geo2imagexy：投影坐标转换为行列号  
【调用】：import geo2latlon2Projection  as geolat  
         geolat.geo2lonlat(x, y)
