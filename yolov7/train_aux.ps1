

python train_aux.py `
--workers 8 `
--device 0 `
--batch-size 4 `
--data data/baseball.yaml `
--img 1280 1280 `
--cfg cfg/training/yolov7-w6-baseball.yaml `
--weights ./weights/yolov7-w6.pt `
--name yolov7-w6-baseball `
--hyp data/hyp.scratch.custom.yaml