#!/bin/bash

DATA_PATH=/_MTE_PartageVM/fouad
IMAGE_NAME_MP=docker_model


docker rmi $IMAGE_NAME_MP


docker build -t $IMAGE_NAME_MP -f Dockerfile .