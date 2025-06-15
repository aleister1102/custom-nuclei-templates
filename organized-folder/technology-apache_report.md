# Technology Apache Templates

## Summary
- **Total templates**: 293
- **Category**: technology-apache

## Templates List

### Critical Severity (43 templates)

#### Apache Airflow Default Credentials
- **File**: `airflow-default-credentials.yaml`
- **Author**: pdteam
- **Tags**: airflow,default-login
- **Description**: No description

#### APACHE-Ambari 弱口令(admin/admin)
- **File**: `APACHE-Ambari-weakPass.yaml`
- **Author**: Str1am
- **Tags**: APACHE-Ambari,weakPass
- **Description**: No description

#### Apache Flink - Remote Code Execution
- **File**: `apache-flink-unauth-rce.yaml`
- **Author**: pikpikcu
- **Tags**: apache,flink,rce,intrusive,unauth
- **Description**: Apache Flink

#### Apache HTTPd - 2.4.49 (CGI enabled) RCE
- **File**: `apache-httpd-rce.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2021,rce,apache
- **Description**: A flaw was found in a change made to path normalization in Apache HTTP Server 2.4.49. An attacker could use a path traversal attack to map URLs to files outside the expected document root. If files ou...

#### Apache Solr SSRF
- **File**: `ApacheSolr-SSRF-1.yaml`
- **Author**: 0xAwali
- **Tags**: 
- **Description**: Apache Solr SSRF Via Shards Parameter , Commonly Bound Ports 8983

#### Apache Solr SSRF
- **File**: `ApacheSolr-SSRF-2.yaml`
- **Author**: 0xAwali
- **Tags**: 
- **Description**: Apache Solr SSRF Via Shards Parameter , Commonly Bound Ports 8983

#### Apache Solr SSRF
- **File**: `ApacheSolr-SSRF-3.yaml`
- **Author**: 0xAwali
- **Tags**: 
- **Description**: Apache Solr SSRF Via Solr Local Parameters Injection , Commonly Bound Ports 8983

#### Apache Solr SSRF
- **File**: `ApacheSolr-SSRF-4.yaml`
- **Author**: 0xAwali
- **Tags**: 
- **Description**: Apache Solr SSRF Solr Local Parameters Injection , Commonly Bound Ports 8983

#### Apache Solr RCE
- **File**: `ApacheSolr-SSRF-5.yaml`
- **Author**: 0xAwali
- **Tags**: 
- **Description**: Apache Solr RCE Via RunExecutableListener , Commonly Bound Ports 8983

#### Apache Solr RCE
- **File**: `ApacheSolr-SSRF-6.yaml`
- **Author**: 0xAwali
- **Tags**: 
- **Description**: Apache Solr RCE Via Deserialization Of untrusted Data Through jmx.serviceUrl , Commonly Bound Ports 8983

#### Apache Struts RCE
- **File**: `ApacheStruts-RCE.yaml`
- **Author**: 0xAwali
- **Tags**: 
- **Description**: Apache Struts XXE , Commonly Bound Ports 80 - 443 - 8080 - 8443

#### OpenSymphony XWork/Apache Struts2 - Remote Code Execution S2-001
- **File**: `CVE-2007-4556.yaml`
- **Author**: pikpikcu
- **Tags**: 
- **Description**: Apache Struts support in OpenSymphony XWork before 1.2.3, and 2.x before 2.0.4, as used in WebWork and Apache Struts, recursively evaluates all input as an Object-Graph Navigation Language (OGNL) expr...

#### Apache Struts 2 - DefaultActionMapper Prefixes OGNL Code Execution
- **File**: `CVE-2013-2251-1.yaml`
- **Author**: exploitation,dwisiswant0,alex
- **Tags**: cve,cve2013,rce,struts,apache
- **Description**: In Struts 2 before 2.3.15.1 the information following "action:", "redirect:" or "redirectAction:" is not properly sanitized. Since said information will be evaluated as OGNL expression against the val...

#### Apache Struts 2 - DefaultActionMapper Prefixes OGNL Code Execution
- **File**: `CVE-2013-2251-2.yaml`
- **Author**: exploitation,dwisiswant0,alex
- **Tags**: cve,cve2013,rce,struts,apache
- **Description**: In Struts 2 before 2.3.15.1 the information following "action:", "redirect:" or "redirectAction:" is not properly sanitized. Since said information will be evaluated as OGNL expression against the val...

#### Apache Struts 2 - DefaultActionMapper Prefixes OGNL Code Execution
- **File**: `CVE-2013-2251-4.yaml`
- **Author**: exploitation,dwisiswant0,alex
- **Tags**: cve,cve2013,rce,struts,apache
- **Description**: In Struts 2 before 2.3.15.1 the information following "action:", "redirect:" or "redirectAction:" is not properly sanitized. Since said information will be evaluated as OGNL expression against the val...

#### Apache Struts 2 - DefaultActionMapper Prefixes OGNL Code Execution
- **File**: `CVE-2013-2251-5.yaml`
- **Author**: exploitation,dwisiswant0,alex
- **Tags**: cve,cve2013,rce,struts,apache
- **Description**: In Struts 2 before 2.3.15.1 the information following "action:", "redirect:" or "redirectAction:" is not properly sanitized. Since said information will be evaluated as OGNL expression against the val...

#### Apache Struts 2 - DefaultActionMapper Prefixes OGNL Code Execution
- **File**: `CVE-2013-2251-7.yaml`
- **Author**: exploitation,dwisiswant0,alex
- **Tags**: cve,cve2013,rce,struts,apache
- **Description**: In Struts 2 before 2.3.15.1 the information following "action:", "redirect:" or "redirectAction:" is not properly sanitized. Since said information will be evaluated as OGNL expression against the val...

#### Apache Struts 2 - DefaultActionMapper Prefixes OGNL Code Execution
- **File**: `CVE-2013-2251-8.yaml`
- **Author**: exploitation,dwisiswant0,alex
- **Tags**: cve,cve2013,rce,struts,apache
- **Description**: In Struts 2 before 2.3.15.1 the information following "action:", "redirect:" or "redirectAction:" is not properly sanitized. Since said information will be evaluated as OGNL expression against the val...

#### Airflow Experimental <1.10.11 - REST API Auth Bypass
- **File**: `CVE-2020-13927.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2020,apache,airflow,unauth,auth-bypass
- **Description**: Airflow's Experimental API prior 1.10.11 allows all API requests without authentication.


#### Apache APISIX 默认密钥漏洞
- **File**: `CVE-2020-13945.yaml`
- **Author**: 不动明王 exp
- **Tags**: 
- **Description**: Apache APISIX是一个高性能API网关。在用户未指定管理员Token或使用了默认配置文件的情况下，Apache APISIX将使用默认的管理员Token edd1c9f034335f136f87ad84b625c8f1，攻击者利用这个Token可以访问到管理员接口，进而通过script参数来插入任意LUA脚本并执行。


#### Apache Tapestry - Remote Code Execution
- **File**: `CVE-2021-27850.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2021,apache,tapestry
- **Description**: Apache Tapestry contains a critical unauthenticated remote code execution vulnerability. Affected versions include 5.4.5, 5.5.0, 5.6.2 and 5.7.0. Note that this vulnerability is a bypass of the fix fo...

#### Apache Solr <= 8.8.1 SSRF
- **File**: `CVE-2021-27905.yaml`
- **Author**: hackergautam
- **Tags**: 
- **Description**: The ReplicationHandler (normally registered at "/replication" under a Solr core) in Apache Solr has a "masterUrl" (also "leaderUrl" alias) parameter that is used to designate another ReplicationHandle...

#### Apache Airflow - Unauthenticated Variable Import
- **File**: `CVE-2021-38540.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2021,apache,airflow,rce
- **Description**: Apache Airflow Airflow >=2.0.0 and <2.1.3 does not protect the variable import endpoint which allows unauthenticated users to hit that endpoint to add/modify Airflow variables used in DAGs, potentiall...

#### Apache <= 2.4.48 Mod_Proxy SSRF
- **File**: `CVE-2021-40438.yaml`
- **Author**: pdteam
- **Tags**: 
- **Description**: Apache 2.4.8 and below contain an issue where uri-path can cause mod_proxy to forward the request to an origin server chosen by the remote user.

#### RCE in Apache HTTP Server 2.4.49
- **File**: `CVE-2021-41773 (2).yaml`
- **Author**: RafaelCaria
- **Tags**: cve,cve2021,rce
- **Description**: No description

#### Apache 2.4.49/2.4.50 - Path Traversal and Remote Code Execution
- **File**: `CVE-2021-42013-1.yaml`
- **Author**: nvn1729,0xd0ff9
- **Tags**: cve,cve2021,lfi,apache,rce,misconfig
- **Description**: A flaw was found in a change made to path normalization in Apache HTTP Server 2.4.49 and 2.4.50. An attacker could use a path traversal attack to map URLs to files outside the expected document root. ...

#### Apache 2.4.49/2.4.50 - Path Traversal and Remote Code Execution
- **File**: `CVE-2021-42013-2.yaml`
- **Author**: nvn1729,0xd0ff9
- **Tags**: cve,cve2021,lfi,apache,rce,misconfig
- **Description**: A flaw was found in a change made to path normalization in Apache HTTP Server 2.4.49 and 2.4.50. An attacker could use a path traversal attack to map URLs to files outside the expected document root. ...

#### Apache APISIX Dashboard <2.10.1 - API Unauthorized Access
- **File**: `CVE-2021-45232.yaml`
- **Author**: Mr-xn
- **Tags**: 
- **Description**: In Apache APISIX Dashboard before 2.10.1, the Manager API uses two frameworks and introduces framework `droplet` on the basis of framework `gin.' While all APIs and authentication middleware are devel...

#### Apache APISIX apisix/batch-requests RCE
- **File**: `CVE-2022-24112.yaml`
- **Author**: Mr-xn
- **Tags**: 
- **Description**: Apache APISIX apisix/batch-requests plugin allows overwriting the X-REAL-IP header to RCE;An attacker can abuse the batch-requests plugin to send requests to bypass the IP restriction of Admin API. A ...

#### Airflow Experimental <1.10.11 - REST API Auth Bypass
- **File**: `CVE-2020-13927_1.yaml`
- **Author**: pdteam
- **Tags**: packetstorm,cve,cve2020,apache,airflow,unauth,auth-bypass,kev
- **Description**: Airflow's Experimental API prior 1.10.11 allows all API requests without authentication.


#### Apache Struts 2.0.0-2.5.25 - Remote Code Execution
- **File**: `CVE-2020-17530.yaml`
- **Author**: pikpikcu
- **Tags**: cve,cve2020,apache,rce,struts,kev,packetstorm
- **Description**: Apache Struts 2.0.0 through Struts 2.5.25 is susceptible to remote code execution because forced OGNL evaluation, when evaluated on raw user input in tag attributes, may allow it.

#### Apache Tapestry - Remote Code Execution
- **File**: `CVE-2021-27850_1.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2021,apache,tapestry
- **Description**: Apache Tapestry contains a critical unauthenticated remote code execution vulnerability. Affected versions include 5.4.5, 5.5.0, 5.6.2 and 5.7.0. Note that this vulnerability is a bypass of the fix fo...

#### Apache Solr <=8.8.1 - Server-Side Request Forgery
- **File**: `CVE-2021-27905_1.yaml`
- **Author**: hackergautam
- **Tags**: cve,cve2021,apache,solr,ssrf
- **Description**: Apache Solr versions 8.8.1 and prior contain a server-side request forgery vulnerability. The ReplicationHandler (normally registered at "/replication" under a Solr core) in Apache Solr has a "masterU...

#### Apache ShenYu Admin JWT - Authentication Bypass
- **File**: `CVE-2021-37580.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2021,apache,jwt,shenyu
- **Description**: Apache ShenYu 2.3.0 and 2.4.0 allow Admin access without proper authentication. The incorrect use of JWT in ShenyuAdminBootstrap allows an attacker to bypass authentication.

#### Apache Airflow - Unauthenticated Variable Import
- **File**: `CVE-2021-38540_1.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2021,apache,airflow,rce,intrusive
- **Description**: Apache Airflow Airflow >=2.0.0 and <2.1.3 does not protect the variable import endpoint which allows unauthenticated users to hit that endpoint to add/modify Airflow variables used in DAGs, potentiall...

#### Apache <= 2.4.48 - Mod_Proxy SSRF
- **File**: `CVE-2021-40438_1.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2021,ssrf,apache,mod-proxy,kev
- **Description**: Apache 2.4.48 and below contain an issue where uri-path can cause mod_proxy to forward the request to an origin server chosen by the remote user.

#### Apache 2.4.49/2.4.50 - Path Traversal and Remote Code Execution
- **File**: `CVE-2021-42013.yaml`
- **Author**: nvn1729,0xd0ff9,666asd
- **Tags**: cve,cve2021,lfi,apache,rce,misconfig,traversal,kev
- **Description**: A flaw was found in a change made to path normalization in Apache HTTP Server 2.4.49 and 2.4.50. An attacker could use a path traversal attack to map URLs to files outside the expected document root. ...

#### Apache APISIX Dashboard <2.10.1 - API Unauthorized Access
- **File**: `CVE-2021-45232_1.yaml`
- **Author**: Mr-xn
- **Tags**: cve,cve2021,apache,unauth,apisix
- **Description**: In Apache APISIX Dashboard before 2.10.1, the Manager API uses two frameworks and introduces framework `droplet` on the basis of framework `gin.' While all APIs and authentication middleware are devel...

#### Apache ShenYu Admin Unauth Access
- **File**: `CVE-2022-23944.yaml`
- **Author**: cckuakilong
- **Tags**: cve,cve2022,shenyu,unauth,apache
- **Description**: Apache ShenYu suffers from an unauthorized access vulnerability where a user can access /plugin api without authentication. This issue affected Apache ShenYu 2.4.0 and 2.4.1.

#### Apache APISIX - Remote Code Execution
- **File**: `CVE-2022-24112_1.yaml`
- **Author**: Mr-xn
- **Tags**: cve,cve2022,apache,rce,apisix,oast,kev,intrusive
- **Description**: A default configuration of Apache APISIX (with default API key) is vulnerable to remote code execution. An attacker can abuse the batch-requests plugin to send requests to bypass the IP restriction of...

#### Apache Superset - Authentication Bypass
- **File**: `CVE-2023-27524.yaml`
- **Author**: DhiyaneshDK,_0xf4n9x_
- **Tags**: packetstorm,cve,cve2023,apache,superset,auth-bypass
- **Description**: Session Validation attacks in Apache Superset versions up to and including 2.0.1. Installations that have not altered the default configured SECRET_KEY according to installation instructions allow for...

#### Apache Flink Unauth RCE
- **File**: `apache-flink-unauth-rce_1.yaml`
- **Author**: pikpikcu
- **Tags**: apache,flink,rce,intrusive,unauth
- **Description**: No description

#### Apache Hadoop - Yarn ResourceManager Remote Code Execution
- **File**: `hadoop-unauth-rce.yaml`
- **Author**: pdteam,Couskito
- **Tags**: vulhub,apache,hadoop,unauth,rce,msf
- **Description**: An unauthenticated Hadoop Resource Manager was discovered, which allows remote code execution by design.


### High Severity (94 templates)

#### Apache Airflow Default Login
- **File**: `airflow-default-login.yaml`
- **Author**: pdteam
- **Tags**: airflow,default-login,apache
- **Description**: An Apache Airflow default login was discovered.

#### Apache Ambari Default Login
- **File**: `ambari-default-login.yaml`
- **Author**: pdteam
- **Tags**: ambari,default-login,apache
- **Description**: An Apache Ambari default admin login was discovered.

#### Axis2 Default Login
- **File**: `axis2-default-login-1.yaml`
- **Author**: pikpikcu
- **Tags**: axis,apache,default-login
- **Description**: No description

#### Axis2 Default Login
- **File**: `axis2-default-login-2.yaml`
- **Author**: pikpikcu
- **Tags**: axis,apache,default-login
- **Description**: No description

#### Axis2 Default Login
- **File**: `axis2-default-login.yaml`
- **Author**: pikpikcu
- **Tags**: axis,apache,default-login,axis2
- **Description**: No description

#### Axis2 Default Password
- **File**: `axis2-default-password-1.yaml`
- **Author**: pikpikcu
- **Tags**: axis,apache,default-login
- **Description**: No description

#### Axis2 Default Password
- **File**: `axis2-default-password-2.yaml`
- **Author**: pikpikcu
- **Tags**: axis,apache,default-login
- **Description**: No description

#### Axis2 Default Password
- **File**: `axis2-default-password.yaml`
- **Author**: pikpikcu
- **Tags**: axis,apache,default-login
- **Description**: No description

#### Apache DolphinScheduler Default Login
- **File**: `dolphinscheduler-default-login.yaml`
- **Author**: For3stCo1d
- **Tags**: apache,dolphinscheduler,default-login,oss
- **Description**: Apache DolphinScheduler default admin credentials were discovered.

#### Apache Druid Default Login
- **File**: `druid-default-login.yaml`
- **Author**: pikpikcu
- **Tags**: druid,default-login
- **Description**: Apache Druid default login information (admin/admin) was discovered.

#### Dubbo Admin Default Login
- **File**: `dubbo-admin-default-login.yaml`
- **Author**: ritikchaddha
- **Tags**: dubbo,apache,default-login
- **Description**: No description

#### Apache Kafka Center Default Login
- **File**: `kafka-center-default-login.yaml`
- **Author**: dhiyaneshDK
- **Tags**: kafka,default-login
- **Description**: Apache Kafka Center default admin credentials were discovered.

#### Apache Ranger Default Login
- **File**: `ranger-default-login.yaml`
- **Author**: For3stCo1d
- **Tags**: apache,ranger,default-login
- **Description**: No description

#### Apache Superset Default Login
- **File**: `superset-default-login.yaml`
- **Author**: dhiyaneshDK
- **Tags**: apache, default-login
- **Description**: Apache Superset up to and including 1.3.2 allowed for registered database connections password leak for authenticated users. This information could be accessed in a non-trivial way.

#### Unauthenticated Airflow Instance
- **File**: `unauthenticated-airflow.yaml`
- **Author**: dhiyaneshDK
- **Tags**: apache,airflow,unauth
- **Description**: No description

#### Apache NiFi系统API命令执行
- **File**: `Apache-NiFi-rce.yaml`
- **Author**: Str1am
- **Tags**: NiFi,rce
- **Description**: No description

#### Apache Solr <= 8.8.1 Arbitrary File Read
- **File**: `apache-solr-file-read.yaml`
- **Author**: DhiyaneshDk
- **Tags**: apache,solr,lfi
- **Description**: No description

#### apache-solr-ssrf
- **File**: `apache-solr-ssrf.yaml`
- **Author**: str1am
- **Tags**: 74cms,sqli
- **Description**: No description

#### Apache solr 未授权访问
- **File**: `Apache-solr-unauth.yaml`
- **Author**: Str1am
- **Tags**: solr,unauth
- **Description**: No description

#### Apache Spark RCE
- **File**: `apache-spark-rce.yaml`
- **Author**: pikpikcu
- **Tags**: rce,apache,spark
- **Description**: No description

#### ApahceTomcat Manager Default Login
- **File**: `tomcat-default-login.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: Apache Tomcat Manager default login credentials were discovered. This template checks for multiple variations.

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-1.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-10.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-11.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-12.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-13.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-14.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-15.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-16.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-2.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-3.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-4.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-5.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-6.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-7.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-8.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default-9.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### tomcat-manager-default-password
- **File**: `tomcat-manager-default.yaml`
- **Author**: pdteam
- **Tags**: tomcat,apache,default-login
- **Description**: No description

#### Apache Apisix Default Admin Login
- **File**: `apisix-default-login.yaml`
- **Author**: pdteam
- **Tags**: apisix,apache,default-login
- **Description**: An Apache Apisix default admin login was discovered.

#### Apache Axis2 Default Login
- **File**: `CVE-2010-0219.yaml`
- **Author**: pikpikcu
- **Tags**: cve,cve2010,axis,apache,default-login,axis2
- **Description**: Apache Axis2, as used in dswsbobje.war in SAP BusinessObjects Enterprise XI 3.2, CA ARCserve D2D r15, and other products, has a default password of axis2 for the admin account, which makes it easier f...

#### Apache Tomcat RCE
- **File**: `CVE-2017-12615.yaml`
- **Author**: j4ckzh0u(https://github.com/j4ckzh0u)
- **Tags**: 
- **Description**: No description

#### Apache Arbitrary File Upload
- **File**: `CVE-2017-15715.yaml`
- **Author**: geeknik
- **Tags**: cve,cve2017,apache,httpd,fileupload
- **Description**: In Apache httpd 2.4.0 to 2.4.29, the expression specified in <FilesMatch> could match '$' to a newline character in a malicious filename, rather than matching only the end of the filename. This could ...

#### Apache Solr Remote Code Execution
- **File**: `CVE-2019-0193.yaml`
- **Author**: fnmsd(https://github.com/fnmsd)
- **Tags**: 
- **Description**: 2019 年 08 月 01 日，Apache Solr 官方发布预警，Apache Solr DataImport 功能 在开启 Debug 模式时，可以接收来自请求的”dataConfig”参数，这个参数的功能与data-config.xml 一样，不过是在开启 Debug 模式时方便通过此参数进行调试，并且 Debug 模式的开启是通过参数传入的。在 dataConfig 参数中可以包含 s...

#### Apache Airflow <= 1.10.10 - 'Example Dag' Remote Code Execution
- **File**: `CVE-2020-11978.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2020,apache,airflow,rce
- **Description**: An issue was found in Apache Airflow versions 1.10.10 and below. A remote code/command injection vulnerability was discovered in one of the example DAGs shipped with Airflow which would allow any auth...

#### Apache Cocoon 2.1.12 XML Injection
- **File**: `CVE-2020-11991.yaml`
- **Author**: pikpikcu
- **Tags**: 
- **Description**: Apache Cocoon 2.1.12 is susceptible to  XML injection. When using the StreamGenerator, the code parses a user-provided XML. A specially crafted XML, including external system entities, can be used to ...

#### Apache Kylin弱口令到rce
- **File**: `CVE-2020-1956.yaml`
- **Author**: Str1am
- **Tags**: Kylin,rce
- **Description**: No description

#### Apache Tomcat Remote Command Execution
- **File**: `CVE-2020-9484.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,apache,tomcat,rce
- **Description**: When using Apache Tomcat versions 10.0.0-M1 to 10.0.0-M4, 9.0.0.M1 to 9.0.34, 8.5.0 to 8.5.54 and 7.0.0 to 7.0.103 if
a) an attacker is able to control the contents and name of a file on the server; a...

#### Apache HTTP Server 2.4.20-2.4.43 - HTTP/2 Cache-Digest DoS
- **File**: `CVE-2020-9490.yaml`
- **Author**: philippedelteil
- **Tags**: cve,cve2020,apache,dos
- **Description**: Apache HTTP Server versions 2.4.20 to 2.4.43. A specially crafted value for the 'Cache-Digest' header in a HTTP/2 request would result in a crash when the server actually tries to HTTP/2 PUSH a resour...

#### Apache Superset Default Password
- **File**: `CVE-2021-44451.yaml`
- **Author**: dhiyaneshDK
- **Tags**: 
- **Description**: Apache Superset up to and including 1.3.2 allowed for registered database connections password leak for authenticated users. This information could be accessed in a non-trivial way.
Users should upgra...

#### Apache Airflow OS Command Injection
- **File**: `CVE-2022-24288.yaml`
- **Author**: xeldax
- **Tags**: cve,cve2022,airflow,rce
- **Description**: Apache Airflow prior to version 2.2.4 is vulnerable to OS command injection attacks because some example DAGs do not properly sanitize user-provided parameters, making them susceptible to OS Command I...

#### CVE-2024-34750
- **File**: `CVE-2024-34750.yaml`
- **Author**: Redflare Cyber
- **Tags**: tech,tomcat,apache,intrusive
- **Description**: Improper Handling of Exceptional Conditions, Uncontrolled Resource Consumption vulnerability in Apache Tomcat. When processing an HTTP/2 stream, Tomcat did not handle some cases of excessive HTTP head...

#### Apache HTTP Server HTTP Request Smuggling (CVE-2024-40725)
- **File**: `CVE-2024-40725.yaml`
- **Author**: Redflare Cyber
- **Tags**: cve, http-request-smuggling, apache, mod_proxy
- **Description**: Detects the presence of CVE-2024-40725 vulnerability in Apache HTTP Server using HTTP Request Smuggling techniques.

#### Apache Airflow <=1.10.10 - Remote Code Execution
- **File**: `CVE-2020-11978_1.yaml`
- **Author**: pdteam
- **Tags**: packetstorm,cve,cve2020,apache,airflow,rce,kev
- **Description**: Apache Airflow versions 1.10.10 and below are vulnerable to remote code/command injection vulnerabilities in one of the example DAGs shipped with Airflow. This could allow any authenticated user to ru...

#### Apache Cocoon 2.1.12 - XML Injection
- **File**: `CVE-2020-11991_1.yaml`
- **Author**: pikpikcu
- **Tags**: cve,cve2020,apache,xml,cocoon,xxe
- **Description**: Apache Cocoon 2.1.12 is susceptible to  XML injection. When using the StreamGenerator, the code parses a user-provided XML. A specially crafted XML, including external system entities, can be used to ...

#### Apache Flink 1.5.1 - Local File Inclusion
- **File**: `CVE-2020-17518.yaml`
- **Author**: pdteam
- **Tags**: lfi,flink,fileupload,vulhub,cve,cve2020,apache,intrusive
- **Description**: Apache Flink 1.5.1 is vulnerable to local file inclusion because of a REST handler that allows file uploads to an arbitrary location on the local file system through a maliciously modified HTTP HEADER...

#### Apache Flink - Local File Inclusion
- **File**: `CVE-2020-17519.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2020,apache,lfi,flink
- **Description**: Apache Flink 1.11.0 (and released in 1.11.1 and 1.11.2 as well) allows attackers to read any file on the local filesystem of the JobManager through the REST interface of the JobManager process (aka lo...

#### Apache Airflow <1.10.14 - Authentication Bypass
- **File**: `CVE-2020-17526.yaml`
- **Author**: piyushchhiroliya
- **Tags**: cve,cve2020,apache,airflow,auth-bypass
- **Description**: Apache Airflow prior to 1.10.14 contains an authentication bypass vulnerability via incorrect session validation with default configuration. An attacker on site A can access unauthorized Airflow on si...

#### Apache Kylin 3.0.1 - Command Injection Vulnerability
- **File**: `CVE-2020-1956_1.yaml`
- **Author**: iamnoooob,rootxharsh,pdresearch
- **Tags**: cve,cve2020,apache,kylin,rce,oast,kev
- **Description**: Apache Kylin 2.3.0, and releases up to 2.6.5 and 3.0.1 has some restful apis which will concatenate os command with the user input string, a user is likely to be able to execute any os command without...

#### Apache Tomcat Remote Command Execution
- **File**: `CVE-2020-9484_1.yaml`
- **Author**: dwisiswant0
- **Tags**: rce,packetstorm,cve,cve2020,apache,tomcat
- **Description**: When using Apache Tomcat versions 10.0.0-M1 to 10.0.0-M4, 9.0.0.M1 to 9.0.34, 8.5.0 to 8.5.54 and 7.0.0 to 7.0.103 if
a) an attacker is able to control the contents and name of a file on the server; a...

#### Apache 2.4.49 - Path Traversal and Remote Code Execution
- **File**: `CVE-2021-41773.yaml`
- **Author**: daffainfo,666asd
- **Tags**: cve,cve2021,lfi,rce,apache,misconfig,traversal,kev
- **Description**: A flaw was found in a change made to path normalization in Apache HTTP Server 2.4.49. An attacker could use a path traversal attack to map URLs to files outside the expected document root. If files ou...

#### Apache Airflow OS Command Injection
- **File**: `CVE-2022-24288_1.yaml`
- **Author**: xeldax
- **Tags**: cve,cve2022,airflow,rce
- **Description**: Apache Airflow prior to version 2.2.4 is vulnerable to OS command injection attacks because some example DAGs do not properly sanitize user-provided parameters, making them susceptible to OS Command I...

#### Apache Spark UI - Remote Command Injection
- **File**: `CVE-2022-33891.yaml`
- **Author**: princechaddha
- **Tags**: cve2022,apache,spark,authenticated,kev,packetstorm,cve
- **Description**: Apache Spark UI is susceptible to remote command injection. ACLs can be enabled via the configuration option spark.acls.enable. With an authentication filter, this checks whether a user has access per...

#### Apache ActiveMQ Default Login
- **File**: `activemq-default-login_1.yaml`
- **Author**: pdteam
- **Tags**: apache,activemq,default-login
- **Description**: Apache ActiveMQ default login information was discovered.

#### Apache Airflow Default Login
- **File**: `airflow-default-login_1.yaml`
- **Author**: pdteam
- **Tags**: airflow,default-login,apache
- **Description**: An Apache Airflow default login was discovered.

#### Apache Ambari Default Login
- **File**: `ambari-default-login_1.yaml`
- **Author**: pdteam
- **Tags**: ambari,default-login,apache
- **Description**: An Apache Ambari default admin login was discovered.

#### Apache Solr <= 8.8.1 Arbitrary File Read
- **File**: `apache-solr-file-read_1.yaml`
- **Author**: DhiyaneshDk
- **Tags**: apache,solr,lfi
- **Description**: No description

#### Apache Apisix Default Admin Login
- **File**: `apisix-default-login_1.yaml`
- **Author**: pdteam
- **Tags**: apisix,apache,default-login
- **Description**: An Apache Apisix default admin login was discovered.

#### Apache DolphinScheduler Default Login
- **File**: `dolphinscheduler-default-login_1.yaml`
- **Author**: For3stCo1d
- **Tags**: apache,dolphinscheduler,default-login,oss
- **Description**: Apache DolphinScheduler default admin credentials were discovered.

#### Apache Druid Default Login
- **File**: `druid-default-login_1.yaml`
- **Author**: pikpikcu
- **Tags**: druid,default-login
- **Description**: Apache Druid default login information (admin/admin) was discovered.

#### Apache Dubbo - Default Admin Discovery
- **File**: `dubbo-admin-default-login_1.yaml`
- **Author**: ritikchaddha
- **Tags**: dubbo,apache,default-login
- **Description**: Apache Dubbo default admin credentials were discovered.

#### Apache htpasswd Config - Detect
- **File**: `htpasswd-detection.yaml`
- **Author**: geeknik
- **Tags**: config,exposure
- **Description**: Apache htpasswd configuration was detected.

#### Apache Kafka Center Default Login
- **File**: `kafka-center-default-login_1.yaml`
- **Author**: dhiyaneshDK
- **Tags**: kafka,default-login
- **Description**: Apache Kafka Center default admin credentials were discovered.

#### Apache Karaf - Default Login
- **File**: `karaf-default-login.yaml`
- **Author**: s0obi
- **Tags**: default-login,apache,karaf
- **Description**: Apache Karaf contains a default login vulnerability. Default login credentials were detected. An attacker can obtain access to user accounts and access sensitive information, modify data, and/or execu...

#### Apache OfBiz Default Login
- **File**: `ofbiz-default-login_1.yaml`
- **Author**: pdteam
- **Tags**: ofbiz,default-login,apache
- **Description**: Apache OfBiz default admin credentials were discovered.

#### Apache Ranger - Default Login
- **File**: `ranger-default-login_1.yaml`
- **Author**: For3stCo1d
- **Tags**: apache,ranger,default-login
- **Description**: Apache Ranger contains a default login vulnerability. An attacker can obtain access to user accounts and access sensitive information, modify data, and/or execute unauthorized operations.

#### Apache Tomcat Manager Default Login
- **File**: `tomcat-default-login_1.yaml`
- **Author**: pdteam,sinKettu
- **Tags**: tomcat,apache,default-login
- **Description**: Apache Tomcat Manager default login credentials were discovered. This template checks for multiple variations.

#### Unauthenticated Airflow Instance
- **File**: `unauthenticated-airflow_1.yaml`
- **Author**: dhiyaneshDK
- **Tags**: apache,airflow,unauth
- **Description**: No description

#### Apache ActiveMQ Default Login
- **File**: `activemq-default-login_2.yaml`
- **Author**: pdteam
- **Tags**: apache,activemq,default-login
- **Description**: Apache ActiveMQ default login information was discovered.

#### Apache Ambari Default Login
- **File**: `ambari-default-login_2.yaml`
- **Author**: pdteam
- **Tags**: ambari,default-login,apache
- **Description**: An Apache Ambari default admin login was discovered.

#### Apache Airflow Default Login
- **File**: `airflow-default-login_2.yaml`
- **Author**: pdteam
- **Tags**: airflow,default-login,apache
- **Description**: An Apache Airflow default login was discovered.

#### Apache Apisix Default Admin Login
- **File**: `apisix-default-login_2.yaml`
- **Author**: pdteam
- **Tags**: apisix,apache,default-login
- **Description**: An Apache Apisix default admin login was discovered.

#### Apache DolphinScheduler Default Login
- **File**: `dolphinscheduler-default-login_2.yaml`
- **Author**: For3stCo1d
- **Tags**: apache,dolphinscheduler,default-login,oss
- **Description**: Apache DolphinScheduler default admin credentials were discovered.

#### Apache Dubbo - Default Admin Discovery
- **File**: `dubbo-admin-default-login_2.yaml`
- **Author**: ritikchaddha
- **Tags**: dubbo,apache,default-login
- **Description**: Apache Dubbo default admin credentials were discovered.

#### Apache Kafka Center Default Login
- **File**: `kafka-center-default-login_2.yaml`
- **Author**: dhiyaneshDK
- **Tags**: kafka,default-login
- **Description**: Apache Kafka Center default admin credentials were discovered.

#### Apache Karaf - Default Login
- **File**: `karaf-default-login_1.yaml`
- **Author**: s0obi
- **Tags**: default-login,apache,karaf
- **Description**: Apache Karaf contains a default login vulnerability. Default login credentials were detected. An attacker can obtain access to user accounts and access sensitive information, modify data, and/or execu...

#### Apache Kylin Console - Default Login
- **File**: `kylin-default-login.yaml`
- **Author**: SleepingBag945
- **Tags**: kylin,default-login,apache
- **Description**: The default password for the Apache Kylin Console is KYLIN for the ADMIN user in Kylin versions before 3.0.0.


#### Apache Ranger - Default Login
- **File**: `ranger-default-login_2.yaml`
- **Author**: For3stCo1d
- **Tags**: apache,ranger,default-login
- **Description**: Apache Ranger contains a default login vulnerability. An attacker can obtain access to user accounts and access sensitive information, modify data, and/or execute unauthorized operations.

#### Apache Tomcat Manager Default Login
- **File**: `tomcat-default-login_2.yaml`
- **Author**: pdteam,sinKettu,nybble04
- **Tags**: tomcat,apache,default-login
- **Description**: Apache Tomcat Manager default login credentials were discovered. This template checks for multiple variations.

#### Apache OfBiz Default Login
- **File**: `ofbiz-default-login_2.yaml`
- **Author**: pdteam
- **Tags**: ofbiz,default-login,apache
- **Description**: Apache OfBiz default admin credentials were discovered.

#### Remote Command Execution ( Apache Struts S2-016)
- **File**: `apache-Struts-S2-016-rce.yaml`
- **Author**: j4v40n654n
- **Tags**: apache, rce
- **Description**: No description

#### ApacheSuperset - Default Login
- **File**: `apache-superset-login-extended.yaml`
- **Author**: dordyan, gtrrnr
- **Tags**: default-login,superset
- **Description**: ApacheSuperset contains a default login vulnerability. An attacker can obtain access to user accounts and access sensitive information, modify data, and/or execute unauthorized operations.

#### Apache Solr <= 8.8.1 Arbitrary File Read
- **File**: `custom-solr-file-read.yaml`
- **Author**: 0xParthJ
- **Tags**: apache,solr,lfi
- **Description**: No description

#### Solr Apache Path Traversal
- **File**: `custom-solr-path-traversal.yaml`
- **Author**: 0xParthJ
- **Tags**: solr,unauth
- **Description**: No description

#### VMWare-VSphere-Arbitrary File Read
- **File**: `custom-vmware-vsphere-file-read.yaml`
- **Author**: 0xParthJ
- **Tags**: apache,solr,lfi
- **Description**: No description

### Medium Severity (37 templates)

#### Apache ActiveMQ Default Login
- **File**: `activemq-default-login.yaml`
- **Author**: pdteam
- **Tags**: apache,activemq,default-login
- **Description**: Apache ActiveMQ default login information was discovered.

#### Apache Airflow Configuration Exposure
- **File**: `airflow-configuration-exposure.yaml`
- **Author**: pdteam
- **Tags**: exposure,config,airflow,apache
- **Description**: No description

#### Apache Ambari Default Credentials
- **File**: `ambari-default-credentials.yaml`
- **Author**: pdteam
- **Tags**: ambari,default-login
- **Description**: No description

#### Apache Ambari Exposure Admin Login Panel
- **File**: `ambari-exposure.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,ambari,exposure
- **Description**: An Apache Ambari panel was discovered.

#### Apache PageSpeed Global Admin Dashboard Exposure
- **File**: `exposed-pagespeed-global-admin.yaml`
- **Author**: pdteam
- **Tags**: panel
- **Description**: No description

#### Apache OfBiz Default Credentials
- **File**: `ofbiz-default-credentials.yaml`
- **Author**: pdteam
- **Tags**: ofbiz,default-login
- **Description**: No description

#### Apache OfBiz Default Login
- **File**: `ofbiz-default-login.yaml`
- **Author**: pdteam
- **Tags**: ofbiz,default-login,apache
- **Description**: Apache OfBiz default admin credentials were discovered.

#### Apache mod_perl Status Page Exposure
- **File**: `perl-status.yaml`
- **Author**: pdteam
- **Tags**: config,exposure,apache,status
- **Description**: No description

#### Apache Solr Exposure
- **File**: `solr-exposure.yaml`
- **Author**: pdteam
- **Tags**: panel,solr,apache
- **Description**: No description

#### Apache Hbase Unauth
- **File**: `apache-hbase-unauth.yaml`
- **Author**: pikpikcu
- **Tags**: apache,unauth,misconfig
- **Description**: No description

#### Apache Storm Unauth
- **File**: `apache-storm-unauth.yaml`
- **Author**: pikpikcu
- **Tags**: apache,unauth,misconfig
- **Description**: No description

#### Apache mod_userdir CRLF injection
- **File**: `CVE-2016-4975.yaml`
- **Author**: melbadry9,nadino,xElkomy
- **Tags**: cve,cve2016,crlf,generic,apache
- **Description**: Apache CRLF injection allowing HTTP response splitting attacks on sites using mod_userdir.

#### Apache Tomcat JK Status Manager Access
- **File**: `CVE-2018-11759-1.yaml`
- **Author**: harshbothra_
- **Tags**: cve,cve2018,apache
- **Description**: No description

#### Apache Tomcat JK Status Manager Access
- **File**: `CVE-2018-11759-2.yaml`
- **Author**: harshbothra_
- **Tags**: cve,cve2018,apache
- **Description**: No description

#### Apache Tomcat - Open Redirect
- **File**: `CVE-2018-11784.yaml`
- **Author**: geeknik
- **Tags**: tomcat,redirect,cve,cve2018,apache
- **Description**: Apache Tomcat versions prior to 9.0.12, 8.5.34, and 7.0.91 are prone to an open-redirection vulnerability because it fails to properly sanitize user-supplied input.

#### Apache ActiveMQ XSS
- **File**: `CVE-2018-8006.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2018,apache,activemq,xss
- **Description**: An instance of a cross-site scripting vulnerability was identified to be present in the web based administration console on the queue.jsp page of Apache ActiveMQ versions 5.0.0 to 5.15.5. The root cau...

#### Apache Tomcat XSS
- **File**: `CVE-2019-0221.yaml`
- **Author**: pikpikcu
- **Tags**: cve,cve2019,apache,xss,tomcat
- **Description**: The SSI printenv command in Apache Tomcat 9.0.0.M1 to 9.0.0.17, 8.5.0 to 8.5.39 and
7.0.0 to 7.0.93 echoes user provided data without escaping and is,
therefore, vulnerable to XSS. SSI is disabled by ...

#### Apache mod_proxy HTML Injection / Partial XSS
- **File**: `CVE-2019-10092.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2019,apache,htmli,injection
- **Description**: In Apache HTTP Server 2.4.0-2.4.39, a limited cross-site scripting issue was reported affecting the mod_proxy error page. An attacker could cause the link on the error page to be malformed and instead...

#### Apache Kylin Exposed Configuration File
- **File**: `CVE-2020-13937.yaml`
- **Author**: pikpikcu
- **Tags**: 
- **Description**: Apache Kylin 2.0.0, 2.1.0, 2.2.0, 2.3.0, 2.3.1, 2.3.2, 2.4.0, 2.4.1, 2.5.0, 2.5.1, 2.5.2, 2.6.0, 2.6.1, 2.6.2, 2.6.3, 2.6.4, 2.6.5, 2.6.6, 3.0.0-alpha, 3.0.0-alpha2, 3.0.0-beta, 3.0.0, 3.0.1,  3.0.2, ...

#### Apache OFBiz Reflected XSS
- **File**: `CVE-2020-1943.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2020,apache,xss,ofbiz
- **Description**: Data sent with contentId to /control/stream is not sanitized, allowing XSS attacks in Apache OFBiz 16.11.01 to 16.11.07.

#### Apache OFBiz XML-RPC Java Deserialization
- **File**: `CVE-2020-9496.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,apache,java,ofbiz
- **Description**: XML-RPC request are vulnerable to unsafe deserialization and Cross-Site Scripting issues in Apache OFBiz 17.12.03

#### Apache Server Status Check
- **File**: `server-status-localhost_1.yaml`
- **Author**: 0xr2r (https://twitter.com/x0xr2r)
- **Tags**: server-info, server-status, balancer-manager, apache, information
- **Description**: Apache Server Status page is exposed, which may contain information about pages visited by the users, their IPs or sensitive information such as session tokens.

#### Apache Kylin - Exposed Configuration File
- **File**: `CVE-2020-13937_1.yaml`
- **Author**: pikpikcu
- **Tags**: cve,cve2020,apache
- **Description**: Apache Kylin 2.0.0, 2.1.0, 2.2.0, 2.3.0, 2.3.1, 2.3.2, 2.4.0, 2.4.1, 2.5.0, 2.5.1, 2.5.2, 2.6.0, 2.6.1, 2.6.2, 2.6.3, 2.6.4, 2.6.5, 2.6.6, 3.0.0-alpha, 3.0.0-alpha2, 3.0.0-beta, 3.0.0, 3.0.1,  3.0.2, ...

#### Apache APISIX - Insufficiently Protected Credentials
- **File**: `CVE-2020-13945_1.yaml`
- **Author**: pdteam
- **Tags**: intrusive,vulhub,packetstorm,cve,cve2020,apache,apisix
- **Description**: Apache APISIX 1.2, 1.3, 1.4, and 1.5 is susceptible to insufficiently protected credentials. An attacker can enable the Admin API and delete the Admin API access IP restriction rules. Eventually, the ...

#### Apache OFBiz <=16.11.07 - Cross-Site Scripting
- **File**: `CVE-2020-1943_1.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2020,apache,xss,ofbiz
- **Description**: Apache OFBiz 16.11.01 to 16.11.07 is vulnerable to cross-site scripting because data sent with contentId to /control/stream is not sanitized.

#### Apache OFBiz 17.12.03 - Cross-Site Scripting
- **File**: `CVE-2020-9496_1.yaml`
- **Author**: dwisiswant0
- **Tags**: ofbiz,packetstorm,cve,cve2020,apache,java
- **Description**: Apache OFBiz 17.12.03 contains cross-site scripting and unsafe deserialization vulnerabilities via an XML-RPC request.

#### Apache Druid - Local File Inclusion
- **File**: `CVE-2021-36749.yaml`
- **Author**: _0xf4n9x_
- **Tags**: cve,cve2021,apache,lfi,auth-bypass,druid
- **Description**: Apache Druid ingestion system is vulnerable to local file inclusion. The InputSource is used for reading data from a certain data source. However, the HTTP InputSource allows authenticated users to re...

#### Apache Superset <=1.3.2 - Default Login
- **File**: `CVE-2021-44451_1.yaml`
- **Author**: dhiyaneshDK
- **Tags**: cve,cve2021,apache,superset,default-login
- **Description**: Apache Superset through 1.3.2 contains a default login vulnerability via registered database connections for authenticated users. An attacker can obtain access to user accounts and thereby obtain sens...

#### Apache ShardingSphere ElasticJob-UI privilege escalation
- **File**: `CVE-2022-22733.yaml`
- **Author**: Zeyad Azima
- **Tags**: cve,cve2023,exposure,sharingsphere,apache
- **Description**: Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache ShardingSphere ElasticJob-UI allows an attacker who has guest account to do privilege escalation. This issue affects ...

#### Apache Airflow Configuration Page - Detect
- **File**: `airflow-configuration-exposure_1.yaml`
- **Author**: pdteam
- **Tags**: exposure,config,airflow,apache
- **Description**: Apache Airflow configuration page was detected.

#### Apache Configuration File - Detect
- **File**: `apache-config_1.yaml`
- **Author**: sheikhrishad
- **Tags**: config,exposure,apache
- **Description**: Apache configuration file was detected.

#### Apache Hbase Unauth
- **File**: `apache-hbase-unauth_1.yaml`
- **Author**: pikpikcu
- **Tags**: apache,unauth,misconfig
- **Description**: No description

#### Apache Server Status Check
- **File**: `apache-server-status-check.yaml`
- **Author**: SirBugs
- **Tags**: 
- **Description**: No description

#### Apache Storm Unauth
- **File**: `apache-storm-unauth_1.yaml`
- **Author**: pikpikcu
- **Tags**: apache,unauth,misconfig
- **Description**: No description

#### Jenkins Open User registration
- **File**: `jenkins-openuser-register.yaml`
- **Author**: DhiyaneshDk
- **Tags**: misconfig,jenkins,apache,tomcat
- **Description**: The Jenkins allows registering a new user and accessing the dashboard.

#### Apache Mod_perl Status Page - Detect
- **File**: `perl-status_1.yaml`
- **Author**: pdteam
- **Tags**: config,exposure,apache,status
- **Description**: Apache mod_perl status page was detected.

#### Apache Solr Exposure
- **File**: `solr-exposure_1.yaml`
- **Author**: pdteam
- **Tags**: panel,solr,apache
- **Description**: No description

### Low Severity (46 templates)

#### Airflow Debug Trace
- **File**: `airflow-debug.yaml`
- **Author**: pdteam
- **Tags**: apache,airflow,fpd
- **Description**: No description

#### Apache CouchDB Fauxton Exposure
- **File**: `couchdb-fauxton.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,couchdb
- **Description**: No description

#### Apache Flink Exposure
- **File**: `flink-exposure.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,flink
- **Description**: No description

#### Apache Hadoop Exposure
- **File**: `hadoop-exposure.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,hadoop
- **Description**: No description

#### Apache Hadoop Unauth
- **File**: `hadoop-unauth-1.yaml`
- **Author**: pdteam
- **Tags**: apache,hadoop,unauth
- **Description**: No description

#### Apache Hadoop Unauth
- **File**: `hadoop-unauth-2.yaml`
- **Author**: pdteam
- **Tags**: apache,hadoop,unauth
- **Description**: No description

#### Apache Hadoop Unauth
- **File**: `hadoop-unauth.yaml`
- **Author**: pdteam
- **Tags**: apache,hadoop,unauth
- **Description**: No description

#### Apache Kafka Connect UI Exposure
- **File**: `kafka-connect-ui.yaml`
- **Author**: pdteam
- **Tags**: panel,kafka,apache
- **Description**: No description

#### Apache Kafka Monitor Exposure
- **File**: `kafka-monitoring.yaml`
- **Author**: pdteam
- **Tags**: panel,kafka,apache
- **Description**: No description

#### Apache Kafka Topics UI Exposure
- **File**: `kafka-topics-ui.yaml`
- **Author**: pdteam
- **Tags**: panel,kafka,apache
- **Description**: No description

#### Server Status Disclosure
- **File**: `server-status-localhost.yaml`
- **Author**: pdteam,geeknik
- **Tags**: apache,debug
- **Description**: No description

#### Server Status Disclosure
- **File**: `server-status.yaml`
- **Author**: pdteam,geeknik
- **Tags**: apache,debug
- **Description**: No description

#### Apache Struts setup in Debug-Mode
- **File**: `struts-debug-mode.yaml`
- **Author**: pdteam
- **Tags**: logs,struts,apache,exposure,setup
- **Description**: No description

#### Apache Struts in Dev Mode
- **File**: `struts-problem-report.yaml`
- **Author**: dhiyaneshDK
- **Tags**: exposure,apache,struts,debug
- **Description**: No description

#### Apache Yarn ResourceManager Exposure / Unauthenticated Access
- **File**: `yarn-manager-exposure.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,yarn,exposure
- **Description**: No description

#### Apache Yarn ResourceManager RCE
- **File**: `yarn-resourcemanager-rce.yaml`
- **Author**: pdteam
- **Tags**: apache,rce
- **Description**: A vulnerability in Apache Yarn ResourceManager allows remote unauthenticated users to cause the product to execute arbitrary code.

#### Apache Config file disclosure
- **File**: `apache-config.yaml`
- **Author**: sheikhrishad
- **Tags**: config,exposure,apache
- **Description**: No description

#### Apache Filename Brute Force
- **File**: `apache-filename-brute-force.yaml`
- **Author**: geeknik
- **Tags**: apache
- **Description**: If the client provides an invalid Accept header, the server will respond with a 406 Not Acceptable error containing a pseudo directory listing.

#### Apache Filename Enumeration
- **File**: `apache-filename-enum.yaml`
- **Author**: geeknik
- **Tags**: apache,misconfig
- **Description**: If the client provides an invalid Accept header, the server will respond with a 406 Not Acceptable error containing a pseudo directory listing.

#### Apache Tomcat example - snoop - Insecure Cookie Handling
- **File**: `apache-tomcat-snoop-cookie-handling.yaml`
- **Author**: wasp76b
- **Tags**: apache,misconfig,tomcat,disclosure
- **Description**: No description

#### Apache Tomcat example - snoop - Internal IP disclosure
- **File**: `apache-tomcat-snoop-ip-disclosure.yaml`
- **Author**: wasp76b
- **Tags**: apache,misconfig,tomcat,disclosure
- **Description**: No description

#### Apache Tomcat example page disclosure - snoop
- **File**: `apache-tomcat-snoop.yaml`
- **Author**: pdteam
- **Tags**: apache,misconfig,tomcat,disclosure
- **Description**: The following example scripts that come with Apache Tomcat v4.x - v7.x and can be used by attackers to gain information about the system. These scripts are also known to be vulnerable to cross site sc...

#### Detect Tomcat Exposed Scripts
- **File**: `tomcat-scripts.yaml`
- **Author**: Co0nan
- **Tags**: apache,tomcat
- **Description**: No description

#### Apache Struts - Multiple Open Redirection Vulnerabilities
- **File**: `CVE-2013-2248.yaml`
- **Author**: 0x_Akoko
- **Tags**: cve,cve2013,apache,redirect,struts
- **Description**: Apache Struts is prone to multiple open-redirection vulnerabilities because the application fails to properly sanitize user-supplied input.

#### Check Apache Server Info
- **File**: `apache-server-info.yml`
- **Author**: DoubleTake (https://twitter.com/LeDoubleTake)
- **Tags**: server-info, server-status, balancer-manager, apache, information
- **Description**: This template checks if the some Apache endpoints can leak information like "Server Version".

#### Apache Server Status Exposure
- **File**: `apache-server-status.yaml`
- **Author**: pdteam
- **Tags**: 
- **Description**: No description

#### Apache Struts CVE-2013-2248 Multiple Open Redirection Vulnerabilities
- **File**: `CVE-2013-2248_1.yaml`
- **Author**: 0x_Akoko
- **Tags**: apache,redirect
- **Description**: Apache Struts is prone to multiple open-redirection vulnerabilities because the application fails to properly sanitize user-supplied input.

#### Apache Struts CVE-2013-2248 Multiple Open Redirection Vulnerabilities
- **File**: `CVE-2013-2248_2.yaml`
- **Author**: 0x_Akoko
- **Tags**: apache,redirect
- **Description**: Apache Struts is prone to multiple open-redirection vulnerabilities because the application fails to properly sanitize user-supplied input.

#### Airflow Debug Trace
- **File**: `airflow-debug_1.yaml`
- **Author**: pdteam
- **Tags**: apache,airflow,fpd
- **Description**: No description

#### Apache Drill Exposure
- **File**: `apache-drill-exposure.yaml`
- **Author**: DhiyaneshDK
- **Tags**: misconfig,exposure,apache,drill
- **Description**: No description

#### Apache Druid Unauth
- **File**: `apache-druid-unauth.yaml`
- **Author**: DhiyaneshDk
- **Tags**: misconfig,druid,unauth,apache
- **Description**: No description

#### Apache Filename Enumeration
- **File**: `apache-filename-enum_1.yaml`
- **Author**: geeknik
- **Tags**: apache,misconfig
- **Description**: If the client provides an invalid Accept header, the server will respond with a 406 Not Acceptable error containing a pseudo directory listing.

#### Apache License File
- **File**: `apache-licenserc.yaml`
- **Author**: DhiyaneshDk
- **Tags**: exposure,file,apache
- **Description**: No description

#### Apache Nifi-Unauthenticated
- **File**: `apache-nifi-unauth.yaml`
- **Author**: notnotnotveg
- **Tags**: 
- **Description**: No description

#### Apache Server Status Page
- **File**: `apache-serverstatus.yaml`
- **Author**: notnotnotveg
- **Tags**: 
- **Description**: No description

#### Apache Struts - ShowCase Application Exposure
- **File**: `apache-struts-showcase.yaml`
- **Author**: DhiyaneshDK
- **Tags**: apache,struts,showcase,misconfig,exposure
- **Description**: No description

#### Apache Tomcat example page disclosure - snoop
- **File**: `apache-tomcat-snoop_1.yaml`
- **Author**: pdteam
- **Tags**: apache,misconfig,tomcat,disclosure
- **Description**: The following example scripts that come with Apache Tomcat v4.x - v7.x and can be used by attackers to gain information about the system. These scripts are also known to be vulnerable to cross site sc...

#### Apache Hadoop Unauth
- **File**: `hadoop-unauth_1.yaml`
- **Author**: pdteam
- **Tags**: apache,hadoop,unauth
- **Description**: No description

#### Kafka Manager Panel - Unauthorized Access
- **File**: `kafka-manager-unauth.yaml`
- **Author**: Paper-Pen
- **Tags**: misconfig,apache,kafka,unauth,exposure
- **Description**: A kafka manager unauthorized access was discovered.

#### Server Status Disclosure
- **File**: `server-status-localhost_2.yaml`
- **Author**: pdteam,geeknik
- **Tags**: apache,debug
- **Description**: No description

#### Apache Struts setup in Debug-Mode
- **File**: `struts-debug-mode_1.yaml`
- **Author**: pdteam
- **Tags**: logs,struts,apache,exposure,setup
- **Description**: No description

#### Apache Struts Dev Mode - Detect
- **File**: `struts-problem-report_1.yaml`
- **Author**: dhiyaneshDK
- **Tags**: struts,debug,edb,exposure,apache
- **Description**: Multiple Apache Struts applications were detected in dev-mode.

#### Tomcat Cookie Exposed
- **File**: `tomcat-cookie-exposed.yaml`
- **Author**: tess,dk999
- **Tags**: misconfig,apache,tomcat,exposure
- **Description**: No description

#### Apache YARN ResourceManager Panel - Detect
- **File**: `yarn-manager-exposure_1.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,yarn,exposure
- **Description**: Apache YARN ResourceManager panel was detected.

#### Apache Yarn ResourceManager RCE
- **File**: `yarn-resourcemanager-rce_1.yaml`
- **Author**: pdteam
- **Tags**: apache,rce
- **Description**: A vulnerability in Apache Yarn ResourceManager allows remote unauthenticated users to cause the product to execute arbitrary code.

#### Apache YARN ResourceManager Panel - Detect
- **File**: `yarn-manager-exposure_2.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,yarn,exposure
- **Description**: Apache YARN ResourceManager panel was detected.

### Info Severity (68 templates)

#### Apache ActiveMQ Exposure
- **File**: `activemq-panel.yaml`
- **Author**: pdteam
- **Tags**: panel,activemq,apache
- **Description**: An Apache ActiveMQ implementation was discovered.

#### Apache Airflow
- **File**: `airflow-detect.yaml`
- **Author**: pdteam
- **Tags**: tech,apache,airflow
- **Description**: No description

#### Apache Airflow Admin Login Panel
- **File**: `airflow-panel.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,airflow,admin
- **Description**: An Apache Airflow admin login panel was discovered.

#### Axis Happyaxis Exposure
- **File**: `axis-happyaxis-1.yaml`
- **Author**: dogasantos
- **Tags**: axis,axis2,middleware,exposure,apache
- **Description**: No description

#### Axis Happyaxis Exposure
- **File**: `axis-happyaxis-2.yaml`
- **Author**: dogasantos
- **Tags**: axis,axis2,middleware,exposure,apache
- **Description**: No description

#### Axis Happyaxis Exposure
- **File**: `axis-happyaxis-3.yaml`
- **Author**: dogasantos
- **Tags**: axis,axis2,middleware,exposure,apache
- **Description**: No description

#### Axis Happyaxis Exposure
- **File**: `axis-happyaxis-4.yaml`
- **Author**: dogasantos
- **Tags**: axis,axis2,middleware,exposure,apache
- **Description**: No description

#### Axis Happyaxis Exposure
- **File**: `axis-happyaxis.yaml`
- **Author**: dogasantos
- **Tags**: axis,axis2,middleware,exposure,apache
- **Description**: No description

#### Apache NiFi detect
- **File**: `nifi-detech-1.yaml`
- **Author**: dwisiswant0
- **Tags**: 
- **Description**: No description

#### Apache NiFi detect
- **File**: `nifi-detech-2.yaml`
- **Author**: dwisiswant0
- **Tags**: 
- **Description**: No description

#### Apache NiFi detect
- **File**: `nifi-detech-3.yaml`
- **Author**: dwisiswant0
- **Tags**: 
- **Description**: No description

#### Apache NiFi detect
- **File**: `nifi-detech-4.yaml`
- **Author**: dwisiswant0
- **Tags**: 
- **Description**: No description

#### Apache NiFi detect
- **File**: `nifi-detech-5.yaml`
- **Author**: dwisiswant0
- **Tags**: 
- **Description**: No description

#### Apache NiFi detect
- **File**: `nifi-detech-6.yaml`
- **Author**: dwisiswant0
- **Tags**: 
- **Description**: No description

#### Apache NiFi detect
- **File**: `nifi-detech-7.yaml`
- **Author**: dwisiswant0
- **Tags**: 
- **Description**: No description

#### Apache NiFi detect
- **File**: `nifi-detech.yaml`
- **Author**: dwisiswant0
- **Tags**: tech,apache,nifi
- **Description**: No description

#### Node RED Detect
- **File**: `node-red-detect.yaml`
- **Author**: pikpikcu
- **Tags**: tech,apache,node-red-dashboard
- **Description**: No description

#### Apache Ranger Detection
- **File**: `ranger-detection.yaml`
- **Author**: For3stCo1d
- **Tags**: tech,apache,ranger
- **Description**: No description

#### Apache RocketMQ Console Exposure
- **File**: `rocketmq-console-exposure.yaml`
- **Author**: pdteam
- **Tags**: panel,apache
- **Description**: No description

#### XAMPP Default Page
- **File**: `xampp-default-page.yaml`
- **Author**: dhiyaneshDK
- **Tags**: tech,php,xampp,apache
- **Description**: No description

#### Apache APISIX Login Panel
- **File**: `apache-apisix-panel.yaml`
- **Author**: pikpikcu
- **Tags**: apache,apisix,panel
- **Description**: An Apache APISIX login panel was detected.

#### apache-axis-detect
- **File**: `apache-axis-detect-1.yaml`
- **Author**: dogasantos
- **Tags**: tech,axis2,middleware,apache
- **Description**: Axis and Axis2 detection

#### apache-axis-detect
- **File**: `apache-axis-detect-2.yaml`
- **Author**: dogasantos
- **Tags**: tech,axis2,middleware,apache
- **Description**: Axis and Axis2 detection

#### apache-axis-detect
- **File**: `apache-axis-detect-3.yaml`
- **Author**: dogasantos
- **Tags**: tech,axis2,middleware,apache
- **Description**: Axis and Axis2 detection

#### apache-axis-detect
- **File**: `apache-axis-detect.yaml`
- **Author**: dogasantos
- **Tags**: tech,axis2,middleware,apache
- **Description**: Axis and Axis2 detection

#### Apache Cocoon detect
- **File**: `apache-cocoon-detect.yaml`
- **Author**: ffffffff0x
- **Tags**: apache,cocoon,tech
- **Description**: No description

#### Apache dubbo detect
- **File**: `apache-dubbo-detect.yaml`
- **Author**: ffffffff0x
- **Tags**: apache,dubbo,tech
- **Description**: No description

#### Apache Guacamole Login Page and version detection
- **File**: `apache-guacamole.yaml`
- **Author**: r3dg33k
- **Tags**: apache,guacamole,tech,login
- **Description**: No description

#### Apache Tapestry Framework detect
- **File**: `apache-tapestry-detect.yaml`
- **Author**: pikpikcu
- **Tags**: apache,tapestry,tech
- **Description**: No description

#### Apache Zeppelin detect
- **File**: `apache-zeppelin-detect.yaml`
- **Author**: pikpikcu
- **Tags**: apache,zeppelin,tech
- **Description**: No description

#### Apache HTTP Server Test Page
- **File**: `default-apache-test-page.yaml`
- **Author**: dhiyaneshDk
- **Tags**: tech,apache
- **Description**: No description

#### Apache Tomcat Manager Disclosure
- **File**: `public-tomcat-manager.yaml`
- **Author**: Ahmed Sherif,geeknik
- **Tags**: panel,tomcat,apache
- **Description**: An Apache Tomcat Manager panel was discovered.

#### Tomcat Detection
- **File**: `tomcat-detect.yaml`
- **Author**: philippedelteil,dhiyaneshDk
- **Tags**: tech,tomcat,apache
- **Description**: If an Tomcat instance is deployed on the target URL, when we send a request for a non existent resource we receive a Tomcat error page with version.

#### Tomcat Manager Path Normalization
- **File**: `tomcat-pathnormalization.yaml`
- **Author**: organiccrap
- **Tags**: panel,tomcat,apache
- **Description**: A Tomcat Manager login panel was discovered via path normalization. Normalizing a path involves modifying the string that identifies a path or file so that it conforms to a valid path on the target op...

#### Detect Tomcat Exposed Scripts
- **File**: `tomcat-scripts-1.yaml`
- **Author**: Co0nan
- **Tags**: apache
- **Description**: No description

#### Detect Tomcat Exposed Scripts
- **File**: `tomcat-scripts-2.yaml`
- **Author**: Co0nan
- **Tags**: apache
- **Description**: No description

#### Detect Tomcat Exposed Scripts
- **File**: `tomcat-scripts-3.yaml`
- **Author**: Co0nan
- **Tags**: apache
- **Description**: No description

#### Detect Tomcat Exposed Scripts
- **File**: `tomcat-scripts-4.yaml`
- **Author**: Co0nan
- **Tags**: apache
- **Description**: No description

#### Detect Tomcat Exposed Scripts
- **File**: `tomcat-scripts-5.yaml`
- **Author**: Co0nan
- **Tags**: apache
- **Description**: No description

#### Detect Tomcat Exposed Scripts
- **File**: `tomcat-scripts-6.yaml`
- **Author**: Co0nan
- **Tags**: apache
- **Description**: No description

#### Apache Druid Detection
- **File**: `apache-druid-detect.yaml`
- **Author**: h0tak88r
- **Tags**: 
- **Description**: No description

#### Apache Load Balancer Manager
- **File**: `apache-loadbalancer.yaml`
- **Author**: h0tak88r
- **Tags**: 
- **Description**: No description

#### Apache Axis2
- **File**: `axis2-detect.yaml`
- **Author**: notnotnotveg
- **Tags**: 
- **Description**: No description

#### Apache httpd Config File - Detect
- **File**: `httpd-config.yaml`
- **Author**: sheikhrishad
- **Tags**: config,exposure,httpd
- **Description**: Apache httpd configuration information was detected.

#### Detect Tomcat Exposed Scripts
- **File**: `tomcat-scripts_1.yaml`
- **Author**: Co0nan
- **Tags**: apache,tomcat
- **Description**: No description

#### Apache ActiveMQ Exposure
- **File**: `activemq-panel_1.yaml`
- **Author**: pdteam
- **Tags**: panel,activemq,apache
- **Description**: An Apache ActiveMQ implementation was discovered.

#### Apache Airflow Admin Login Panel
- **File**: `airflow-panel_1.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,airflow,admin
- **Description**: An Apache Airflow admin login panel was discovered.

#### Apache Ambari Exposure Admin Login Panel
- **File**: `ambari-exposure_1.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,ambari,exposure
- **Description**: An Apache Ambari panel was discovered.

#### Apache APISIX Login Panel
- **File**: `apache-apisix-panel_1.yaml`
- **Author**: pikpikcu
- **Tags**: apache,apisix,panel
- **Description**: An Apache APISIX login panel was detected.

#### Apache JMeter Dashboard Login Panel - Detect
- **File**: `apache-jmeter-dashboard.yaml`
- **Author**: tess
- **Tags**: apache,jmeter,panel
- **Description**: Apache JMeter Dashboard login panel was detected.

#### Apache Mesos - Panel Detect
- **File**: `apache-mesos-panel.yaml`
- **Author**: pikpikcu
- **Tags**: panel,apache,mesos
- **Description**: Apache Mesos panel was detected.

#### Apache CouchDB Panel - Detect
- **File**: `couchdb-exposure.yaml`
- **Author**: organiccrap
- **Tags**: panel,couchdb
- **Description**: Apache CouchDB panel was detected.

#### Apache CouchDB Fauxton Panel - Detect
- **File**: `couchdb-fauxton_1.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,couchdb
- **Description**: Apache CouchDB Fauxton panel was detected.

#### Eagle For Apache Kakfa Login - Detect
- **File**: `efak-login-panel.yaml`
- **Author**: irshad ahamed
- **Tags**: panel,efak,login,detect
- **Description**: EFAK is a visualization and management software that allows one to query, visualize, alert on, and explore their metrics wherever they were stored.


#### Apache Flink Login Panel - Detect
- **File**: `flink-exposure_1.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,flink
- **Description**: Apache Flink login panel was detected.

#### Apache Hadoop Panel - Detect
- **File**: `hadoop-exposure_1.yaml`
- **Author**: pdteam
- **Tags**: panel,apache,hadoop
- **Description**: Apache Hadoop panel was detected.

#### Apache Kafka Control Center Login Panel - Detect
- **File**: `kafka-center-login.yaml`
- **Author**: dhiyaneshDK
- **Tags**: panel,kafka
- **Description**: Apache Kafka Control Center login panel was detected.

#### Apache Kafka Connect UI Login Panel - Detect
- **File**: `kafka-connect-ui_1.yaml`
- **Author**: pdteam
- **Tags**: panel,kafka,apache
- **Description**: Apache Kafka Connect UI login panel was detected.

#### Apache Kafka Consumer Offset Monitor Panel - Detect
- **File**: `kafka-consumer-monitor.yaml`
- **Author**: dhiyaneshDK
- **Tags**: panel,kafka
- **Description**: Apache Kafka Consumer Offset Monitor panel was detected.

#### Apache Kafka Monitor Login Panel - Detect
- **File**: `kafka-monitoring_1.yaml`
- **Author**: pdteam
- **Tags**: panel,kafka,apache
- **Description**: Apache Kafka Monitor login panel was detected.

#### Apache Kafka Topics Panel - Detect
- **File**: `kafka-topics-ui_1.yaml`
- **Author**: pdteam
- **Tags**: panel,kafka,apache
- **Description**: Apache Kafka Topics panel was detected.

#### Apache Tomcat Manager Login Panel - Detect
- **File**: `public-tomcat-manager_1.yaml`
- **Author**: Ahmed Sherif,geeknik,sinKettu
- **Tags**: panel,tomcat,apache
- **Description**: Apache Tomcat Manager login panel was detected.

#### Apache RocketMQ Console Panel - Detect
- **File**: `rocketmq-console-exposure_1.yaml`
- **Author**: pdteam
- **Tags**: panel,apache
- **Description**: Apache RocketMQ Console panel was detected.

#### Apache Solr Admin Panel - Detect
- **File**: `solr-panel-exposure.yaml`
- **Author**: pdteam
- **Tags**: panel,solr,apache,admin
- **Description**: Apache Solr admin panel was detected.

#### Apache Spark Panel - Detect
- **File**: `spark-panel.yaml`
- **Author**: righettod
- **Tags**: panel,spark
- **Description**: Apache Spark panel was detected.

#### Apache Superset Login Panel - Detect
- **File**: `superset-login.yaml`
- **Author**: DhiyaneshDk
- **Tags**: panel,superset
- **Description**: Apache Superset login panel was detected.

#### Tomcat Manager Path Normalization
- **File**: `tomcat-pathnormalization_1.yaml`
- **Author**: organiccrap
- **Tags**: panel,tomcat,apache
- **Description**: No description

#### Apache Tomcat - Default Login Discovery
- **File**: `tomcat-examples-login.yaml`
- **Author**: 0xelkomy & C0NQR0R
- **Tags**: default-login,tomcat
- **Description**: Apache Tomcat 10.1.0-M1 to 10.1.0-M16, 10.0.0-M1 to 10.0.22, 9.0.30 to 9.0.64 and 8.5.50 to 8.5.81  default login credentials were successful.

