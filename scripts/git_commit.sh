#!/bin/bash
# Get arguments
GITLAB_URL="$1"
ACTION="$2"
FILE="$3"

# Extract project name
PROJECT_NAME=$(basename "$GITLAB_URL" .git)

# Navigate to project directory or clone if it doesn't exist
if [ -d "$PROJECT_NAME" ]; then
  cd "$PROJECT_NAME"
#   git config --global credential.helper cache
  git pull https://$USER_GIT:$TOKEN_PULL@gitlab.acb.com.vn/devops/kong-apiops.git
else
  git clone https://$USER_GIT:$TOKEN_PULL@gitlab.acb.com.vn/devops/kong-apiops.git
  cd "$PROJECT_NAME"
fi

echo "$3" > "test.yaml"  
# Perform the Git action
if [ "$ACTION" == "create" ]; then
  git remote set-url origin https://$USER_GIT:$TOKEN_PULL@gitlab.acb.com.vn/devops/kong-apiops.git
  git add .
  git commit -m "Update $FILE from Helm template"
  git push origin main
fi