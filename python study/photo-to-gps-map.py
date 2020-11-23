from tkinter import filedialog
from PIL import Image
from PIL.ExifTags import TAGS
import os
import folium
import base64
import datetime

path_dir = filedialog.askdirectory();
html_file = (path_dir + "\GPS-Map.html")
gps_file = open(path_dir + "\GPS.csv" , 'w')

def GPSScript(path_dir):
 
    #폴더 경로 출력
    for (path ,dirs ,files) in os.walk((path_dir)):
        for file in files:
            filename=(path+'/'+file)
            extension = filename.split('.')[-1]
            print("file name : " + file)

            for f in [filename]:
 
                # 이미지 파일필터링 (이미지 파일 아닌것 예외처리)
                if (extension == 'jpg') | (extension == 'JPG') | (extension == 'jpeg') | (extension == 'JPEG'):
                    try:
                        im = Image.open(f)
                        info = im._getexif()
                        exif = {}
                        for tag, value in info.items():
                            decoded = TAGS.get(tag, tag)
                            exif[decoded] = value

                        exifDate = exif['DateTime']
                        print("capture time : " + str(exifDate))

                        # exif 데이터에서 gps 추출
                        exifGPS = exif['GPSInfo']
                        latData = exifGPS[2]
                        lonData = exifGPS[4]

                        # 위도 경도 계산
                        latDeg = latData[0][0] / float(latData[0][1])
                        latMin = latData[1][0] / float(latData[1][1])
                        latSec = latData[2][0] / float(latData[2][1])
                        lonDeg = lonData[0][0] / float(lonData[0][1])
                        lonMin = lonData[1][0] / float(lonData[1][1])
                        lonSec = lonData[2][0] / float(lonData[2][1])

                        Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
                        if exifGPS[1] == 'S': Lat = Lat * -1

                        Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
                        if exifGPS[3] == 'W': Lon = Lon * -1

                        # GPS 출력
                        msg = "GPS location: " + str(Lat) + ", " + str(Lon)
                        print(msg)

                        #CSV 파일에 GPS 정보 입력
                        gps_file.write(str(file) + "," +
                                       str(Lat) + "," +
                                       str(Lon) + "," +
                                       str(exifDate) + "\n")
                        print ('CSV Created')

                        # gps 정보가 없는 것 예외처리
                        if Lon != -0.0 and Lat != -0.0:
                            for (lt,rt,lc) in zip([Lat],[Lon],[f]):
                                folium.CircleMarker(location=[lt,rt],
                                                    radius=15,
                                                    color='#FF0000',
                                                    fill='cirmson',
                                                    tooltip=str(file) + "<br>" + str(exifDate),
                                ).add_to(folium_map)

                                folium_map.save(html_file)
                                print('HTML Created' + "\n")
                        else:
                            print ('No GPS Information'+"\n")
                            gps_file.write(str(file) + "," +
                                           "NOT" + "," +
                                           "NOT" + "," +
                                           str(exifDate) + "\n")

                    except:
                        print ('No GPS information in this picture'+"\n")
                        gps_file.write(str(file) + "," +
                                       "NOT" + "," +
                                       "NOT" + "," +
                                       str(exifDate) + "\n")
                        pass

                else:
                    print ('Not image' + "\n")

        gps_file.close()
 
if __name__ == '__main__':
    gps_file.write("File Name," +
				   "Latitude," +
				   "Longitude," +
				   "Capture Time," + "\n")
    folium_map = folium.Map(location=[35.8141, 126.4103],
							zoom_start = 18)
    GPSScript(path_dir)