# Attack Open Redirect Templates

## Summary
- **Total templates**: 3
- **Category**: attack-open-redirect

## Templates List

### Medium Severity (2 templates)

#### Gitea <1.16.5 - Open Redirect
- **File**: `CVE-2022-1058.yaml`
- **Author**: theamanrawat
- **Tags**: huntr,cve,cve2022,open-redirect,gitea
- **Description**: Gitea before 1.16.5 is susceptible to open redirect via GitHub repository go-gitea/gitea. An attacker can redirect a user to a malicious site and potentially obtain sensitive information, modify data,...

#### open-redirect
- **File**: `open-redirect.yaml`
- **Author**: MR.iambatman
- **Tags**: 
- **Description**: redirect

### Low Severity (1 templates)

#### Open Redirect Vulnerability Detection
- **File**: `open-redirect-bypass.yaml`
- **Author**: h0tak88r
- **Tags**: open-redirect, misconfiguration
- **Description**: Detects open redirect vulnerabilities by checking if the server redirects to an external domain.

