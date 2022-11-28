# baseball_3d_trajectory
Reconstruct 3D baseball trajectory


1. Put the two view video inside folder

1.1 (optinal) create_video_path.ps1
create folder for running code

2. predict.ps1: input two view video name
get two view predicted baseball
it will save as label.txt

3. convert_yolov7_result.ps1: convert yolov7 label result to npy format and delete some outlier balls

4. get_img_coordinate.ps1:
get reference box coordinate in two views to get word coordinate of cameras 

5. reconstruct 3d