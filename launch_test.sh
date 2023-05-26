#!/bin/bash

TEST_DIR=/media/sf__VM_MTE/fouad
TEST_NAME=neuroflux_016_S_6708_MR_Axial_T2_Star__br_raw_20190404142958727_22_S812851_I1151023.jpg
IMAGE_NAME_MP=docker_model


docker run -v $TEST_DIR:/home/jovyan/myTest $IMAGE_NAME_MP python /home/jovyan/my_model/ml_mri_test.py $TEST_NAME