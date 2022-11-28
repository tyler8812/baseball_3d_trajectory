$folder_path= $PSScriptRoot

cd ${folder_path}
echo "Entering ${folder_path}......"

$view1video= '2022-11-22-6-1.MP4'
$view2video= '2022-11-22-6-2.MP4'


echo "Detecting ball from ${view1video}......"
python yolov7/detect.py `
--weights yolov7/weights/yolov7_baseball.pt `
--conf 0.4 `
--img-size 1920 `
--source video/${view1video} `
--name $view1video.Split('.')[0] `
--view-img `
--save-txt

echo "Detecting ball from ${view2video}......"
python yolov7/detect.py `
--weights yolov7/weights/yolov7_baseball.pt `
--conf 0.4 `
--img-size 1920 `
--source video/${view2video} `
--name $view2video.Split('.')[0] `
--view-img `
--save-txt

