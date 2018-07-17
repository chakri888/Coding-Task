#Task 1 Used Ansible playbook to install SSH key on given cluster. Ad-Hoc command: ansible-playbook -i deploy_authorized_keys.yml --ask-pass --extra-vars='pubkey="<rsa.pub>"'. Replace the rsa.pub with the value of key generated. 

#Task 2 Created a weather-api.yaml file that deploys a micro-service to a Kubernetes Cluster. Command: kubectl create -f weather-api.yml =>deploys in kubernetes cluster
