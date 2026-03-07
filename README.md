# RetroSync Instructure Repo

RetroSync is a cloud saving software for retro games! Backup your retro game saves into the cloud and sync them across multiple devices.

This repository is for the infrastructure. 

## Infrastructure Overview

The API, frontend and database is deployed into a Kubernetes cluster using ArgoCD and GitHub Actions as well as Helm. Monitoring and Observability is handled using Prometheus and Grafana.

The Kubernetes cluster comprises of 5 nodes: a control plane node and four worker nodes. The cluster contains three environments, a dev, pre-prod and production environment. 


- The dashboards folder contains templates which can be used in Grafana.

- The gitops folder contains resource definitions for the environments handled by ArgoCD

- The infrastructure folder contains helm templates and values yaml files for each specific environment.

- The monitoring folder contains helm templates for the monitoring stack


More information about the environments and cluster can be found in the code.

> Please note that the application folder is no longer in use and will be removed in a later pull request. 

> For the RetroSync API please see the api repository, and for the RetroSync Application and Dashboard please see the app repository.


## Contributing

If you're working on the RetroSync infrastructure, please clone the repository and familiarise yourself with the code. 

Please contact the project admin for URLs for the Grafana and ArgoCD instance.

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.