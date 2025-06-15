# Technology Magento Templates

## Summary
- **Total templates**: 31
- **Category**: technology-magento

## Templates List

### Critical Severity (2 templates)

#### Magento Mass Importer  <0.7.24 - Remote Auth Bypass
- **File**: `CVE-2020-5777.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,magmi,magento,auth,bypass,plugin
- **Description**: Magento Mass Importer (aka MAGMI) versions prior to 0.7.24 are vulnerable to a remote authentication bypass due to allowing default credentials in the event there is a database connection failure.

#### Magento Mass Importer  <0.7.24 - Remote Auth Bypass
- **File**: `CVE-2020-5777_1.yaml`
- **Author**: dwisiswant0
- **Tags**: plugin,tenable,cve,cve2020,magmi,magento,auth,bypass
- **Description**: Magento Mass Importer (aka MAGMI) versions prior to 0.7.24 are vulnerable to a remote authentication bypass due to allowing default credentials in the event there is a database connection failure.

### High Severity (13 templates)

#### Magento Cacheleak
- **File**: `magento-cacheleak.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: Magento Cacheleak is an implementation vulnerability, result of bad implementation of web-server configuration for Magento platform. Magento was developed to work under the Apache web-server which nat...

#### Magento Unprotected development files
- **File**: `magento-unprotected-dev-files-1.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: Magento version 1.9.2.x includes /dev directories or files that might reveal your passwords and other sensitive information. The /dev directories and files are not protected by default. According to M...

#### Magento Unprotected development files
- **File**: `magento-unprotected-dev-files-2.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: Magento version 1.9.2.x includes /dev directories or files that might reveal your passwords and other sensitive information. The /dev directories and files are not protected by default. According to M...

#### Magento Unprotected development files
- **File**: `magento-unprotected-dev-files.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: Magento version 1.9.2.x includes /dev directories or files that might reveal your passwords and other sensitive information. The /dev directories and files are not protected by default. According to M...

#### Magento Server Magmi Plugin - Directory Traversal
- **File**: `CVE-2015-2067.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2015,lfi,magento,magmi,plugin
- **Description**: Directory traversal vulnerability in web/ajax_pluginconf.php in the MAGMI (aka Magento Mass Importer) plugin for Magento Server allows remote attackers to read arbitrary files via a .. (dot dot) in th...

#### Cross Site Request Forgery (CSRF) in MAGMI (Magento Mass Importer) Plugin
- **File**: `CVE-2020-5776-1.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,magmi,magento
- **Description**: Currently, all versions of MAGMI are vulnerable to CSRF due to the lack of CSRF tokens. RCE (via phpcli command) is possible in the event that a CSRF is leveraged against an existing admin session for...

#### Cross Site Request Forgery (CSRF) in MAGMI (Magento Mass Importer) Plugin
- **File**: `CVE-2020-5776-2.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,magmi,magento
- **Description**: Currently, all versions of MAGMI are vulnerable to CSRF due to the lack of CSRF tokens. RCE (via phpcli command) is possible in the event that a CSRF is leveraged against an existing admin session for...

#### Cross Site Request Forgery (CSRF) in MAGMI (Magento Mass Importer) Plugin
- **File**: `CVE-2020-5776.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,magmi,magento
- **Description**: Currently, all versions of MAGMI are vulnerable to CSRF due to the lack of CSRF tokens. RCE (via phpcli command) is possible in the event that a CSRF is leveraged against an existing admin session for...

#### MAGMI - Cross-Site Request Forgery
- **File**: `CVE-2020-5776_1.yaml`
- **Author**: dwisiswant0
- **Tags**: magmi,magento,tenable,cve,cve2020
- **Description**: MAGMI (Magento Mass Importer) is vulnerable to cross-site request forgery (CSRF) due to a lack of CSRF tokens. Remote code execution (via phpcli command) is also possible in the event that CSRF is lev...

#### Magento Cacheleak
- **File**: `magento-cacheleak_1.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: Magento Cacheleak is an implementation vulnerability, result of bad implementation of web-server configuration for Magento platform. Magento was developed to work under the Apache web-server which nat...

#### Magento Configuration Panel - Detect
- **File**: `magento-config-disclosure.yaml`
- **Author**: ptonewreckin,danigoland,geeknik
- **Tags**: magento,exposure,credential,config
- **Description**: Magento configuration panel was detected. Misconfigured instances of Magento may disclose usernames, passwords, and database configurations via /app/etc/local.xml.


#### Magento Installation Wizard
- **File**: `magento-installer.yaml`
- **Author**: DhiyaneshDk
- **Tags**: misconfig,magento,install,exposure
- **Description**: No description

#### Magento Unprotected development files
- **File**: `magento-unprotected-dev-files_1.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: Magento version 1.9.2.x includes /dev directories or files that might reveal your passwords and other sensitive information. The /dev directories and files are not protected by default. According to M...

### Medium Severity (4 templates)

#### Magento Config Disclosure
- **File**: `magento-config-1.yaml`
- **Author**: geeknik
- **Tags**: config,exposure,magento
- **Description**: No description

#### Magento Config Disclosure
- **File**: `magento-config-2.yaml`
- **Author**: geeknik
- **Tags**: config,exposure,magento
- **Description**: No description

#### Magento Config Disclosure
- **File**: `magento-config.yaml`
- **Author**: geeknik
- **Tags**: config,exposure,magento
- **Description**: No description

#### Magento Server Magmi Plugin - Cross Site Scripting
- **File**: `CVE-2015-2068.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2015,magento,magmi,xss,plugin
- **Description**: Multiple cross-site scripting (XSS) vulnerabilities in the MAGMI (aka Magento Mass Importer) plugin for Magento Server allow remote attackers to inject arbitrary web script or HTML via the (1) profile...

### Info Severity (12 templates)

#### Exposed Magento Admin Panel
- **File**: `magento-admin-panel.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento,panel
- **Description**: As a security best practice, Magento recommends that you use a unique, custom Admin URL instead of the default admin or a common term such as backend. Although it will not directly protect your site f...

#### Magento Detect
- **File**: `magento-detect-1.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: Identify Magento

#### Magento Detect
- **File**: `magento-detect-2.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: Identify Magento

#### Magento Detect
- **File**: `magento-detect.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: Identify Magento

#### MAGMI (Magento Mass Importer) Plugin Detect
- **File**: `magmi-detect.yaml`
- **Author**: dwisiswant0
- **Tags**: magento,magmi,plugin
- **Description**: No description

#### Exposed Magento 2 API
- **File**: `magento-2-exposed-api-1.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: The API in Magento 2 can be accessed by the world without providing credentials. Through the API information like storefront, (hidden) products including prices are exposed.

#### Exposed Magento 2 API
- **File**: `magento-2-exposed-api-2.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: The API in Magento 2 can be accessed by the world without providing credentials. Through the API information like storefront, (hidden) products including prices are exposed.

#### Exposed Magento 2 API
- **File**: `magento-2-exposed-api-3.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: The API in Magento 2 can be accessed by the world without providing credentials. Through the API information like storefront, (hidden) products including prices are exposed.

#### Exposed Magento 2 API
- **File**: `magento-2-exposed-api.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: The API in Magento 2 can be accessed by the world without providing credentials. Through the API information like storefront, (hidden) products including prices are exposed.

#### Exposed Magento 2 API
- **File**: `magento-2-exposed-api_1.yaml`
- **Author**: TechbrunchFR
- **Tags**: magento
- **Description**: The API in Magento 2 can be accessed by the world without providing credentials. Through the API information like storefront, (hidden) products including prices are exposed.

#### Magento Admin Login Panel - Detect
- **File**: `magento-admin-panel_1.yaml`
- **Author**: TechbrunchFR,ritikchaddha
- **Tags**: magento,panel
- **Description**: Magento admin login panel was detected.


#### Magento Connect Manager Installer - Detect
- **File**: `magento-downloader-panel.yaml`
- **Author**: 5up3r541y4n
- **Tags**: magento,exposure,panel
- **Description**: Magento Connect Manager installer was detected. The software, available via /downloader/ location, requires Magento admin rights and uses the same authorization methods as for backend. If an attacker ...

