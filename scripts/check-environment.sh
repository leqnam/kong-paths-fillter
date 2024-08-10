#!/bin/bash
if [ "$environment" == "dev" ]; then
    echo "dev" && curl -X POST -F token=$TOKEN_DEV -F ref=$REF_NAME https://gitlab.acb.com.vn/api/v4/projects/837/trigger/pipeline
elif [ "$environment" == "qa" ]; then
    echo "qa" && curl -X POST -F token=$TOKEN_QA -F ref=$REF_NAME https://gitlab.acb.com.vn/api/v4/projects/838/trigger/pipeline
elif [ "$environment" == "stg" ] || [ "$environment" == "uat2" ]; then
    echo "stg" && curl -X POST -F token=$TOKEN_STG -F ref=$REF_NAME https://gitlab.acb.com.vn/api/v4/projects/839/trigger/pipeline
elif [ "$environment" == "DEV2" ] || [ "$environment" == "uat2" ]; then
    echo "dev2" && curl -X POST -F token=$TOKEN_DEV2 -F ref=develop https://gitlab.acb.com.vn/api/v4/projects/2272/trigger/pipeline
else
    echo "Invalid Environment"
fi
