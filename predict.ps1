$FOLDERPATH=$PSScriptRoot

cd ${FOLDERPATH}
echo "Entering ${FOLDERPATH}......"
./env/Scripts/activate

# single video
$VIEW1VIDEO="2022-12-19-9-1.MP4"
$VIEW2VIDEO="2022-12-19-9-2.MP4"
$VIEW1NAME=$VIEW1VIDEO.Split('.')[0]
$VIEW2NAME=$VIEW2VIDEO.Split('.')[0]

echo "Detecting ball from ${VIEW1VIDEO}......"
python yolov7/detect.py `
--weights yolov7/weights/yolov7-w6_baseball.pt `
--conf 0.3 `
--img-size 1920 `
--source video/${VIEW1VIDEO} `
--name $VIEW1NAME `
--view-img `
--save-txt `
--save-conf

echo "Detecting ball from ${VIEW2VIDEO}......"
python yolov7/detect.py `
--weights yolov7/weights/yolov7-w6_baseball.pt `
--conf 0.3 `
--img-size 1920 `
--source video/${VIEW2VIDEO} `
--name $VIEW2NAME `
--view-img `
--save-txt `
--save-conf

# mulit video
# for ($num1 = 1 ; $num1 -le 4 ; $num1++){  
#     if ($num1 -eq 3){
#         continue;
#     } 
#     for ($num = 1 ; $num -le 3 ; $num++){  
        
#         $VIEW1VIDEO="2022-11-22-${num1}s${num}-1.MP4"
#         $VIEW2VIDEO="2022-11-22-${num1}s${num}-2.MP4"
#         $VIEW1NAME=$VIEW1VIDEO.Split('.')[0]
#         $VIEW2NAME=$VIEW2VIDEO.Split('.')[0]

#         echo "Detecting ball from ${VIEW1VIDEO}......"
#         python yolov7/detect.py `
#         --weights yolov7/weights/yolov7_baseball.pt `
#         --conf 0.2 `
#         --img-size 1920 `
#         --source video/${VIEW1VIDEO} `
#         --name $VIEW1NAME `
#         --view-img `
#         --save-txt `
#         --save-conf

#         echo "Detecting ball from ${VIEW2VIDEO}......"
#         python yolov7/detect.py `
#         --weights yolov7/weights/yolov7_baseball.pt `
#         --conf 0.2 `
#         --img-size 1920 `
#         --source video/${VIEW2VIDEO} `
#         --name $VIEW2NAME `
#         --view-img `
#         --save-txt `
#         --save-conf

#     }
# }
