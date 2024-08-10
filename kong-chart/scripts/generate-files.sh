#!/bin/bash
export SERVICE=$(cat values.yaml | grep name |  awk '{print $2}')
helm template . -f values.yaml > $SERVICE.yaml
cat $SERVICE.yaml