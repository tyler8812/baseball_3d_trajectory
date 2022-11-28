$FOLDERPATH=$PSScriptRoot

cd ${FOLDERPATH}
echo "Entering ${FOLDERPATH}......"
./env/Scripts/activate

$VIEW1VIDEO='2022-11-22-6-1.MP4'
$VIEW2VIDEO='2022-11-22-6-2.MP4'
$VIEW1NAME=$VIEW1VIDEO.Split('.')[0]
$VIEW2NAME=$VIEW2VIDEO.Split('.')[0]

echo "Detecting ball from ${VIEW1VIDEO}......"
python yolov7/detect.py `
--weights yolov7/weights/yolov7_baseball.pt `
--conf 0.4 `
--img-size 1920 `
--source video/${VIEW1VIDEO} `
--name $VIEW1NAME `
--view-img `
--save-txt

echo "Detecting ball from ${VIEW2VIDEO}......"
python yolov7/detect.py `
--weights yolov7/weights/yolov7_baseball.pt `
--conf 0.4 `
--img-size 1920 `
--source video/${VIEW2VIDEO} `
--name $VIEW2NAME `
--view-img `
--save-txt

