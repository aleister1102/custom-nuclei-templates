# Technology Adminer Templates

## Summary
- **Total templates**: 16
- **Category**: technology-adminer

## Templates List

### High Severity (3 templates)

#### Adminer SSRF Using Verbose Error Messages
- **File**: `CVE-2021-21311.yaml`
- **Author**: Adam Crosser
- **Tags**: cve,cve2021,adminer,ssrf
- **Description**: Adminer is an open-source database management in a single PHP file. In adminer from version 4.0.0 and before 4.7.9 there is a server-side request forgery vulnerability. Users of Adminer versions bundl...

#### Adminer <4.7.9 - Server-Side Request Forgery
- **File**: `CVE-2021-21311_1.yaml`
- **Author**: Adam Crosser,pwnhxl
- **Tags**: cve,cve2021,adminer,ssrf
- **Description**: Adminer before 4.7.9 is susceptible to server-side request forgery due to exposure of sensitive information in error messages. Users of Adminer versions bundling all drivers, e.g. adminer.php, are aff...

#### Adminer Default Login - Detect
- **File**: `adminer-default-login.yaml`
- **Author**: j4vaovo
- **Tags**: default-login,adminer
- **Description**: Adminer contains a default login vulnerability. An attacker can obtain access to user accounts and access sensitive information, modify data, and/or execute unauthorized operations.


### Medium Severity (2 templates)

#### Adminer reflected XSS via the table parameter
- **File**: `CVE-2021-29625.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2021,adminer,xss
- **Description**: Adminer is open-source database management software. A cross-site scripting vulnerability in Adminer versions 4.6.1 to 4.8.0 affects users of MySQL, MariaDB, PgSQL and SQLite. XSS is in most cases pre...

#### Adminer <=4.8.0 - Cross-Site Scripting
- **File**: `CVE-2021-29625_1.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2021,adminer,xss
- **Description**: Adminer 4.6.1 to 4.8.0 contains a cross-site scripting vulnerability which affects users of MySQL, MariaDB, PgSQL, and SQLite in browsers without CSP when Adminer uses a `pdo_` extension to communicat...

### Info Severity (11 templates)

#### Adminer Login panel
- **File**: `adminer-panel-1.yaml`
- **Author**: random_robbie,meme-lord
- **Tags**: panel
- **Description**: No description

#### Adminer Login panel
- **File**: `adminer-panel-2.yaml`
- **Author**: random_robbie,meme-lord
- **Tags**: panel
- **Description**: No description

#### Adminer Login panel
- **File**: `adminer-panel-3.yaml`
- **Author**: random_robbie,meme-lord
- **Tags**: panel
- **Description**: No description

#### Adminer Login panel
- **File**: `adminer-panel-4.yaml`
- **Author**: random_robbie,meme-lord
- **Tags**: panel
- **Description**: No description

#### Adminer Login panel
- **File**: `adminer-panel-5.yaml`
- **Author**: random_robbie,meme-lord
- **Tags**: panel
- **Description**: No description

#### Adminer Login panel
- **File**: `adminer-panel-6.yaml`
- **Author**: random_robbie,meme-lord
- **Tags**: panel
- **Description**: No description

#### Adminer Login panel
- **File**: `adminer-panel-7.yaml`
- **Author**: random_robbie,meme-lord
- **Tags**: panel
- **Description**: No description

#### Adminer Login Panel Fuzz
- **File**: `adminer-panel-fuzz.yaml`
- **Author**: random_robbie,meme-lord
- **Tags**: fuzz,adminer,login
- **Description**: No description

#### Adminer Login Panel
- **File**: `adminer-panel.yaml`
- **Author**: random_robbie,meme-lord,ritikchaddha
- **Tags**: panel,adminer
- **Description**: An Adminer login panel was detected.

#### Adminer Login Panel - Detect
- **File**: `adminer-panel-detect.yaml`
- **Author**: random_robbie,meme-lord
- **Tags**: fuzz,adminer,login
- **Description**: Adminer login panel was detected.

#### Adminer Login Panel - Detect
- **File**: `adminer-panel_1.yaml`
- **Author**: random_robbie,meme-lord,ritikchaddha
- **Tags**: panel,adminer
- **Description**: An Adminer login panel was detected.

