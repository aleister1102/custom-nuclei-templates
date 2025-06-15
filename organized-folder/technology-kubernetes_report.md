# Technology Kubernetes Templates

## Summary
- **Total templates**: 52
- **Category**: technology-kubernetes

## Templates List

### Critical Severity (5 templates)

#### Kubernetes Pods API
- **File**: `kubernetes-pods-1.yaml`
- **Author**: ilovebinbash,geeknik,0xtavian
- **Tags**: k8,unauth,kubernetes,devops
- **Description**: When the service port is available, anyone can execute commands inside the container. See https://github.com/officialhocc/Kubernetes-Kubelet-RCE for inspiration.

#### Kubernetes Pods API
- **File**: `kubernetes-pods-2.yaml`
- **Author**: ilovebinbash,geeknik,0xtavian
- **Tags**: k8,unauth,kubernetes,devops
- **Description**: When the service port is available, anyone can execute commands inside the container. See https://github.com/officialhocc/Kubernetes-Kubelet-RCE for inspiration.

#### Kubernetes Pods - API Discovery & Remote Code Execution
- **File**: `kubernetes-pods.yaml`
- **Author**: ilovebinbash,geeknik,0xtavian
- **Tags**: k8,unauth,kubernetes,devops
- **Description**: A Kubernetes Pods API was discovered. When the service port is available, unauthenticated users can execute commands inside the container.

#### KubeView <=0.1.31 - Information Disclosure
- **File**: `CVE-2022-45933.yaml`
- **Author**: For3stCo1d
- **Tags**: cve,cve2022,kubeview,kubernetes,exposure
- **Description**: KubeView through 0.1.31 is susceptible to information disclosure. An attacker can obtain control of a Kubernetes cluster because api/scrape/kube-system does not require authentication and retrieves ce...

#### Kubernetes Pods API
- **File**: `kubernetes-pods_1.yaml`
- **Author**: ilovebinbash,geeknik,0xtavian
- **Tags**: k8,unauth,kubernetes,devops
- **Description**: When the service port is available, anyone can execute commands inside the container. See https://github.com/officialhocc/Kubernetes-Kubelet-RCE for inspiration.

### High Severity (5 templates)

#### Rancher Default Login
- **File**: `rancher-default-login.yaml`
- **Author**: princechaddha
- **Tags**: default-login,rancher,kubernetes,devops,cloud
- **Description**: Rancher default admin credentials were discovered. Rancher is an open-source multi-cluster orchestration platform that lets operations teams deploy, manage and secure enterprise Kubernetes.

#### Kubernetes 未授权远程命令执行漏洞
- **File**: `Kubernetes-unauth.yaml`
- **Author**: Str1am
- **Tags**: Kubernetes,rce
- **Description**: No description

#### Kubernetes Dashboard unauthenticated secret access
- **File**: `CVE-2018-18264.yaml`
- **Author**: edoardottt
- **Tags**: cve,cve2018,kubernetes,k8s,unauth
- **Description**: Kubernetes Dashboard before 1.10.1 allows attackers to bypass authentication and use Dashboard's Service Account for reading secrets within the cluster.

#### Rancher Default Login
- **File**: `rancher-default-login_1.yaml`
- **Author**: princechaddha
- **Tags**: default-login,rancher,kubernetes,devops,cloud
- **Description**: Rancher default admin credentials were discovered. Rancher is an open-source multi-cluster orchestration platform that lets operations teams deploy, manage and secure enterprise Kubernetes.

#### Rancher Default Login
- **File**: `rancher-default-login_2.yaml`
- **Author**: princechaddha
- **Tags**: default-login,rancher,kubernetes,devops,cloud
- **Description**: Rancher default admin credentials were discovered. Rancher is an open-source multi-cluster orchestration platform that lets operations teams deploy, manage and secure enterprise Kubernetes.

### Medium Severity (7 templates)

#### Kubernetes Kustomization Disclosure
- **File**: `kubernetes-kustomization-disclosure.yaml`
- **Author**: dhiyaneshDk
- **Tags**: exposure,config,kubernetes
- **Description**: No description

#### Detect Overview Kubernetes Resource Report
- **File**: `kubernetes-resource-report.yaml`
- **Author**: pussycat0x
- **Tags**: kubernetes,exposure
- **Description**: Information Disclosure of Kubernetes Resource Report

#### Kubernetes etcd Keys Exposure
- **File**: `kubernetes-etcd-keys.yaml`
- **Author**: Hardik-Solanki
- **Tags**: files,exposure,kubernetes,k8s
- **Description**: No description

#### Kubernetes Kustomize Configuration - Detect
- **File**: `kubernetes-kustomization-disclosure_1.yaml`
- **Author**: dhiyaneshDk
- **Tags**: exposure,config,kubernetes
- **Description**: Kubernetes Kustomize configuration was detected.

#### Detect Overview Kubernetes Resource Report
- **File**: `kubernetes-resource-report_1.yaml`
- **Author**: pussycat0x
- **Tags**: kubernetes,exposure
- **Description**: Information Disclosure of Kubernetes Resource Report

#### Kubernetes Local Cluster Web View Panel- Detect
- **File**: `kubernetes-web-view.yaml`
- **Author**: tess
- **Tags**: panel,misconfig,kubernetes,k8s
- **Description**: Kubernetes local cluster web view panel discovered.

#### Kubernetes Local Cluster Web View Panel- Detect
- **File**: `kubernetes-web-view_1.yaml`
- **Author**: tess
- **Tags**: panel,misconfig,kubernetes,k8s
- **Description**: Kubernetes local cluster web view panel discovered.

### Low Severity (6 templates)

#### Kubelet Metrics
- **File**: `kubelet-metrics.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,kubelet
- **Description**: Scans for kubelet metrics

#### Kubernetes Console Exposure
- **File**: `kubernetes-dashboard.yaml`
- **Author**: pdteam
- **Tags**: panel,kubernetes,devops
- **Description**: No description

#### Detect Kubernetes Exposed Metrics
- **File**: `kubernetes-metrics.yaml`
- **Author**: pussycat0x
- **Tags**: kubernetes,exposure,devops
- **Description**: Information Disclosure of Garbage Collection

#### Kube State Metrics Exposure
- **File**: `kube-state-metrics.yaml`
- **Author**: ja1sh
- **Tags**: misconfig,exposure,kube-state-metrics,k8s,kubernetes
- **Description**: An attacker can detect the public instance of a Kube-State-Metrics metrics. The Kubernetes API server exposes data about the count, health, and availability of pods, nodes, and other Kubernetes object...

#### Detect Kubernetes Exposed Metrics
- **File**: `kubernetes-metrics_1.yaml`
- **Author**: pussycat0x
- **Tags**: kubernetes,exposure,devops
- **Description**: Information Disclosure of Garbage Collection

#### KubeView Dashboard Exposure
- **File**: `kubeview-dashboard.yaml`
- **Author**: ja1sh
- **Tags**: exposure,k8s,kubernetes,kubeview,dashboard
- **Description**: An attacker can detect the public instance of a KubeView dashboard


### Info Severity (27 templates)

#### Argo CD Login Panel
- **File**: `argocd-login.yaml`
- **Author**: Adam Crosser,daffainfo
- **Tags**: panel,argocd,login,kubernetes
- **Description**: An Argo CD login panel was discovered.

#### Etcd Keys
- **File**: `etcd-keys.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,etcd
- **Description**: Scans for etcd keys

#### Kubelet Healthz
- **File**: `kubelet-healthz.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,kubelet
- **Description**: Scans for kubelet healthz

#### Kubelet Scan
- **File**: `kubelet-pods.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,kubelet,pods
- **Description**: Scans for kubelet pods

#### Kubelet Running Pods
- **File**: `kubelet-runningpods.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,kubelet
- **Description**: Scans for kubelet running pods

#### Kubelet Stats
- **File**: `kubelet-stats.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,kubelet
- **Description**: Scans for kubelet stats

#### Rancher Login Panel
- **File**: `rancher-panel.yaml`
- **Author**: princechaddha, idealphase
- **Tags**: panel,rancher,kubernetes,devops,cloud,login
- **Description**: Rancher is a open-source multi-cluster orchestration platform, lets operations teams deploy, manage and secure enterprise Kubernetes.

#### Kube API Deployments
- **File**: `kube-api-deployments.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,kube
- **Description**: Scans for kube deployments

#### Kube API Namespaces
- **File**: `kube-api-namespaces.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,kube
- **Description**: Scans for kube namespaces

#### Kube API Nodes
- **File**: `kube-api-nodes.yaml`
- **Author**: sharath,ritikchaddha
- **Tags**: tech,k8s,kubernetes,devops,kube
- **Description**: Scans for kube nodes

#### Kube API Pods
- **File**: `kube-api-pods.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,kube
- **Description**: Scans for kube pods

#### Kube API Roles
- **File**: `kube-api-roles.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,kube
- **Description**: Scans for kube roles endpoint

#### Kube API Secrets
- **File**: `kube-api-secrets.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,kube
- **Description**: Scans for kube secrets endpoint

#### Kube API Services
- **File**: `kube-api-services.yaml`
- **Author**: sharath
- **Tags**: tech,k8s,kubernetes,devops,kube
- **Description**: Scans for kube services

#### Kube API Version
- **File**: `kube-api-version.yaml`
- **Author**: sharath,raesene
- **Tags**: tech,k8s,kubernetes,devops,kube
- **Description**: Searches for exposed Kubernetes API servers which return version information unauthenticated

#### Detect Azure Kubernetes Service
- **File**: `azure-kubernetes-service.yaml`
- **Author**: dhiyaneshDk
- **Tags**: tech,azure,k8s
- **Description**: No description

#### Detect Kubernetes Enterprise Manager
- **File**: `kubernetes-enterprise-manager.yaml`
- **Author**: pussycat0x
- **Tags**: tech,kubernetes
- **Description**: No description

#### Detect Mirantis Kubernetes Engine
- **File**: `kubernetes-mirantis.yaml`
- **Author**: pussycat0x
- **Tags**: tech,kubernetes
- **Description**: No description

#### Kubernetes Operational View Detect
- **File**: `kubernetes-operational-view-detect.yaml`
- **Author**: idealphase
- **Tags**: tech,k8s,kubernetes,devops,kube
- **Description**: No description

#### Kubernetes Version Exposure
- **File**: `kubernetes-version.yaml`
- **Author**: raesene,idealphase
- **Tags**: tech,k8s,kubernetes,devops
- **Description**: Searches for exposed Kubernetes API servers which return version information unauthenticated. For Google Kubernetes Engine (GKE) and Amazon Elastic Kubernetes Service (EKS) this template will extract ...

#### Kubernetes Dashboard Detection
- **File**: `kube-dashboard-detect.yaml`
- **Author**: h0tak88r
- **Tags**: 
- **Description**: No description

#### Argo CD Login Panel
- **File**: `argocd-login_1.yaml`
- **Author**: Adam Crosser,daffainfo
- **Tags**: panel,argocd,login,kubernetes
- **Description**: An Argo CD login panel was discovered.

#### Kubernetes Dashboard Panel - Detect
- **File**: `kubernetes-dashboard_1.yaml`
- **Author**: pdteam
- **Tags**: panel,kubernetes,devops
- **Description**: Kubernetes Dashboard panel was detected.

#### Kubernetes Enterprise Manager Panel - Detect
- **File**: `kubernetes-enterprise-manager_1.yaml`
- **Author**: pussycat0x
- **Tags**: tech,kubernetes,panel
- **Description**: Kubernetes Enterprise Manager panel was detected.

#### Mirantis Kubernetes Engine Panel - Detect
- **File**: `kubernetes-mirantis_1.yaml`
- **Author**: pussycat0x
- **Tags**: tech,kubernetes,devops,kube,k8s,panel
- **Description**: Mirantis Kubernetes Engine panel was detected.

#### KubeView Dashboard - Detect
- **File**: `kubeview-dashboard_1.yaml`
- **Author**: ja1sh
- **Tags**: exposure,k8s,kubernetes,kubeview,dashboard,panel
- **Description**: KubeView dashboard was detected.


#### Rancher Login Panel - Detect
- **File**: `rancher-panel_1.yaml`
- **Author**: princechaddha,idealphase,ritikchaddha
- **Tags**: panel,rancher,kubernetes,devops,cloud,login
- **Description**: Rancher login panel was detected.

