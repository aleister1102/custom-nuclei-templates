# Technology Nodejs Templates

## Summary
- **Total templates**: 6
- **Category**: technology-nodejs

## Templates List

### Critical Severity (1 templates)

#### Node.js Embedded JavaScript 3.1.6 - Template Injection
- **File**: `CVE-2022-29078.yaml`
- **Author**: For3stCo1d
- **Tags**: cve,cve2022,ssti,rce,ejs,nodejs,oast,intrusive
- **Description**: Node.js Embedded JavaScript 3.1.6 is susceptible to server-side template injection via settings[view options][outputFunctionName], which is parsed as an internal option and overwrites the outputFuncti...

### High Severity (4 templates)

#### Node.js st module Directory Traversal
- **File**: `CVE-2014-3744.yaml`
- **Author**: geeknik
- **Tags**: cve,cve2014,lfi,nodejs,st
- **Description**: A directory traversal vulnerability in the st module before 0.2.5 for Node.js allows remote attackers to read arbitrary files via a %2e%2e (encoded dot dot) in an unspecified path.

#### Node.js 8.5.0 >=< 8.6.0 Directory Traversal
- **File**: `CVE-2017-14849.yaml`
- **Author**: Random_Robbie
- **Tags**: cve,cve2017,nodejs,lfi
- **Description**: Node.js 8.5.0 before 8.6.0 allows remote attackers to access unintended files, because a change to ".." handling was incompatible with the pathname validation used by unspecified community modules.

#### Node.js Systeminformation Command Injection
- **File**: `CVE-2021-21315.yaml`
- **Author**: pikpikcu
- **Tags**: nodejs,cve,cve2021
- **Description**: The System Information Library for Node.JS (npm package "systeminformation") is an open source collection of functions to retrieve detailed hardware, system and OS information. In systeminformation be...

#### Node.JS System Information Library <5.3.1 - Remote Command Injection
- **File**: `CVE-2021-21315_1.yaml`
- **Author**: pikpikcu
- **Tags**: nodejs,cve,cve2021,kev
- **Description**: Node.JS System Information Library System before version 5.3.1 is susceptible to remote command injection. Node.JS (npm package "systeminformation") is an open source collection of functions to retrie...

### Medium Severity (1 templates)

#### node-srv Path Traversal
- **File**: `CVE-2018-3714.yaml`
- **Author**: madrobot
- **Tags**: cve,cve2018,nodejs,lfi
- **Description**: node-srv node module suffers from a Path Traversal vulnerability due to lack of validation of url, which allows a malicious user to read content of any file with known path.

