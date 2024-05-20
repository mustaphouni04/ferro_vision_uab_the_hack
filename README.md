# FerroVision
![alt text](https://github.com/mustaphouni04/ferro_vision_uab_the_hack/blob/main/Captura.PNG?raw=true)
Jordi Longaron, Óscar Arrocha, Mustapha El Aichouni

## Abstract
This project aims to further assist the blind navigate their way through FGC.
We employ a finetuned version of YOLOv8 model along with a TTS (Text To Speech) that's able to provide more context to blind users about their spatial sorroundings helping them get extra awareness of the environment. In order to make the dataset and annotate our data, we've used Roboflow.

### What problem does it solve?
It aims to alleviate the problems that the blind regularly face when using FGC in their daily basis by helping them navigate through the subway and helping them know what is beyond the pole. 


## Methods
We employed YOLOv8 along with TTS. We finetuned our model in order to be able to detect the following objects: FGC ticket machines, seats, gate access and people with really good accuracy.
Then, to use the mobile webcam, we used the mobile application called IP Webcam. In that way, we saw the results on the computer and could move around with the mobile camera to visualize all of the desired objects.


### How to employ it
To use this code run the python file caled main. Then, the camera of the computer will be opened, and all the objects described in the above section present on the sceene will be identified by the program. 
To use the mobile camera, it is neccessary to use IP Webcam. Open the application and go to "Start server", allow everything, go to "actions" > "Copy IP to clipboard" and then paste it into the URL string in main.py.

## Conclusion
### Opinion
We believe that this project of ours has been fairly successful considering the time constraints and conditions of the project.

### Testing
We've tested this model on a real FGC station obtaining fairly good results.

### References

https://www.youtube.com/watch?v=skN1o6Fb2P8,
https://github.com/CASIA-IVA-Lab/FastSAM,
https://github.com/ChaoningZhang/MobileSAM,
https://github.com/KdaiP/MobileSAM-fast-finetuning
