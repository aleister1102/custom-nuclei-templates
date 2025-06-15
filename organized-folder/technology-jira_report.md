# Technology Jira Templates

## Summary
- **Total templates**: 69
- **Category**: technology-jira

## Templates List

### Critical Severity (3 templates)

#### Jira 未授权服务端模板注入
- **File**: `CVE-2019-11581.yaml`
- **Author**: harris2015(https://github.com/harris2015)
- **Tags**: 
- **Description**: No description

#### Atlassian Jira - Authentication bypass in Seraph
- **File**: `CVE-2022-0540.yaml`
- **Author**: DhiyaneshDK 不动明王
- **Tags**: 
- **Description**: A vulnerability in Jira Seraph allows a remote, unauthenticated attacker to 
bypass authentication by sending a specially crafted HTTP 
request. This affects Atlassian Jira Server and Data Center vers...

#### Atlassian Jira Seraph - Authentication Bypass
- **File**: `CVE-2022-0540_1.yaml`
- **Author**: DhiyaneshDK
- **Tags**: cve,cve2022,atlassian,jira,exposure,auth-bypass
- **Description**: Jira Seraph allows a remote, unauthenticated attacker to bypass authentication by sending a specially crafted HTTP request. This affects Atlassian Jira Server and Data Center versions before 8.13.18, ...

### High Severity (4 templates)

#### Full-Read Server Side Request Forgery in Mobile Plugin for Jira Data Center and Server
- **File**: `CVE-2022-26135.yaml`
- **Author**: dk4trin
- **Tags**: cve,cve2022,atlassian,jira,ssrf
- **Description**: A vulnerability in Mobile Plugin for Jira Data Center and Server allows a remote, authenticated user (including a user who joined via the sign-up feature) to perform a full read server-side request fo...

#### STAGIL Navigation for Jira Menu & Themes <2.0.52 - Local File Inclusion
- **File**: `CVE-2023-26255.yaml`
- **Author**: DhiyaneshDK
- **Tags**: cve,cve2023,lfi,jira,cms,atlassian
- **Description**: STAGIL Navigation for Jira Menu & Themes plugin before 2.0.52 is susceptible to local file inclusion via modifying the fileName parameter to the snjCustomDesignConfig endpoint. An attacker can inject ...

#### STAGIL Navigation for Jira Menu & Themes <2.0.52 - Local File Inclusion
- **File**: `CVE-2023-26256.yaml`
- **Author**: pikpikcu
- **Tags**: cve,cve2023,lfi,jira,cms,atlassian
- **Description**: STAGIL Navigation for Jira Menu & Themes plugin before 2.0.52 is susceptible to local file inclusion via modifying the fileName parameter to the snjFooterNavigationConfig endpoint. An attacker can inj...

#### Atlassian JIRA Setup - Installer
- **File**: `jira-setup.yaml`
- **Author**: ritikchaddha
- **Tags**: misconfig,jira,atlassian,installer
- **Description**: No description

### Medium Severity (34 templates)

#### Jira Service Desk Signup
- **File**: `jira-service-desk-signup.yaml`
- **Author**: TechbrunchFR
- **Tags**: jira,atlassian,service
- **Description**: No description

#### Rainbow.Zen Jira XSS
- **File**: `CVE-2007-0885.yaml`
- **Author**: geeknik
- **Tags**: cve,cve2007,jira,xss
- **Description**: Cross-site scripting (XSS) vulnerability in jira/secure/BrowseProject.jspa in Rainbow with the Zen (Rainbow.Zen) extension allows remote attackers to inject arbitrary web script or HTML via the id par...

#### Atlassian Jira WallboardServlet XSS
- **File**: `CVE-2018-20824.yaml`
- **Author**: madrobot,dwisiswant0
- **Tags**: cve,cve2018,atlassian,jira,xss
- **Description**: The WallboardServlet resource in Jira before version 7.13.1 allows remote attackers to inject arbitrary HTML or JavaScript via a cross site scripting (XSS) vulnerability in the cyclePeriod parameter.

#### Atlassian JIRA Information Exposure (CVE-2019-3401)
- **File**: `CVE-2019-3401.yaml`
- **Author**: TechbrunchFR,milo2012
- **Tags**: cve,cve2019,jira,atlassian,exposure
- **Description**: The ManageFilters.jspa resource in Jira before version 7.13.3 and from version 8.0.0 before version 8.1.1 allows remote attackers to enumerate usernames via an incorrect authorisation check.

#### Jira - Reflected XSS using searchOwnerUserName parameter.
- **File**: `CVE-2019-3402.yaml`
- **Author**: pdteam
- **Tags**: cve,cve2019,atlassian,jira,xss
- **Description**: The ConfigurePortalPages.jspa resource in Jira before version 7.13.3 and from version 8.0.0 before version 8.1.1 allows remote attackers to inject arbitrary HTML or JavaScript via a cross site scripti...

#### User enumeration via an incorrect authorisation check
- **File**: `CVE-2019-3403.yaml`
- **Author**: Ganofins
- **Tags**: cve,cve2019,atlassian,jira
- **Description**: The /rest/api/2/user/picker rest resource in Jira before version 7.13.3, from version 8.0.0 before version 8.0.4, and from version 8.1.0 before version 8.1.1 allows remote attackers to enumerate usern...

#### Jira Improper Authorization
- **File**: `CVE-2019-8446.yaml`
- **Author**: dhiyaneshDk
- **Tags**: cve,cve2019,jira
- **Description**: The /rest/issueNav/1/issueTable resource in Jira before version 8.3.2 allows remote attackers to enumerate usernames via an incorrect authorisation check.

#### Jira Information Disclosure
- **File**: `CVE-2019-8449.yaml`
- **Author**: MaxSecurity(https://github.com/MaxSecurity)
- **Tags**: 
- **Description**: No description

#### Jira Information Disclosure
- **File**: `CVE-2020-14179.yaml`
- **Author**: harris2015(https://github.com/harris2015)
- **Tags**: 
- **Description**: No description

#### Jira Unauthorized User Enumeration
- **File**: `CVE-2020-14181.yaml`
- **Author**: whwlsfb(https://github.com/whwlsfb)
- **Tags**: 
- **Description**: No description

#### Pre-Auth Limited Arbitrary File Read in Jira Server
- **File**: `CVE-2020-29453 (copy 1).yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,atlassian,jira,lfi
- **Description**: The CachingResourceDownloadRewriteRule class in Jira Server and Jira Data Center allowed unauthenticated remote attackers to read arbitrary files within WEB-INF and META-INF directories via an incorre...

#### Pre-Auth Limited Arbitrary File Read in Jira Server
- **File**: `CVE-2020-29453-1.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,atlassian,jira,lfi
- **Description**: The CachingResourceDownloadRewriteRule class in Jira Server and Jira Data Center allowed unauthenticated remote attackers to read arbitrary files within WEB-INF and META-INF directories via an incorre...

#### Jira Server Pre-Auth - Arbitrary File Retrieval (WEB-INF, META-INF)
- **File**: `CVE-2020-29453.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,atlassian,jira,lfi
- **Description**: The CachingResourceDownloadRewriteRule class in Jira Server and Jira Data Center allowed unauthenticated remote attackers to read arbitrary files within WEB-INF and META-INF directories via an incorre...

#### Jira Dashboard Gadgets / Information Disclosure
- **File**: `CVE-2020-36287.yaml`
- **Author**: Jafar_Abo_Nada
- **Tags**: cve,cve2020,jira,atlassian,disclosure
- **Description**: The dashboard gadgets preference resource of the Atlassian gadgets plugin used in Jira Server and Jira Data Center before version 8.13.5, and from version 8.14.0 before version 8.15.1 allows remote an...

#### Atlassian Jira Unauth User Enumeration
- **File**: `CVE-2020-36289-1.yaml`
- **Author**: dhiyaneshDk
- **Tags**: cve,cve2020,jira,atlassian
- **Description**: Affected versions of Atlassian Jira Server and Data Center allow an unauthenticated user to enumerate users via an Information Disclosure vulnerability in the QueryComponentRendererValue!Default.jspa ...

#### Atlassian Jira Unauth User Enumeration
- **File**: `CVE-2020-36289-2.yaml`
- **Author**: dhiyaneshDk
- **Tags**: cve,cve2020,jira,atlassian
- **Description**: Affected versions of Atlassian Jira Server and Data Center allow an unauthenticated user to enumerate users via an Information Disclosure vulnerability in the QueryComponentRendererValue!Default.jspa ...

#### Atlassian Jira Unauth User Enumeration
- **File**: `CVE-2020-36289.yaml`
- **Author**: dhiyaneshDk
- **Tags**: cve,cve2020,jira,atlassian,unauth
- **Description**: Affected versions of Atlassian Jira Server and Data Center allow an unauthenticated user to enumerate users via an Information Disclosure vulnerability in the QueryComponentRendererValue!Default.jspa ...

#### Jira Subversion ALM for enterprise XSS
- **File**: `CVE-2020-9344-1.yaml`
- **Author**: madrobot
- **Tags**: cve,cve2020,atlassian,jira,xss
- **Description**: Subversion ALM for the enterprise before 8.8.2 allows reflected XSS at multiple locations.

#### Jira Subversion ALM for enterprise XSS
- **File**: `CVE-2020-9344-2.yaml`
- **Author**: madrobot
- **Tags**: cve,cve2020,atlassian,jira,xss
- **Description**: Subversion ALM for the enterprise before 8.8.2 allows reflected XSS at multiple locations.

#### Jira Subversion ALM for enterprise XSS
- **File**: `CVE-2020-9344-3.yaml`
- **Author**: madrobot
- **Tags**: cve,cve2020,atlassian,jira,xss
- **Description**: Subversion ALM for the enterprise before 8.8.2 allows reflected XSS at multiple locations.

#### Jira Subversion ALM for enterprise XSS
- **File**: `CVE-2020-9344-4.yaml`
- **Author**: madrobot
- **Tags**: cve,cve2020,atlassian,jira,xss
- **Description**: Subversion ALM for the enterprise before 8.8.2 allows reflected XSS at multiple locations.

#### Jira Subversion ALM for enterprise XSS
- **File**: `CVE-2020-9344-5.yaml`
- **Author**: madrobot
- **Tags**: cve,cve2020,atlassian,jira,xss
- **Description**: Subversion ALM for the enterprise before 8.8.2 allows reflected XSS at multiple locations.

#### Jira Subversion ALM for enterprise XSS
- **File**: `CVE-2020-9344.yaml`
- **Author**: madrobot
- **Tags**: cve,cve2020,atlassian,jira,xss
- **Description**: Subversion ALM for the enterprise before 8.8.2 allows reflected XSS at multiple locations.

#### Jira Limited Local File Read
- **File**: `CVE-2021-26086.yaml`
- **Author**: cocxanh
- **Tags**: cve,cve2021,jira,lfi
- **Description**: Affected versions of Atlassian Jira Server and Data Center allow remote attackers to read particular files via a path traversal vulnerability in the /WEB-INF/web.xml endpoint.

#### Atlassian Jira Server/Data Center <8.5.8/8.6.0 - 8.11.1 - Information Disclosure
- **File**: `CVE-2020-14179_1.yaml`
- **Author**: x1m_martijn
- **Tags**: cve,cve2020,atlassian,jira,exposure,disclosure
- **Description**: Atlassian Jira Server and Data Center before 8.5.8 and 8.6.0 through 8.11.1 are susceptible to information disclosure via the /secure/QueryComponent!Default.jspa endpoint. An attacker can view custom ...

#### Jira Server and Data Center - Information Disclosure
- **File**: `CVE-2020-14181_1.yaml`
- **Author**: bjhulst
- **Tags**: cve,cve2020,atlassian,jira,packetstorm
- **Description**: Jira Server and Data Center is susceptible to information disclosure. An attacker can enumerate users via the /ViewUserHover.jspa endpoint and thus potentially access sensitive information, modify dat...

#### Jira Server Pre-Auth - Arbitrary File Retrieval (WEB-INF, META-INF)
- **File**: `CVE-2020-29453_1.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,atlassian,jira,lfi,intrusive
- **Description**: The CachingResourceDownloadRewriteRule class in Jira Server and Jira Data Center allowed unauthenticated remote attackers to read arbitrary files within WEB-INF and META-INF directories via an incorre...

#### Jira Server and Data Center - Information Disclosure
- **File**: `CVE-2020-36289_1.yaml`
- **Author**: dhiyaneshDk
- **Tags**: cve,cve2020,jira,atlassian,unauth
- **Description**: Jira Server and Data Center is susceptible to information disclosure. An attacker can enumerate users via the QueryComponentRendererValue!Default.jspa endpoint and thus potentially access sensitive in...

#### Jira Subversion ALM for Enterprise <8.8.2 - Cross-Site Scripting
- **File**: `CVE-2020-9344_1.yaml`
- **Author**: madrobot
- **Tags**: cve,cve2020,atlassian,jira,xss
- **Description**: Jira Subversion ALM for Enterprise before 8.8.2 contains a cross-site scripting vulnerability at multiple locations.

#### Atlassian Jira Limited -  Local File Inclusion
- **File**: `CVE-2021-26086_1.yaml`
- **Author**: cocxanh
- **Tags**: lfi,packetstorm,cve,cve2021,jira,intrusive
- **Description**: Affected versions of Atlassian Jira Limited Server and Data Center are vulnerable to local file inclusion because they allow remote attackers to read particular files via a path traversal vulnerabilit...

#### Jira Netic Group Export <1.0.3 - Missing Authorization
- **File**: `CVE-2022-39960.yaml`
- **Author**: For3stCo1d
- **Tags**: cve,cve2022,atlassian,jira,netic,unauth
- **Description**: Jira Netic Group Export add-on before 1.0.3 contains a missing authorization vulnerability. The add-on does not perform authorization checks, which can allow an unauthenticated user to export all grou...

#### Confluence SSRF in sharelinks
- **File**: `confluence-ssrf-sharelinks.yaml`
- **Author**: TechbrunchFR
- **Tags**: confluence,atlassian,ssrf,jira,oast
- **Description**: Vulnerable should be Confluence versions released from 2016 November and older

#### Jira Service Desk Signup
- **File**: `jira-service-desk-signup_1.yaml`
- **Author**: TechbrunchFR
- **Tags**: jira,atlassian,service
- **Description**: No description

#### Atlassian Jira Service Desk Signup
- **File**: `jira-servicedesk-signup.yaml`
- **Author**: TechbrunchFR
- **Tags**: atlassian,servicedesk,jira,confluence
- **Description**: This instance of Atlassian JIRA is misconfigured to allow an attacker to sign up (create a new account) just by navigating to the signup page that is accessible at the URL /servicedesk/customer/user/s...

### Info Severity (27 templates)

#### Detect Jira Issue Management Software
- **File**: `jira-detect-1.yaml`
- **Author**: pdteam,philippedelteil
- **Tags**: panel,jira
- **Description**: No description

#### Detect Jira Issue Management Software
- **File**: `jira-detect-2.yaml`
- **Author**: pdteam,philippedelteil
- **Tags**: panel,jira
- **Description**: No description

#### Detect Jira Issue Management Software
- **File**: `jira-detect-3.yaml`
- **Author**: pdteam,philippedelteil
- **Tags**: panel,jira
- **Description**: No description

#### Detect Jira Issue Management Software
- **File**: `jira-detect.yaml`
- **Author**: pdteam,philippedelteil
- **Tags**: panel,jira
- **Description**: No description

#### Jira Rest API Server Information
- **File**: `jira-serverinfo.yaml`
- **Author**: pdteam
- **Tags**: jira,tech
- **Description**: No description

#### Jira Unauthenticated Admin Projects
- **File**: `jira-unauthenticated-adminprojects.yaml`
- **Author**: TESS
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated Dashboards
- **File**: `jira-unauthenticated-dashboards.yaml`
- **Author**: TechbrunchFR
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated Installed gadgets
- **File**: `jira-unauthenticated-installed-gadgets.yaml`
- **Author**: philippedelteil
- **Tags**: atlassian,jira
- **Description**: Some Jira instances allow to read the installed gadgets (sometimes it's also possible to read config xml file for some gadgets)

#### Jira Unauthenticated Popular Filters
- **File**: `jira-unauthenticated-popular-filters.yaml`
- **Author**: TechbrunchFR
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated Project Categories
- **File**: `jira-unauthenticated-projectcategories.yaml`
- **Author**: TESS
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated Projects
- **File**: `jira-unauthenticated-projects.yaml`
- **Author**: TechbrunchFR
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated Resolutions
- **File**: `jira-unauthenticated-resolutions.yaml`
- **Author**: TESS
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated Access to screens
- **File**: `jira-unauthenticated-screens.yaml`
- **Author**: TESS
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated User Picker
- **File**: `jira-unauthenticated-user-picker.yaml`
- **Author**: TechbrunchFR
- **Tags**: atlassian,jira
- **Description**: No description

#### Servicedesk Login Panel Detector
- **File**: `servicedesk-login-panel-1.yaml`
- **Author**: aashiq
- **Tags**: servicedesk,confluence,jira,panel
- **Description**: Searches for ServiceDesk login panels by trying to query the "/servicedesk/customer/user/login" endpoint

#### Servicedesk Login Panel Detector
- **File**: `servicedesk-login-panel-2.yaml`
- **Author**: aashiq
- **Tags**: servicedesk,confluence,jira,panel
- **Description**: Searches for ServiceDesk login panels by trying to query the "/servicedesk/customer/user/login" endpoint

#### Servicedesk Login Panel Detector
- **File**: `servicedesk-login-panel.yaml`
- **Author**: aashiq
- **Tags**: servicedesk,confluence,jira,panel,login
- **Description**: Searches for ServiceDesk login panels by trying to query the "/servicedesk/customer/user/login" endpoint

#### Jira Unauthenticated Admin Projects
- **File**: `jira-unauthenticated-adminprojects_1.yaml`
- **Author**: TESS
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated Dashboards
- **File**: `jira-unauthenticated-dashboards_1.yaml`
- **Author**: TechbrunchFR
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated Installed gadgets
- **File**: `jira-unauthenticated-installed-gadgets_1.yaml`
- **Author**: philippedelteil
- **Tags**: atlassian,jira
- **Description**: Some Jira instances allow to read the installed gadgets (sometimes it's also possible to read config xml file for some gadgets)

#### Jira Unauthenticated Project Categories
- **File**: `jira-unauthenticated-projectcategories_1.yaml`
- **Author**: TESS
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated Projects
- **File**: `jira-unauthenticated-projects_1.yaml`
- **Author**: TechbrunchFR
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated Resolutions
- **File**: `jira-unauthenticated-resolutions_1.yaml`
- **Author**: TESS
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated Access to screens
- **File**: `jira-unauthenticated-screens_1.yaml`
- **Author**: TESS
- **Tags**: atlassian,jira
- **Description**: No description

#### Jira Unauthenticated User Picker
- **File**: `jira-unauthenticated-user-picker_1.yaml`
- **Author**: TechbrunchFR
- **Tags**: atlassian,jira
- **Description**: No description

#### Detect Jira Issue Management Software
- **File**: `jira-detect_1.yaml`
- **Author**: pdteam,philippedelteil
- **Tags**: panel,jira
- **Description**: No description

#### Jira Service Desk Login Panel - Detect
- **File**: `servicedesk-login-panel_1.yaml`
- **Author**: aashiq
- **Tags**: servicedesk,confluence,jira,panel,login
- **Description**: Jira Service Desk login panel was detected.

