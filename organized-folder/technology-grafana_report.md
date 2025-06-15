# Technology Grafana Templates

## Summary
- **Total templates**: 31
- **Category**: technology-grafana

## Templates List

### Critical Severity (3 templates)

#### Grafana & Zabbix Integration - Credentials Disclosure
- **File**: `CVE-2022-26148.yaml`
- **Author**: Geekby
- **Tags**: 
- **Description**: Grafana through 7.3.4, when integrated with Zabbix, contains a credential disclosure vulnerability. The Zabbix password can be found in the api_jsonrpc.php HTML source code. When the user logs in and ...

#### Grafana Snapshot Authentication Bypass
- **File**: `CVE-2021-39226_1.yaml`
- **Author**: dk4trin
- **Tags**: grafana,bypass
- **Description**: No description

#### Grafana & Zabbix Integration - Credentials Disclosure
- **File**: `CVE-2022-26148_1.yaml`
- **Author**: Geekby
- **Tags**: cve,cve2022,grafana,zabbix,exposure
- **Description**: Grafana through 7.3.4, when integrated with Zabbix, contains a credential disclosure vulnerability. The Zabbix password can be found in the api_jsonrpc.php HTML source code. When the user logs in and ...

### High Severity (16 templates)

#### Grafana Default Credentials Check
- **File**: `grafana-default-credential-1.yaml`
- **Author**: pdteam
- **Tags**: grafana,default-login
- **Description**: No description

#### Grafana Default Credentials Check
- **File**: `grafana-default-credential-2.yaml`
- **Author**: pdteam
- **Tags**: grafana,default-login
- **Description**: No description

#### Grafana Default Login
- **File**: `grafana-default-login-1.yaml`
- **Author**: pdteam
- **Tags**: grafana,default-login
- **Description**: No description

#### Grafana Default Login
- **File**: `grafana-default-login-2.yaml`
- **Author**: pdteam
- **Tags**: grafana,default-login
- **Description**: No description

#### Grafana Default Login
- **File**: `grafana-default-login.yaml`
- **Author**: pdteam
- **Tags**: grafana,default-login
- **Description**: Grafana default admin login credentials were detected.

#### Grafana v8.x Arbitrary File Read
- **File**: `grafana-file-read.yaml`
- **Author**: z0ne,dhiyaneshDk,jeya.seelan,dwisiswant0
- **Tags**: grafana,lfi,fuzz
- **Description**: No description

#### Grafana Unauthenticated Snapshot Creation
- **File**: `CVE-2021-27358.yaml`
- **Author**: pdteam,bing0o
- **Tags**: cve,cve2021,grafana,unauth
- **Description**: Grafana 6.7.3 through 7.4.1 snapshot functionality can allow an unauthenticated remote attacker to trigger a Denial of Service via a remote API call if a commonly used configuration is set.

#### Grafana Snapshot - Authentication Bypass
- **File**: `CVE-2021-39226.yaml`
- **Author**: Evan Rubinstein
- **Tags**: cve,cve2021,grafana
- **Description**: Grafana instances up to 7.5.11 and 8.1.5 allow remote unauthenticated users to view the snapshot associated with the lowest database key by accessing the literal paths /api/snapshot/:key or /dashboard...

#### Grafana v8.x Arbitrary File Read
- **File**: `CVE-2021-43798.yaml`
- **Author**: z0ne,dhiyaneshDk
- **Tags**: cve,cve2021,grafana,lfi
- **Description**: Grafana versions 8.0.0-beta1 through 8.3.0 are vulnerable to a local directory traversal, allowing access to local files. The vulnerable URL path is `<grafana_host_url>/public/plugins/NAME/`, where NA...

#### Grafana Default Login
- **File**: `grafana-default-login_1.yaml`
- **Author**: d3sca
- **Tags**: grafana,default-login
- **Description**: No description

#### Grafana Unauthenticated Snapshot Creation
- **File**: `CVE-2021-27358_1.yaml`
- **Author**: pdteam,bing0o
- **Tags**: cve,cve2021,grafana,unauth
- **Description**: Grafana 6.7.3 through 7.4.1 snapshot functionality can allow an unauthenticated remote attacker to trigger a Denial of Service via a remote API call if a commonly used configuration is set.

#### Grafana Snapshot - Authentication Bypass
- **File**: `CVE-2021-39226_2.yaml`
- **Author**: Evan Rubinstein
- **Tags**: cve,cve2021,grafana,kev
- **Description**: Grafana instances up to 7.5.11 and 8.1.5 allow remote unauthenticated users to view the snapshot associated with the lowest database key by accessing the literal paths /api/snapshot/:key or /dashboard...

#### Grafana v8.x - Arbitrary File Read
- **File**: `CVE-2021-43798_1.yaml`
- **Author**: z0ne,dhiyaneshDk,j4vaovo
- **Tags**: packetstorm,cve,cve2021,grafana,lfi
- **Description**: Grafana versions 8.0.0-beta1 through 8.3.0 are vulnerable to a local directory traversal, allowing access to local files. The vulnerable URL path is `<grafana_host_url>/public/plugins/NAME/`, where NA...

#### Grafana Default Login
- **File**: `grafana-default-login_2.yaml`
- **Author**: pdteam
- **Tags**: grafana,default-login
- **Description**: Grafana default admin login credentials were detected.

#### Grafana v8.x Arbitrary File Read
- **File**: `grafana-file-read_1.yaml`
- **Author**: z0ne,dhiyaneshDk,jeya.seelan,dwisiswant0
- **Tags**: grafana,lfi,fuzz
- **Description**: No description

#### Grafana Default Login
- **File**: `grafana-default-login_3.yaml`
- **Author**: pdteam
- **Tags**: grafana,default-login
- **Description**: Grafana default admin login credentials were detected.

### Medium Severity (7 templates)

#### Grafana Public Signup
- **File**: `grafana-public-signup.yaml`
- **Author**: pdteam
- **Tags**: grafana,intrusive
- **Description**: No description

#### Grafana unauthenticated API
- **File**: `CVE-2019-15043.yaml`
- **Author**: bing0o
- **Tags**: cve,cve2019,grafana
- **Description**: In Grafana 2.x through 6.x before 6.3.4, parts of the HTTP API allow unauthenticated use. This makes it possible to run a denial of service attack against the server running Grafana.

#### Grafana CVE-2021-43798
- **File**: `CVE-2021-43798-Grafana.yaml`
- **Author**: Str1am
- **Tags**: Grafana,file_read
- **Description**: Grafana 版本 8.0.0-beta1 到 8.3.0（补丁版本除外）容易受到目录遍历

#### Grafana 8.0.0 <= v.8.2.2 XSS
- **File**: `CVE-2021-41174.yaml`
- **Author**: dk4trin
- **Tags**: grafana,xss
- **Description**: No description

#### Prometheus Config API Endpoint Discovery
- **File**: `grafana_with_prometheus_api_proxy.yaml`
- **Author**: Esonhugh-self-maintained
- **Tags**: prometheus,misconfig,grafana
- **Description**: A Prometheus API endpoint via grafana Public Access was discovered.

#### Grafana Public Signup
- **File**: `grafana-public-signup_1.yaml`
- **Author**: pdteam
- **Tags**: grafana,intrusive
- **Description**: No description

#### Grafana Default Login
- **File**: `custom-grafana-default-login.yaml`
- **Author**: 0xParthJ
- **Tags**: default-login
- **Description**: Grafana default login credentials were discovered.

### Info Severity (5 templates)

#### Grafana panel detect
- **File**: `grafana-detect.yaml`
- **Author**: organiccrap
- **Tags**: panel,grafana
- **Description**: No description

#### Grafana Login Panel - Detect
- **File**: `grafana-detect_1.yaml`
- **Author**: organiccrap,AdamCrosser,bhutch
- **Tags**: panel,grafana,detect
- **Description**: Grafana login panel was detected.

#### Grafana Cloud API Key
- **File**: `grafana-cloud-token.yaml`
- **Author**: DhiyaneshDK
- **Tags**: grafana,exposure,tokens
- **Description**: No description

#### Grafana API Key
- **File**: `grafana-key.yaml`
- **Author**: DhiyaneshDK
- **Tags**: grafana,exposure,tokens
- **Description**: No description

#### Grafana Service Account Token
- **File**: `grafana-serviceaccount-token.yaml`
- **Author**: DhiyaneshDK
- **Tags**: grafana,exposure,tokens
- **Description**: No description

