# Attack Xxe Templates

## Summary
- **Total templates**: 22
- **Category**: attack-xxe

## Templates List

### Critical Severity (8 templates)

#### PeopleSoft XXE
- **File**: `PeopleSoft-XXE-1.yaml`
- **Author**: 0xAwali
- **Tags**: 
- **Description**: PeopleSoft XXE , Commonly Bound Ports 80 - 443

#### PeopleSoft XXE
- **File**: `PeopleSoft-XXE-2.yaml`
- **Author**: 0xAwali
- **Tags**: 
- **Description**: PeopleSoft XXE , Commonly Bound Ports 80 - 443

#### WSO2 API Manager <=3.1.0 - Blind XML External Entity Injection
- **File**: `CVE-2020-24589.yaml`
- **Author**: lethargynavigator
- **Tags**: cve,cve2020,wso2,xxe,oast,blind
- **Description**: WSO2 API Manager 3.1.0 and earlier is vulnerable to blind XML external entity injection (XXE). XXE often allows an attacker to view files on the server file system, and to interact with any backend or...

#### LumisXP <10.0.0 - Blind XML External Entity Attack
- **File**: `CVE-2021-27931.yaml`
- **Author**: alph4byt3
- **Tags**: cve,cve2021,lumis,xxe,oast,blind
- **Description**: LumisXP (aka Lumis Experience Platform) before 10.0.0 allows unauthenticated blind XML external entity (XXE) attacks via an API request to PageControllerXml.jsp. One can send a request crafted with an...

#### WSO2 API Manager <=3.1.0 - Blind XML External Entity Injection
- **File**: `CVE-2020-24589_1.yaml`
- **Author**: lethargynavigator
- **Tags**: cve,cve2020,wso2,xxe,oast,blind
- **Description**: WSO2 API Manager 3.1.0 and earlier is vulnerable to blind XML external entity injection (XXE). XXE often allows an attacker to view files on the server file system, and to interact with any backend or...

#### LumisXP <10.0.0 - Blind XML External Entity Attack
- **File**: `CVE-2021-27931_1.yaml`
- **Author**: alph4byt3
- **Tags**: cve,cve2021,lumis,xxe,oast,blind
- **Description**: LumisXP (aka Lumis Experience Platform) before 10.0.0 allows unauthenticated blind XML external entity (XXE) attacks via an API request to PageControllerXml.jsp. One can send a request crafted with an...

#### Zoho ManageEngine ADAudit Plus <7600 - XML Entity Injection/Remote Code Execution
- **File**: `CVE-2022-28219.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2022,xxe,rce,zoho,manageengine,unauth
- **Description**: Zoho ManageEngine ADAudit Plus before version 7060 is vulnerable to an
unauthenticated XML entity injection attack that can lead to remote code execution.


#### XXE
- **File**: `xxe_lfi.yaml`
- **Author**: MRiambatman
- **Tags**: 
- **Description**: No description

### High Severity (9 templates)

#### Generic Blind XXE
- **File**: `generic-blind-xxe.yaml`
- **Author**: geeknik
- **Tags**: xxe,generic,blind
- **Description**: No description

#### SAP Internet Graphics Server (IGS) XML External Entity
- **File**: `CVE-2018-2392.yaml`
- **Author**: _generic_human_
- **Tags**: cve,cve2018,sap,igs,xxe,xmlchart
- **Description**: SAP Internet Graphics Servers (IGS) running versions 7.20, 7.20EXT, 7.45, 7.49, or 7.53 has two XXE vulnerabilities within the XMLCHART page - CVE-2018-2392 and CVE-2018-2393. These vulnerabilities oc...

#### IBM Maximo Asset Management Information Disclosure via XXE
- **File**: `CVE-2020-4463-1.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,ibm,xxe
- **Description**: IBM Maximo Asset Management is vulnerable to an
XML External Entity Injection (XXE) attack when processing XML data.
A remote attacker could exploit this vulnerability to expose
sensitive information ...

#### IBM Maximo Asset Management Information Disclosure via XXE
- **File**: `CVE-2020-4463-2.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,ibm,xxe
- **Description**: IBM Maximo Asset Management is vulnerable to an
XML External Entity Injection (XXE) attack when processing XML data.
A remote attacker could exploit this vulnerability to expose
sensitive information ...

#### IBM Maximo Asset Management Information Disclosure via XXE
- **File**: `CVE-2020-4463.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,ibm,xxe,disclosure
- **Description**: IBM Maximo Asset Management is vulnerable to an
XML External Entity Injection (XXE) attack when processing XML data.
A remote attacker could exploit this vulnerability to expose
sensitive information ...

#### OpenCMS - Unauthenticated XXE
- **File**: `CVE-2023-42344.yaml`
- **Author**: 0xr2r
- **Tags**: cve,cve2023,xxe,opencms
- **Description**: users can execute code without authentication.  An attacker can execute malicious requests on the OpenCms server. When the requests are successful vulnerable OpenCms can be exploited resulting in an u...

#### IBM Maximo Asset Management Information Disclosure - XML External Entity Injection
- **File**: `CVE-2020-4463_1.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,ibm,xxe,disclosure
- **Description**: IBM Maximo Asset Management is vulnerable to an
XML external entity injection (XXE) attack when processing XML data.
A remote attacker could exploit this vulnerability to expose
sensitive information ...

#### FreeIPA - XML Entity Injection
- **File**: `CVE-2022-2414.yaml`
- **Author**: DhiyaneshDk
- **Tags**: cve,cve2022,dogtag,freeipa,xxe
- **Description**: Access to external entities when parsing XML documents can lead to XML external entity (XXE) attacks. This flaw allows a remote attacker to potentially retrieve the content of arbitrary files by sendi...

#### Generic Blind XXE
- **File**: `generic-blind-xxe_1.yaml`
- **Author**: geeknik
- **Tags**: xxe,generic,blind
- **Description**: No description

### Medium Severity (5 templates)

#### JAMF Blind XXE / SSRF
- **File**: `jamf-blind-xxe.yaml`
- **Author**: pdteam
- **Tags**: xxe,ssrf,jamf
- **Description**: No description

#### Find Kronos wsdl exposure (Try XXE)
- **File**: `Kronos-wsld-exposure.yaml`
- **Author**: Clark
- **Tags**: 
- **Description**: No description

#### JAMF Blind XXE / SSRF
- **File**: `jamf-blind-xxe_1.yaml`
- **Author**: pdteam
- **Tags**: xxe,ssrf,jamf
- **Description**: No description

#### XXE Fuzzing
- **File**: `fuzz-xxe.yaml`
- **Author**: pwnhxl,otterly
- **Tags**: dast,xxe
- **Description**: No description

#### Find Kronos wsdl exposure (Try XXE)
- **File**: `kronos-wsld-exposure_1.yaml`
- **Author**: Clark
- **Tags**: 
- **Description**: No description

