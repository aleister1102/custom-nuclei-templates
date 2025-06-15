# Technology Joomla Templates

## Summary
- **Total templates**: 147
- **Category**: technology-joomla

## Templates List

### Critical Severity (5 templates)

#### Rusty Joomla RCE - Unauthenticated PHP Object Injection in Joomla CMS
- **File**: `rusty-joomla.yaml`
- **Author**: leovalcante,kiks7
- **Tags**: joomla,rce,unauth,php,cms,objectinjection
- **Description**: Unauthenticated PHP Object Injection in Joomla CMS from the release 3.0.0 to the 3.4.6 (releases from 2012 to December 2015) that leads to Remote Code Execution.

#### Joomla! JCK Editor SQL Injection
- **File**: `CVE-2018-17254.yaml`
- **Author**: Suman_Kar
- **Tags**: joomla,sqli,cve,cve2018
- **Description**: The JCK Editor component 6.4.4 for Joomla! allows SQL Injection via the jtreelink/dialogs/links.php parent parameter.

#### Joomla SQL Inject
- **File**: `CVE-2018-7314.yaml`
- **Author**: 南方有梦(http://github.com/hackgov)
- **Tags**: 
- **Description**: No description

#### Joomla未授权访问漏洞(CVE-2023-23752)
- **File**: `CVE-2023-23752.yaml`
- **Author**: daffainfo、m4sk
- **Tags**: 
- **Description**: Joomla中存在未授权访问漏洞，由于对Web服务端点的访问限制不当，远程攻击者可以绕过安全限制获得Web应用程序敏感信息。
影响版本4.0.0 <= Joomla <= 4.2.7
fofa-query: title="锐捷网络-EWEB网管系统"


#### Joomla! CMS <=3.4.6 - Remote Code Execution
- **File**: `rusty-joomla_1.yaml`
- **Author**: leovalcante,kiks7
- **Tags**: joomla,rce,unauth,php,cms,objectinjection
- **Description**: Joomla! CMS 3.0.0 through the 3.4.6 release contains an unauthenticated PHP object injection that leads to remote code execution.


### High Severity (129 templates)

#### Joomla! com_fabrik 3.9.11 - Directory Traversal
- **File**: `joomla-com-fabrik-lfi.yaml`
- **Author**: dhiyaneshDk
- **Tags**: joomla,lfi
- **Description**: No description

#### Joomla! Component com_sef - Local File Inclusion
- **File**: `joomla-jvehicles-lfi.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A local file inclusion vulnerability in the Jvehicles (com_jvehicles) component version 1.0 for Joomla! allows remote attackers to load arbitrary files via the controller parameter in index.php.

#### Joomla! Component RSfiles <=1.0.2 - Arbitrary File Retrieval
- **File**: `CVE-2007-4504.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2007,joomla,lfi
- **Description**: An arbitrary file retrieval vulnerability in index.php in the RSfiles component (com_rsfiles) <=1.0.2 for Joomla! allows remote attackers to arbitrarily read files via a .. (dot dot) in the path param...

#### Joomla! Component imagebrowser 0.1.5 rc2 - Directory Traversal
- **File**: `CVE-2008-4668.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2008,joomla,lfi
- **Description**: Directory traversal vulnerability in the Image Browser (com_imagebrowser) 0.1.5 component for Joomla! allows remote attackers to include and execute arbitrary local files via a .. (dot dot) in the fol...

#### Joomla! Component com_extplorer 2.0.0 RC2 - Directory Traversal
- **File**: `CVE-2008-4764.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2008,joomla,lfi
- **Description**: Directory traversal vulnerability in the eXtplorer module (com_extplorer) 2.0.0 RC2 and earlier in Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the dir parameter in a ...

#### Joomla! Component ionFiles 4.4.2 - File Disclosure
- **File**: `CVE-2008-6080.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2008,joomla,lfi
- **Description**: Directory traversal vulnerability in download.php in the ionFiles (com_ionfiles) 4.4.2 component for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the file parameter.

#### Joomla! Component RWCards 3.0.11 - Local File Inclusion
- **File**: `CVE-2008-6172.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2008,joomla,lfi
- **Description**: A directory traversal vulnerability in captcha/captcha_image.php in the RWCards (com_rwcards) 3.0.11 component for Joomla! when magic_quotes_gpc is disabled allows remote attackers to include and exec...

#### Joomla! Component ProDesk 1.0/1.2 - Local File Inclusion
- **File**: `CVE-2008-6222.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2008,joomla,lfi
- **Description**: Directory traversal vulnerability in the Pro Desk Support Center (com_pro_desk) component 1.0 and 1.2 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the include_file...

#### Joomla! Component Cmimarketplace - 'viewit' Directory Traversal
- **File**: `CVE-2009-1496.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2009,joomla,lfi
- **Description**: Directory traversal vulnerability in the Cmi Marketplace (com_cmimarketplace) component 0.1 for Joomla! allows remote attackers to list arbitrary directories via a .. (dot dot) in the viewit parameter...

#### Joomla! Component com_Projectfork 2.0.10 - Local File Inclusion
- **File**: `CVE-2009-2100.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2009,joomla,lfi
- **Description**: Directory traversal vulnerability in the JoomlaPraise Projectfork (com_projectfork) component 2.0.10 for Joomla! allows remote attackers to read arbitrary files via directory traversal sequences in th...

#### Joomla! Component Agora 3.0.0b (com_agora) - Local File Inclusion
- **File**: `CVE-2009-3053.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2009,joomla,lfi
- **Description**: Directory traversal vulnerability in the Agora (com_agora) component 3.0.0b for Joomla! allows remote attackers to include and execute arbitrary local files via directory traversal sequences in the ac...

#### Joomla! Component com_album 1.14 - Directory Traversal
- **File**: `CVE-2009-3318.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2009,joomla,lfi
- **Description**: Directory traversal vulnerability in the Roland Breedveld Album (com_album) component 1.14 for Joomla! allows remote attackers to access arbitrary directories and have unspecified other impact via a ....

#### Joomla! Component Omilen Photo Gallery 0.5b - Local File Inclusion
- **File**: `CVE-2009-4202.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2009,joomla,lfi,photo
- **Description**: Directory traversal vulnerability in the Omilen Photo Gallery (com_omphotogallery) component Beta 0.5 for Joomla! allows remote attackers to include and execute arbitrary local files via directory tra...

#### Joomla! Component iF Portfolio Nexus - 'Controller' Remote File Inclusion
- **File**: `CVE-2009-4679.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2009,joomla,lfi,nexus
- **Description**: Directory traversal vulnerability in the inertialFATE iF Portfolio Nexus (com_if_nexus) component 1.5 for Joomla! allows remote attackers to include and execute arbitrary local files via a .. (dot dot...

#### Joomla! Component com_biblestudy - Local File Inclusion
- **File**: `CVE-2010-0157.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Bible Study (com_biblestudy) component 6.1 for Joomla! allows remote attackers to include and execute arbitrary local files via a .. (dot dot) in the control...

#### Joomla! Component Jw_allVideos - Arbitrary File Retrieval
- **File**: `CVE-2010-0696.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in includes/download.php in the JoomlaWorks AllVideos (Jw_allVideos) plugin 3.0 through 3.2 for Joomla! allows remote attackers to read arbitrary files via a ./../....

#### Joomla! Plugin Core Design Scriptegrator - Local File Inclusion
- **File**: `CVE-2010-0759.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi,plugin
- **Description**: A directory traversal vulnerability in plugins/system/cdscriptegrator/libraries/highslide/js/jsloader.php in the Core Design Scriptegrator plugin 1.4.1 for Joomla! allows remote attackers to read, and...

#### Joomla! Component com_jvideodirect - Directory Traversal
- **File**: `CVE-2010-0942.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: Directory traversal vulnerability in the jVideoDirect (com_jvideodirect) component for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to index.p...

#### Joomla! Component com_jashowcase - Directory Traversal
- **File**: `CVE-2010-0943.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the JA Showcase (com_jashowcase) component for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter in a jashow...

#### Joomla! Component com_jcollection - Directory Traversal
- **File**: `CVE-2010-0944.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the JCollection (com_jcollection) component for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to index.p...

#### Joomla! Component com_gcalendar Suite 2.1.5 - Local File Inclusion
- **File**: `CVE-2010-0972.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the GCalendar (com_gcalendar) component 2.1.5 for Joomla! allows remote attackers to include and execute arbitrary local files via a .. (dot dot) in the controll...

#### Joomla! Component com_cartweberp - Local File Inclusion
- **File**: `CVE-2010-0982.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the CARTwebERP (com_cartweberp) component 1.56.75 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to i...

#### Joomla! Component com_abbrev - Local File Inclusion
- **File**: `CVE-2010-0985.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Abbreviations Manager (com_abbrev) component 1.1 for Joomla! allows remote attackers to include and execute arbitrary local files via a .. (dot dot) in the c...

#### Joomla! Component com_rokdownloads - Local File Inclusion
- **File**: `CVE-2010-1056.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the RokDownloads (com_rokdownloads) component before 1.0.1 for Joomla! allows remote attackers to include and execute arbitrary local files via a .. (dot dot) in...

#### Joomla! Component com_communitypolls 1.5.2 - Local File Inclusion
- **File**: `CVE-2010-1081.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Community Polls (com_communitypolls) component 1.5.2, and possibly earlier, for Core Joomla! allows remote attackers to read arbitrary files via a .. (dot do...

#### Joomla! Component & Plugin JE Tooltip 1.0 - Local File Inclusion
- **File**: `CVE-2010-1217.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi,plugin
- **Description**: A directory traversal vulnerability in the JE Form Creator (com_jeformcr) component for Joomla!, when magic_quotes_gpc is disabled, allows remote attackers to read arbitrary files via directory traver...

#### Joomla! Component com_janews - Local File Inclusion
- **File**: `CVE-2010-1219.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the JA News (com_janews) component 1.0 for Joomla! allows remote attackers to read arbitrary local files via a .. (dot dot) in the controller parameter to index....

#### Joomla! Component DW Graph - Local File Inclusion
- **File**: `CVE-2010-1302.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi,graph
- **Description**: A directory traversal vulnerability in dwgraphs.php in the DecryptWeb DW Graphs (com_dwgraphs) component 1.0 for Joomla! allows remote attackers to read arbitrary files via directory traversal sequenc...

#### Joomla! Component User Status - Local File Inclusion
- **File**: `CVE-2010-1304.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi,status
- **Description**: A directory traversal vulnerability in userstatus.php in the User Status (com_userstatus) component 1.21.16 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the contro...

#### Joomla! Component JInventory 1.23.02 - Local File Inclusion
- **File**: `CVE-2010-1305.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in jinventory.php in the JInventory (com_jinventory) component 1.23.02 and possibly other versions before 1.26.03, a module for Joomla!, allows remote attackers to ...

#### Joomla! Component Picasa 2.0 - Local File Inclusion
- **File**: `CVE-2010-1306.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Picasa (com_joomlapicasa2) component 2.0 and 2.0.5 for Joomla! allows remote attackers to read arbitrary local files via a .. (dot dot) in the controller par...

#### Joomla! Component Magic Updater - Local File Inclusion
- **File**: `CVE-2010-1307.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Magic Updater (com_joomlaupdater) component for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to ind...

#### Joomla! Component SVMap 1.1.1 - Local File Inclusion
- **File**: `CVE-2010-1308.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the SVMap (com_svmap) component 1.1.1 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to index.php.

#### Joomla! Component News Portal 1.5.x - Local File Inclusion
- **File**: `CVE-2010-1312.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the iJoomla News Portal (com_news_portal) component 1.5.x for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parame...

#### Joomla! Component Saber Cart 1.0.0.12 - Local File Inclusion
- **File**: `CVE-2010-1313.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Seber Cart (com_sebercart) component 1.0.0.12 and 1.0.0.13 for Joomla!, when magic_quotes_gpc is disabled, allows remote attackers to read arbitrary files vi...

#### Joomla! Component Highslide 1.5 - Local File Inclusion
- **File**: `CVE-2010-1314.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Highslide JS (com_hsconfig) component 1.5 and 2.0.9 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller paramete...

#### Joomla! Component webERPcustomer - Local File Inclusion
- **File**: `CVE-2010-1315.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in weberpcustomer.php in the webERPcustomer (com_weberpcustomer) component 1.2.1 and 1.x before 1.06.02 for Joomla! allows remote attackers to read arbitrary files ...

#### Joomla! Component com_jresearch - 'Controller' Local File Inclusion
- **File**: `CVE-2010-1340.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in jresearch.php in the J!Research (com_jresearch) component for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parame...

#### Joomla! Component Cookex Agency CKForms - Local File Inclusion
- **File**: `CVE-2010-1345.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Cookex Agency CKForms (com_ckforms) component 1.3.3 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller paramete...

#### Joomla! Component Juke Box 1.7 - Local File Inclusion
- **File**: `CVE-2010-1352.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the JOOFORGE Jutebox (com_jukebox) component 1.0 and 1.7 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller paramet...

#### Joomla! Component LoginBox - Local File Inclusion
- **File**: `CVE-2010-1353.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the LoginBox Pro (com_loginbox) component for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the view parameter to index.php.

#### Joomla! Component VJDEO 1.0 - Local File Inclusion
- **File**: `CVE-2010-1354.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the VJDEO (com_vjdeo) component 1.0 and 1.0.1 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to index...

#### Joomla! Component Photo Battle 1.0.1 - Local File Inclusion
- **File**: `CVE-2010-1461.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi,photo
- **Description**: A directory traversal vulnerability in the Photo Battle (com_photobattle) component 1.0.1 for Joomla! allows remote attackers to read arbitrary files via the view parameter to index.php.

#### Joomla! Component JProject Manager 1.0 - Local File Inclusion
- **File**: `CVE-2010-1469.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Ternaria Informatica JProject Manager (com_jprojectmanager) component 1.0 for Joomla! allows remote attackers to read arbitrary files and possibly have unspe...

#### Joomla! Component Web TV 1.0 - Local File Inclusion
- **File**: `CVE-2010-1470.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Web TV (com_webtv) component 1.0 for Joomla! allows remote attackers to read arbitrary files and have possibly other unspecified impacts via a .. (dot dot) i...

#### Joomla! Component Address Book 1.5.0 - Local File Inclusion
- **File**: `CVE-2010-1471.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the AddressBook (com_addressbook) component 1.5.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to i...

#### Joomla! Component Horoscope 1.5.0 - Local File Inclusion
- **File**: `CVE-2010-1472.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Daily Horoscope (com_horoscope) component 1.5.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to...

#### Joomla! Component Advertising 0.25 - Local File Inclusion
- **File**: `CVE-2010-1473.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Advertising (com_advertising) component 0.25 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts via a .....

#### Joomla! Component Sweetykeeper 1.5 - Local File Inclusion
- **File**: `CVE-2010-1474.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Sweety Keeper (com_sweetykeeper) component 1.5.x for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts via ...

#### Joomla! Component Preventive And Reservation 1.0.5 - Local File Inclusion
- **File**: `CVE-2010-1475.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Preventive & Reservation (com_preventive) component 1.0.5 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other imp...

#### Joomla! Component AlphaUserPoints 1.5.5 - Local File Inclusion
- **File**: `CVE-2010-1476.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the AlphaUserPoints (com_alphauserpoints) component 1.5.5 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts...

#### Joomla! Component Jfeedback 1.2 - Local File Inclusion
- **File**: `CVE-2010-1478.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Ternaria Informatica Jfeedback! (com_jfeedback) component 1.2 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other...

#### Joomla! Component MMS Blog 2.3.0 - Local File Inclusion
- **File**: `CVE-2010-1491.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the MMS Blog (com_mmsblog) component 2.3.0 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts via a .. (dot ...

#### Joomla! Component AWDwall 1.5.4 - Local File Inclusion
- **File**: `CVE-2010-1494.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the AWDwall (com_awdwall) component 1.5.4 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to index.php...

#### Joomla! Component Matamko 1.01 - Local File Inclusion
- **File**: `CVE-2010-1495.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Matamko (com_matamko) component 1.01 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to index.php.

#### Joomla! Component redSHOP 1.0 - Local File Inclusion
- **File**: `CVE-2010-1531.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the redSHOP (com_redshop) component 1.0.x for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the view parameter to index.php.

#### Joomla! Component PowerMail Pro 1.5.3 - Local File Inclusion
- **File**: `CVE-2010-1532.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the givesight PowerMail Pro (com_powermail) component 1.5.3 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impac...

#### Joomla! Component TweetLA 1.0.1 - Local File Inclusion
- **File**: `CVE-2010-1533.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the TweetLA (com_tweetla) component 1.0.1 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to index.php...

#### Joomla! Component Shoutbox Pro - Local File Inclusion
- **File**: `CVE-2010-1534.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Shoutbox Pro (com_shoutbox) component for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to index.php...

#### Joomla! Component TRAVELbook 1.0.1 - Local File Inclusion
- **File**: `CVE-2010-1535.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the TRAVELbook (com_travelbook) component 1.0.1 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts via a .. ...

#### Joomla! Component com_blog - Directory Traversal
- **File**: `CVE-2010-1540.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in index.php in the MyBlog (com_myblog) component 3.0.329 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the task parameter.

#### Joomla! Component JA Comment - Local File Inclusion
- **File**: `CVE-2010-1601.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the JA Comment (com_jacomment) component for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the view parameter to index.php.

#### Joomla! Component ZiMB Comment 0.8.1 - Local File Inclusion
- **File**: `CVE-2010-1602.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the ZiMB Comment (com_zimbcomment) component 0.8.1 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts via a ...

#### Joomla! Component ZiMBCore 0.1 - Local File Inclusion
- **File**: `CVE-2010-1603.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the ZiMB Core (aka ZiMBCore or com_zimbcore) component 0.1 in the ZiMB Manager collection for Joomla! allows remote attackers to read arbitrary files and possibl...

#### Joomla! Component WMI 1.5.0 - Local File Inclusion
- **File**: `CVE-2010-1607.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in wmi.php in the Webmoney Web Merchant Interface (aka WMI or com_wmi) component 1.5.0 for Joomla! allows remote attackers to include and execute arbitrary local fi...

#### Joomla! Component Graphics 1.0.6 - Local File Inclusion
- **File**: `CVE-2010-1653.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in graphics.php in the Graphics (com_graphics) component 1.0.6 and 1.5.0 for Joomla! allows remote attackers to include and execute arbitrary local files via a .. (...

#### Joomla! Component SmartSite 1.0.0 - Local File Inclusion
- **File**: `CVE-2010-1657.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the SmartSite (com_smartsite) component 1.0.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to index...

#### Joomla! Component NoticeBoard 1.3 - Local File Inclusion
- **File**: `CVE-2010-1658.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Code-Garage NoticeBoard (com_noticeboard) component 1.3 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impac...

#### Joomla! Component Ultimate Portfolio 1.0 - Local File Inclusion
- **File**: `CVE-2010-1659.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Ultimate Portfolio (com_ultimateportfolio) component 1.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller par...

#### Joomla! Component Arcade Games 1.0 - Local File Inclusion
- **File**: `CVE-2010-1714.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Arcade Games (com_arcadegames) component 1.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to in...

#### Joomla! Component Online Exam 1.5.0 - Local File Inclusion
- **File**: `CVE-2010-1715.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Online Examination (aka Online Exam or com_onlineexam) component 1.5.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the ...

#### Joomla! Component iF surfALERT 1.2 - Local File Inclusion
- **File**: `CVE-2010-1717.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the iF surfALERT (com_if_surfalert) component 1.2 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts via a ....

#### Joomla! Component Archery Scores 1.0.6 - Local File Inclusion
- **File**: `CVE-2010-1718.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in archeryscores.php in the Archery Scores (com_archeryscores) component 1.0.6 for Joomla! allows remote attackers to include and execute arbitrary local files via ...

#### Joomla! Component MT Fire Eagle 1.2 - Local File Inclusion
- **File**: `CVE-2010-1719.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the MT Fire Eagle (com_mtfireeagle) component 1.2 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts via a ....

#### Joomla! Component Online Market 2.x - Local File Inclusion
- **File**: `CVE-2010-1722.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Online Market (com_market) component 2.x for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts via a .. (do...

#### Joomla! Component iNetLanka Contact Us Draw Root Map 1.1 - Local File Inclusion
- **File**: `CVE-2010-1723.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the iNetLanka Contact Us Draw Root Map (com_drawroot) component 1.1 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified oth...

#### Joomla! Component SMEStorage - Local File Inclusion
- **File**: `CVE-2010-1858.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the SMEStorage (com_smestorage) component before 1.1 for Joomla! allows remote attackers to read arbitrary files via directory traversal sequences in the control...

#### Joomla! Component Jvehicles - Local File Inclusion
- **File**: `CVE-2010-1873.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: SQL injection vulnerability in the Jvehicles (com_jvehicles) component 1.0, 2.0, and 2.1111 for Joomla! allows remote attackers to execute arbitrary SQL commands via the aid parameter in an agentlisti...

#### Joomla! Component Property - Local File Inclusion
- **File**: `CVE-2010-1875.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Real Estate Property (com_properties) component 3.1.22-03 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other imp...

#### Joomla! Component OrgChart 1.0.0 - Local File Inclusion
- **File**: `CVE-2010-1878.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the OrgChart (com_orgchart) component 1.0.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to index.p...

#### Joomla! Component BeeHeard 1.0 - Local File Inclusion
- **File**: `CVE-2010-1952.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the BeeHeard (com_beeheard) and BeeHeard Lite (com_beeheardlite) component 1.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in ...

#### Joomla! Component iNetLanka Multiple Map 1.0 - Local File Inclusion
- **File**: `CVE-2010-1953.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the iNetLanka Multiple Map (com_multimap) component 1.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller paramete...

#### Joomla! Component iNetLanka Multiple root 1.0 - Local File Inclusion
- **File**: `CVE-2010-1954.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the iNetLanka Multiple root (com_multiroot) component 1.0 and 1.1 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controlle...

#### Joomla! Component Deluxe Blog Factory 1.1.2 - Local File Inclusion
- **File**: `CVE-2010-1955.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Deluxe Blog Factory (com_blogfactory) component 1.1.2 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parame...

#### Joomla! Component Gadget Factory 1.0.0 - Local File Inclusion
- **File**: `CVE-2010-1956.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Gadget Factory (com_gadgetfactory) component 1.0.0 and 1.5.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller...

#### Joomla! Component Love Factory 1.3.4 - Local File Inclusion
- **File**: `CVE-2010-1957.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Love Factory (com_lovefactory) component 1.3.4 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to ...

#### Joomla! Component J!WHMCS Integrator 1.5.0 - Local File Inclusion
- **File**: `CVE-2010-1977.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the J!WHMCS Integrator (com_jwhmcs) component 1.5.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to...

#### Joomla! Component Affiliate Datafeeds 880 - Local File Inclusion
- **File**: `CVE-2010-1979.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Affiliate Datafeeds (com_datafeeds) component build 880 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller para...

#### Joomla! Component Joomla! Flickr 1.0 - Local File Inclusion
- **File**: `CVE-2010-1980.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in joomlaflickr.php in the Joomla Flickr (com_joomlaflickr) component 1.0.3 for Joomla! allows remote attackers to include and execute arbitrary local files via a ....

#### Joomla! Component Fabrik 2.0 - Local File Inclusion
- **File**: `CVE-2010-1981.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Fabrik (com_fabrik) component 2.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to index.php.

#### Joomla! Component JA Voice 2.0 - Local File Inclusion
- **File**: `CVE-2010-1982.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the JA Voice (com_javoice) component 2.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the view parameter to index.php.

#### Joomla! Component redTWITTER 1.0 - Local File Inclusion
- **File**: `CVE-2010-1983.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A drectory traversal vulnerability in the redTWITTER (com_redtwitter) component 1.0.x including 1.0b11 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the view parame...

#### Joomla Percha Categories Tree 0.6 - Local File Inclusion
- **File**: `CVE-2010-2033.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Percha Fields Attach (com_perchafieldsattach) component 1.x for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other i...

#### Joomla! Component Percha Image Attach 1.1 - Directory Traversal
- **File**: `CVE-2010-2034.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Percha Image Attach (com_perchaimageattach) component 1.1 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other imp...

#### Joomla! Component Percha Gallery 1.6 Beta - Directory Traversal
- **File**: `CVE-2010-2035.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Percha Gallery (com_perchagallery) component 1.6 Beta for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts...

#### Joomla! Component Percha Fields Attach 1.0 - Directory Traversal
- **File**: `CVE-2010-2036.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,lfi,joomla
- **Description**: A directory traversal vulnerability in the Percha Fields Attach (com_perchafieldsattach) component 1.x for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other i...

#### Joomla! Component Percha Downloads Attach 1.1 - Directory Traversal
- **File**: `CVE-2010-2037.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,lfi,joomla
- **Description**: A directory traversal vulnerability in the Percha Downloads Attach (com_perchadownloadsattach) component 1.1 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified o...

#### Joomla! Component FDione Form Wizard 1.0.2 - Local File Inclusion
- **File**: `CVE-2010-2045.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Dione Form Wizard (aka FDione or com_dioneformwizard) component 1.0.2 for Joomla! allows remote attackers to read arbitrary files via directory traversal seq...

#### Joomla! Component MS Comment 0.8.0b - Local File Inclusion
- **File**: `CVE-2010-2050.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Moron Solutions MS Comment (com_mscomment) component 0.8.0b for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller ...

#### Joomla! Component simpledownload <=0.9.5 - Arbitrary File Retrieval
- **File**: `CVE-2010-2122.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the SimpleDownload (com_simpledownload) component before 0.9.6 for Joomla! allows remote attackers to retrieve arbitrary files via a .. (dot dot) in the controll...

#### Joomla! Component JE Quotation Form 1.0b1 - Local File Inclusion
- **File**: `CVE-2010-2128.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the JE Quotation Form (com_jequoteform) component 1.0b1 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts v...

#### Joomla! Component com_bfsurvey - Local File Inclusion
- **File**: `CVE-2010-2259.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the BF Survey (com_bfsurvey) component for Joomla! allows remote attackers to include and execute arbitrary local files via a .. (dot dot) in the controller para...

#### Joomla! Component Picasa2Gallery 1.2.8 - Local File Inclusion
- **File**: `CVE-2010-2507.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Picasa2Gallery (com_picasa2gallery) component 1.2.8 and earlier for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified oth...

#### Joomla! Component jesectionfinder - Local File Inclusion
- **File**: `CVE-2010-2680.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the JExtensions JE Section/Property Finder (jesectionfinder) component for Joomla! allows remote attackers to include and execute arbitrary local files via direc...

#### Joomla! Component Realtyna Translator 1.0.15 - Local File Inclusion
- **File**: `CVE-2010-2682.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Realtyna Translator (com_realtyna) component 1.0.15 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts v...

#### Joomla! Component Music Manager - Local File Inclusion
- **File**: `CVE-2010-2857.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Music Manager component for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts via a .. (dot dot) in the cid...

#### Joomla! Component Visites 1.1 - MosConfig_absolute_path Remote File Inclusion
- **File**: `CVE-2010-2918.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A PHP remote file inclusion vulnerability in core/include/myMailer.class.php in the Visites (com_joomla-visites) component 1.1 RC2 for Joomla! allows remote attackers to execute arbitrary PHP code via...

#### Joomla! Component Foobla Suggestions 1.5.1.2 - Local File Inclusion
- **File**: `CVE-2010-2920.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Foobla Suggestions (com_foobla_suggestions) component 1.5.1.2 for Joomla! allows remote attackers to read arbitrary files via directory traversal sequences i...

#### Joomla! Component PicSell 1.0 - Arbitrary File Retrieval
- **File**: `CVE-2010-3203.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the PicSell (com_picsell) component 1.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the dflink parameter in a prevsell dwnf...

#### Joomla! Component Jphone 1.0 Alpha 3 - Local File Inclusion
- **File**: `CVE-2010-3426.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in jphone.php in the JPhone (com_jphone) component 1.0 Alpha 3 for Joomla! allows remote attackers to include and execute arbitrary local files via a .. (dot dot) i...

#### Joomla! Component JotLoader 2.2.1 - Local File Inclusion
- **File**: `CVE-2010-4617.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the JotLoader (com_jotloader) component 2.2.1 for Joomla! allows remote attackers to read arbitrary files via directory traversal sequences in the section parame...

#### Joomla! Component JRadio - Local File Inclusion
- **File**: `CVE-2010-4719.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in JRadio (com_jradio) component before 1.5.1 for Joomla! allows remote attackers to read arbitrary files via directory traversal sequences in the controller parame...

#### Joomla! Component Jimtawl 1.0.2 - Local File Inclusion
- **File**: `CVE-2010-4769.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the Jimtawl (com_jimtawl) component 1.0.2 Joomla! allows remote attackers to read arbitrary files and possibly unspecified other impacts via a .. (dot dot) in th...

#### Joomla! Component Canteen 1.0 - Local File Inclusion
- **File**: `CVE-2010-4977.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A SQL injection vulnerability in menu.php in the Canteen (com_canteen) component 1.0 for Joomla! allows remote attackers to execute arbitrary SQL commands via the mealid parameter to index.php.

#### Joomla! Component JE Job 1.0 - Local File Inclusion
- **File**: `CVE-2010-5028.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A SQL injection vulnerability in the JExtensions JE Job (com_jejob) component 1.0 for Joomla! allows remote attackers to execute arbitrary SQL commands via the catid parameter in an item action to ind...

#### Joomla! Component Jstore - 'Controller' Local File Inclusion
- **File**: `CVE-2010-5286.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in Jstore (com_jstore) component for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impacts via a .. (dot dot) in the c...

#### Joomla! Component com_kp - 'Controller' Local File Inclusion
- **File**: `CVE-2011-4804.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2011,joomla,lfi
- **Description**: A directory traversal vulnerability in the obSuggest (com_obsuggest) component before 1.8 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter to ...

#### Joomla! Component MooFAQ (com_moofaq) - Local File Inclusion
- **File**: `CVE-2009-2015.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2009,joomla,lfi
- **Description**: Directory traversal vulnerability in includes/file_includer.php in the Ideal MooFAQ (com_moofaq) component 1.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the fil...

#### Joomla! Component Jtag Members Directory 5.3.7 - Arbitrary File Retrieval
- **File**: `CVE-2018-6008.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2018,joomla,lfi
- **Description**: Arbitrary file retrieval exists in the Jtag Members Directory 5.3.7 component for Joomla! via the download_file parameter.

#### Joomla! Component GMapFP 3.5 - Unauthenticated Arbitrary File Upload
- **File**: `CVE-2020-23972-1.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,joomla
- **Description**: An attacker can access the upload function of the application
without authenticating to the application and also can upload
files due the issues of unrestricted file upload which can be
bypassed by ch...

#### Joomla! Component GMapFP 3.5 - Unauthenticated Arbitrary File Upload
- **File**: `CVE-2020-23972-2.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,joomla
- **Description**: An attacker can access the upload function of the application
without authenticating to the application and also can upload
files due the issues of unrestricted file upload which can be
bypassed by ch...

#### Joomla! Component GMapFP 3.5 - Unauthenticated Arbitrary File Upload
- **File**: `CVE-2020-23972.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,joomla
- **Description**: An attacker can access the upload function of the application
without authenticating to the application and also can upload
files due the issues of unrestricted file upload which can be
bypassed by ch...

#### Joomla Helpdesk Pro plugin before 1.4.0 - Local File Disclosure
- **File**: `CVE-2015-4074.yaml`
- **Author**: 0x_Akoko
- **Tags**: cve,cve2015,joomla,plugin,lfi
- **Description**: Directory traversal vulnerability in the Helpdesk Pro plugin before 1.4.0 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the filename parameter in a ticket.download_...

#### JE Messenger 1.2.2 Joomla - Directory Traversal
- **File**: `CVE-2019-9922.yaml`
- **Author**: 0x_Akoko
- **Tags**: cve,cve2019,joomla,messenger,lfi
- **Description**: An issue was discovered in the Harmis JE Messenger component 1.2.2 for Joomla. Directory Traversal allows read access to arbitrary files.

#### CVE-2023-23752-joomla
- **File**: `CVE-2023-23752_1.yaml`
- **Author**: hakimi
- **Tags**: CVE-2023-23752
- **Description**: description

#### Joomla! Component GMapFP 3.5 - Arbitrary File Upload
- **File**: `CVE-2020-23972_1.yaml`
- **Author**: dwisiswant0
- **Tags**: cve,cve2020,joomla,edb,packetstorm,fileupload,intrusive
- **Description**: Joomla! Component GMapFP 3.5 is vulnerable to arbitrary file upload vulnerabilities. An attacker can access the upload function of the application
without authentication and can upload files because o...

#### Joomla! com_fabrik 3.9.11 - Directory Traversal
- **File**: `joomla-com-fabrik-lfi_1.yaml`
- **Author**: dhiyaneshDk
- **Tags**: joomla,lfi
- **Description**: No description

#### Joomla! Installer Exposure
- **File**: `joomla-installer.yaml`
- **Author**: DhiyaneshDk
- **Tags**: misconfig,joomla,install
- **Description**: No description

#### Joomla! Component com_sef - Local File Inclusion
- **File**: `joomla-jvehicles-lfi_1.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi,edb
- **Description**: A local file inclusion vulnerability in the Jvehicles (com_jvehicles) component version 1.0 for Joomla! allows remote attackers to load arbitrary files via the controller parameter in index.php.

### Medium Severity (7 templates)

#### Joomla! Database File List
- **File**: `joomla-file-listing.yaml`
- **Author**: iampritam
- **Tags**: exposure,joomla,listing,database
- **Description**: A Joomla! database directory /libraries/joomla/database/ was found exposed and has directory indexing enabled.

#### Joomla! Component CCNewsLetter - Local File Inclusion
- **File**: `CVE-2010-0467.yaml`
- **Author**: daffainfo
- **Tags**: cve,cve2010,joomla,lfi
- **Description**: A directory traversal vulnerability in the ccNewsletter (com_ccnewsletter) component 1.0.5 for Joomla! allows remote attackers to read arbitrary files via a .. (dot dot) in the controller parameter in...

#### ChronoForums 2.0.11 - Directory Traversal
- **File**: `CVE-2021-28377.yaml`
- **Author**: 0x_Akoko
- **Tags**: cve,cve2021,chronoforums,lfi,joomla
- **Description**: The ChronoForums avatar function is vulnerable through unauthenticated path traversal attacks. This enables unauthenticated attackers to read arbitrary files, like for instance Joomla's configuration ...

#### Joomla! ChronoForums 2.0.11 - Local File Inclusion
- **File**: `CVE-2021-28377_1.yaml`
- **Author**: 0x_Akoko
- **Tags**: cve,cve2021,chronoforums,lfi,joomla
- **Description**: Joomla! ChronoForums 2.0.11 avatar function is vulnerable to local file inclusion through unauthenticated path traversal attacks. This enables an attacker to read arbitrary files, for example the Joom...

#### Joomla! Webservice - Password Disclosure
- **File**: `CVE-2023-23752_2.yaml`
- **Author**: badboycxcc,Sascha Brendel
- **Tags**: cve,cve2023,joomla
- **Description**: An issue was discovered in Joomla! 4.0.0 through 4.2.7. An improper access check allows unauthorized access to webservice endpoints.


#### Joomla! Database File List
- **File**: `joomla-file-listing_1.yaml`
- **Author**: iampritam
- **Tags**: exposure,joomla,listing,database,edb
- **Description**: A Joomla! database directory /libraries/joomla/database/ was found exposed and has directory indexing enabled.

#### Joomla! Manifest File - Disclosure
- **File**: `joomla-manifest-file_1.yaml`
- **Author**: oppsec
- **Tags**: misc,joomla
- **Description**: A Joomla! Manifest file was discovered. joomla.xml is a file which stores information about installed Joomla!, such as version, files, and paths.

### Low Severity (2 templates)

#### Joomla Config Dist File
- **File**: `joomla-config-file.yaml`
- **Author**: oppsec
- **Tags**: config,exposure,joomla
- **Description**: configuration.php-dist is a file created by Joomla to save Joomla settings.

#### Joomla! Configuration File - Detect
- **File**: `joomla-config-file_1.yaml`
- **Author**: oppsec
- **Tags**: config,exposure,joomla
- **Description**: Joomla! configuration.php-dist file was detected.

### Info Severity (4 templates)

#### Joomla htaccess file disclosure
- **File**: `joomla-htaccess.yaml`
- **Author**: oppsec
- **Tags**: misc,joomla
- **Description**: Joomla has an htaccess file to store configurations about HTTP config, directory listing, etc.

#### Joomla Manifest File Disclosure
- **File**: `joomla-manifest-file.yaml`
- **Author**: oppsec
- **Tags**: misc,joomla
- **Description**: A Joomla Manifest file was discovered. joomla.xml is a file which stores information about installed Joomla, such as version, files, and paths.

#### Joomla! Panel
- **File**: `joomla-panel.yaml`
- **Author**: its0x08
- **Tags**: panel,joomla
- **Description**: No description

#### Joomla! Panel
- **File**: `joomla-panel_1.yaml`
- **Author**: its0x08
- **Tags**: panel,joomla
- **Description**: No description

