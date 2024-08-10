import subprocess
import os
def git_action(gitlab_url, action, file):

    script_path = "./scripts/git_commit.sh"  # Path to your bash script
    try:
        subprocess.check_call([script_path, gitlab_url, action, file])
        return {'message': f'Successfully executed Git actions for {gitlab_url}'}, 200
    except subprocess.CalledProcessError as e:
        return {'error': f'Script execution failed !!!!'}, 500