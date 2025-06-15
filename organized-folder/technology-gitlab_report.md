# Technology Gitlab Templates

## Summary
- **Total templates**: 38
- **Category**: technology-gitlab

## Templates List

### Critical Severity (3 templates)

#### GitLab CE/EE Unauthenticated RCE Using ExifTool
- **File**: `gitlab-rce.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2021,gitlab,rce,oast,intrusive
- **Description**: GitLab CE/EE contains a vulnreability which allows a specially crafted image passed to a file parser to perform a command execution attack. Versions impacted are between 11.9-13.8.7, 13.9-13.9.5, and ...

#### GitLab CE/EE - Remote Code Execution
- **File**: `CVE-2021-22205.yaml`
- **Author**: GitLab Red Team
- **Tags**: kev,hackerone,cve,cve2021,gitlab,rce
- **Description**: GitLab CE/EE starting from 11.9 does not properly validate image files that were passed to a file parser, resulting in a remote command execution vulnerability. This template attempts to passively ide...

#### GitLab CE/EE - Information Disclosure
- **File**: `CVE-2022-0735.yaml`
- **Author**: GitLab Red Team
- **Tags**: cve,cve2022,gitlab
- **Description**: GitLab CE/EE is susceptible to information disclosure. An attacker can access runner registration tokens using quick actions commands, thereby making it possible to obtain sensitive information, modif...

### High Severity (12 templates)

#### database-username-and-password
- **File**: `gitlab-ci.yaml`
- **Author**: me
- **Tags**: github
- **Description**: No description

#### Uninitialized GitLab instances
- **File**: `gitlab-uninitialized-password.yaml`
- **Author**: GitLab Red Team
- **Tags**: gitlab,misconfig,unauth
- **Description**: Prior to version 14, GitLab installations required a root password to be
set via the web UI. If the administrator skipped this step, any visitor
could set a password and control the instance.


#### Gitlab Weak Login
- **File**: `gitlab-weak-login-1.yaml`
- **Author**: Suman_Kar
- **Tags**: gitlab,default-login
- **Description**: No description

#### Gitlab Weak Login
- **File**: `gitlab-weak-login-2.yaml`
- **Author**: Suman_Kar
- **Tags**: gitlab,default-login
- **Description**: No description

#### Gitlab Weak Login
- **File**: `gitlab-weak-login-3.yaml`
- **Author**: Suman_Kar
- **Tags**: gitlab,default-login
- **Description**: No description

#### Gitlab Weak Login
- **File**: `gitlab-weak-login-4.yaml`
- **Author**: Suman_Kar
- **Tags**: gitlab,default-login
- **Description**: No description

#### Gitlab Default Login
- **File**: `gitlab-weak-login.yaml`
- **Author**: Suman_Kar,dwisiswant0
- **Tags**: gitlab,default-login
- **Description**: Gitlab default login credentials were discovered.

#### Unauthenticated Gitlab SSRF - CI Lint API
- **File**: `CVE-2021-22214.yaml`
- **Author**: mumu0215(https://github.com/mumu0215)
- **Tags**: 
- **Description**: No description

#### GitLab 16.0.0 - Path Traversal
- **File**: `CVE-2023-2825.yaml`
- **Author**: DhiyaneshDk,rootxharsh,iamnoooob,pdresearch
- **Tags**: cve,cve2023,gitlab,lfi,kev,authenticated,intrusive
- **Description**: An issue has been discovered in GitLab CE/EE affecting only version 16.0.0. An unauthenticated malicious user can use a path traversal vulnerability to read arbitrary files on the server when an attac...

#### Uninitialized GitLab instances
- **File**: `gitlab-uninitialized-password_1.yaml`
- **Author**: GitLab Red Team
- **Tags**: gitlab,misconfig,unauth
- **Description**: Prior to version 14, GitLab installations required a root password to be
set via the web UI. If the administrator skipped this step, any visitor
could set a password and control the instance.


#### Gitlab Default Login
- **File**: `gitlab-weak-login_1.yaml`
- **Author**: Suman_Kar,dwisiswant0
- **Tags**: gitlab,default-login
- **Description**: Gitlab default login credentials were discovered.

#### Gitlab Default Login
- **File**: `gitlab-weak-login_2.yaml`
- **Author**: Suman_Kar,dwisiswant0
- **Tags**: gitlab,default-login
- **Description**: Gitlab default login credentials were discovered.

### Medium Severity (6 templates)

#### GitLab - User Information Disclosure Via Open API
- **File**: `gitlab-api-user-enum.yaml`
- **Author**: Suman_Kar
- **Tags**: gitlab,enum,misconfig,disclosure
- **Description**: No description

#### GitLab Information Disclosure
- **File**: `CVE-2020-26413.yaml`
- **Author**: Print1n(https://github.com/Print1n)
- **Tags**: 
- **Description**: fofa app="GitLab"

#### GitLab GraphQL API User Enumeration
- **File**: `CVE-2021-4191.yaml`
- **Author**: zsusac
- **Tags**: cve,cve2021,gitlab,api,graphql,enum,unauth
- **Description**: An unauthenticated remote attacker can leverage this vulnerability to collect registered GitLab usernames, names, and email addresses.

#### Gitlab CE/EE 13.4 - 13.6.2 - Information Disclosure
- **File**: `CVE-2020-26413_1.yaml`
- **Author**: _0xf4n9x_,pikpikcu
- **Tags**: hackerone,cve,cve2020,gitlab,exposure,enum,graphql
- **Description**: GitLab CE and EE 13.4 through 13.6.2 is susceptible to Information disclosure via GraphQL. User email is visible. An attacker can possibly obtain sensitive information, modify data, and/or execute una...

#### GitLab GraphQL API User Enumeration
- **File**: `CVE-2021-4191_1.yaml`
- **Author**: zsusac
- **Tags**: cve,cve2021,gitlab,api,graphql,enum,unauth
- **Description**: An unauthenticated remote attacker can leverage this vulnerability to collect registered GitLab usernames, names, and email addresses.

#### GitLab - User Information Disclosure Via Open API
- **File**: `gitlab-api-user-enum_1.yaml`
- **Author**: Suman_Kar
- **Tags**: gitlab,enum,misconfig,disclosure
- **Description**: No description

### Info Severity (17 templates)

#### Gitlab API Test
- **File**: `api-gitlab.yaml`
- **Author**: Adam Crosser
- **Tags**: token-spray,gitlab
- **Description**: No description

#### Detect Gitlab
- **File**: `gitlab-detect.yaml`
- **Author**: ehsahil
- **Tags**: panel,gitlab
- **Description**: No description

#### GitLab public repositories
- **File**: `gitlab-public-repos.yaml`
- **Author**: ldionmarcil
- **Tags**: gitlab,exposure,misconfig
- **Description**: No description

#### GitLab public signup
- **File**: `gitlab-public-signup.yaml`
- **Author**: pdteam
- **Tags**: gitlab,misconfig
- **Description**: No description

#### GitLab public snippets
- **File**: `gitlab-public-snippets-1.yaml`
- **Author**: pdteam
- **Tags**: gitlab
- **Description**: No description

#### GitLab public snippets
- **File**: `gitlab-public-snippets-2.yaml`
- **Author**: pdteam
- **Tags**: gitlab
- **Description**: No description

#### GitLab public snippets
- **File**: `gitlab-public-snippets.yaml`
- **Author**: pdteam
- **Tags**: gitlab,exposure,misconfig
- **Description**: No description

#### GitLab - User Enumeration
- **File**: `gitlab-user-enum.yaml`
- **Author**: Suman_Kar
- **Tags**: gitlab,enum,misconfig,fuzz
- **Description**: No description

#### Gitlab User enumeration
- **File**: `gitlab-user-enumeration.yaml`
- **Author**: pikpikcu
- **Tags**: gitlab,enum
- **Description**: No description

#### GitLab public repositories
- **File**: `gitlab-public-repos_1.yaml`
- **Author**: ldionmarcil
- **Tags**: gitlab,exposure,misconfig
- **Description**: No description

#### GitLab public signup
- **File**: `gitlab-public-signup_1.yaml`
- **Author**: pdteam
- **Tags**: gitlab,misconfig
- **Description**: No description

#### GitLab public snippets
- **File**: `gitlab-public-snippets_1.yaml`
- **Author**: pdteam
- **Tags**: gitlab,exposure,misconfig
- **Description**: No description

#### GitLab - User Enumeration
- **File**: `gitlab-user-enum_1.yaml`
- **Author**: Suman_Kar
- **Tags**: gitlab,enum,misconfig,fuzz
- **Description**: No description

#### Gitlab Login Panel - Detect
- **File**: `gitlab-detect_1.yaml`
- **Author**: ehsahil
- **Tags**: panel,gitlab
- **Description**: Gitlab login panel was detected.

#### GitLab Personal Access Token
- **File**: `gitlab-personal-token.yaml`
- **Author**: DhiyaneshDK
- **Tags**: gitlab,token,exposure
- **Description**: No description

#### GitLab Pipeline Trigger Token
- **File**: `gitlab-pipeline-token.yaml`
- **Author**: DhiyaneshDK
- **Tags**: gitlab,token,exposure
- **Description**: No description

#### GitLab Runner Registration Token
- **File**: `gitlab-runner-token.yaml`
- **Author**: DhiyaneshDK
- **Tags**: gitlab,runner,token,exposure
- **Description**: No description

