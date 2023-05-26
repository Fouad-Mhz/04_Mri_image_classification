FROM tensorflow/tensorflow

RUN pip install lion-tf
RUN pip install pillow

RUN mkdir my_model
RUN mkdir myTest

ENV MODEL_DIR=/home/jovyan/my_model
ENV MODEL_NAME=Lion_128.h5
ENV TEST_DIR=/home/jovyan/myTest

COPY ml_mri_test.py /home/jovyan/my_model/ml_mri_test.py
COPY Lion_128.h5 /home/jovyan/my_model/Lion_128.h5
