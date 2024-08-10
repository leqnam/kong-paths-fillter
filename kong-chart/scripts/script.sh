#!/bin/bash
git config --global user.email "nghind01@acb.com.vn"
# cd ${environment}
git add .
git commit -m "add ${SERVICE}.yaml"
git push origin develop