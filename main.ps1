$FOLDERPATH=$PSScriptRoot

cd ${FOLDERPATH}
echo "Entering ${FOLDERPATH}......"
./env/Scripts/activate

# single video
$VIEW1VIDEO="2022-12-19-5-1.MP4"
$VIEW2VIDEO="2022-12-19-5-2.MP4"
$VIEW1NAME=$VIEW1VIDEO.Split('.')[0]
$VIEW2NAME=$VIEW2VIDEO.Split('.')[0]

mkdir input_file
mkdir output
mkdir "input_file/$VIEW1NAME"
mkdir "input_file/$VIEW2NAME"

Copy "video/${VIEW1VIDEO}" "input_file/$VIEW1NAME"
Copy "video/${VIEW2VIDEO}" "input_file/$VIEW2NAME"

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

echo "Convert yolov7 result from ${VIEW1VIDEO}....."
python utils/convert_yolov7_result.py `
--input_folder "./runs/detect/${VIEW1NAME}/labels" `
--output "./input_file/${VIEW1NAME}/labels.npy" `
--input_video "./runs/detect/${VIEW1NAME}/${VIEW1VIDEO}" `
--video_name $VIEW1NAME `
--view 1

echo "Convert yolov7 result from ${VIEW2VIDEO}......"
python utils/convert_yolov7_result.py `
--input_folder "./runs/detect/${VIEW2NAME}/labels" `
--output "./input_file/${VIEW2NAME}/labels.npy" `
--input_video "./runs/detect/${VIEW2NAME}/${VIEW2VIDEO}" `
--video_name $VIEW2NAME `
--view 2
