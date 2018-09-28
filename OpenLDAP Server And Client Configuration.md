<font size=4>

# Server

#### 1.关闭iptables
>$ service iptables stop</br>
><font color=red>**# 或自行配置iptables规则**</font>

#### 2.关闭SELinux
>1.临时关闭
>
>$ getenforce</br>
>Enforcing
>
>$ setenforce 0
>
>$ getenforce</br>
>Permissive
>
>2.永久关闭
>
>$ sed -i 's/SELINUX=.*/SELINUX=disabled/g' /etc/selinux/config

#### 3.安装OpenLDAP Server
>$ yum -y install openldap-servers

#### 4.修改配置文件
>$ \cp -arp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
>
>$ chown ldap:ldap /var/lib/ldap/DB_CONFIG
>
>$ \cp -arp /usr/share/openldap-servers/slapd.conf.obsolete /etc/openldap/slapd.conf
>
>$ \cp -arp /etc/openldap/slapd.conf{,_$(date +%F)}
>
>$ slappasswd</br>
>New password: wSffQl00SIWbnyo3<font color=red>&nbsp;&nbsp;&nbsp;&nbsp;**# 此处为密码，不在屏幕上显示**</font></br>
>Re-enter new password: wSffQl00SIWbnyo3<font color=red>&nbsp;&nbsp;&nbsp;&nbsp;**# 同上**</font></br>
>{SSHA}6MjZaOMp4PczlpNISEchqlnPrmF7dndl
>
>$ sed -i '107,117s/dc=my-domain,dc=com/dc=ourscloud,dc=win/g' /etc/openldap/slapd.conf</br>

    执行以下长语句：
    sed -i 'N;122a\rootpw          {SSHA}6MjZaOMp4PczlpNISEchqlnPrmF7dndl' /etc/openldap/slapd.conf
>
>$ diff /etc/openldap/slapd.conf{,_$(date +%F)}

    107c107
    <         by dn.exact="cn=Manager,dc=ourscloud,dc=win" read
    ---
    >         by dn.exact="cn=Manager,dc=my-domain,dc=com" read
    115c115
    < suffix                "dc=ourscloud,dc=win"
    ---
    > suffix                "dc=my-domain,dc=com"
    117c117
    < rootdn                "cn=Manager,dc=ourscloud,dc=win"
    ---
    > rootdn                "cn=Manager,dc=my-domain,dc=com"
    123d122
    < rootpw          {SSHA}6MjZaOMp4PczlpNISEchqlnPrmF7dndl

>$ service slapd start</br>
>$ chkconfig --level 3 slapd on
>
>$ rm -rf /etc/openldap/slapd.d/*
>
>$ slaptest -f /etc/openldap/slapd.conf -F /etc/openldap/slapd.d/

    config file testing succeeded

>$ chown -R ldap:ldap /etc/openldap/slapd.d/
>
>$ service slapd restart
>
>$ ps -aux | egrep ldap

    Warning: bad syntax, perhaps a bogus '-'? See /usr/share/doc/procps-3.2.8/FAQ
    ldap       4828  0.0  0.2 518864  5648 ?        Ssl  10:51   0:00 /usr/sbin/slapd -h  ldap:/// ldapi:/// -u ldap
    root       4834  0.0  0.0 103320   888 pts/0    S+   10:51   0:00 egrep ldap

>$ netstat -natulp | egrep slapd

    tcp        0      0 0.0.0.0:389                 0.0.0.0:*                   LISTEN      4828/slapd
    tcp        0      0 :::389                      :::*                        LISTEN      4828/slapd

>$ yum -y install migrationtools
>
>$ cd /usr/share/migrationtools/
>
>$ \cp -arp migrate_common.ph{,_$(date +%F)}

    执行以下长语句：
    sed -i 's/\$DEFAULT_MAIL_DOMAIN = ".*";/\$DEFAULT_MAIL_DOMAIN = "ourscloud.win";/g; s/\$DEFAULT_BASE = "dc=.*,dc=.*";/\$DEFAULT_BASE = "dc=ourscloud,dc=win";/g' migrate_common.ph

>$ ./migrate_base.pl > /tmp/base.ldif
>
>$ ./migrate_passwd.pl /etc/passwd > /tmp/passwd.ldif
>
>$ ./migrate_group.pl /etc/group > /tmp/group.ldif
>
>$ ldapadd -x -D "cn=Manager,dc=ourscloud,dc=win" -w wSffQl00SIWbnyo3 -f /tmp/base.ldif

    adding new entry "dc=ourscloud,dc=win"

    adding new entry "ou=Hosts,dc=ourscloud,dc=win"

    adding new entry "ou=Rpc,dc=ourscloud,dc=win"

    adding new entry "ou=Services,dc=ourscloud,dc=win"

    adding new entry "nisMapName=netgroup.byuser,dc=ourscloud,dc=win"

    adding new entry "ou=Mounts,dc=ourscloud,dc=win"

    adding new entry "ou=Networks,dc=ourscloud,dc=win"

    adding new entry "ou=People,dc=ourscloud,dc=win"

    adding new entry "ou=Group,dc=ourscloud,dc=win"

    adding new entry "ou=Netgroup,dc=ourscloud,dc=win"

    adding new entry "ou=Protocols,dc=ourscloud,dc=win"

    adding new entry "ou=Aliases,dc=ourscloud,dc=win"

    adding new entry "nisMapName=netgroup.byhost,dc=ourscloud,dc=win"

>$ ldapsearch -x -H ldap://127.0.0.1 -b '' -s base

    # extended LDIF
    #
    # LDAPv3
    # base <> with scope baseObject
    # filter: (objectclass=*)
    # requesting: ALL
    #

    #
    dn:
    objectClass: top
    objectClass: OpenLDAProotDSE

    # search result
    search: 2
    result: 0 Success

    # numResponses: 2
    # numEntries: 1

>$ ldapadd -x -D "cn=Manager,dc=ourscloud,dc=win" -w wSffQl00SIWbnyo3 -f /tmp/passwd.ldif

    adding new entry "uid=root,ou=People,dc=ourscloud,dc=win"

    adding new entry "uid=bin,ou=People,dc=ourscloud,dc=win"

    adding new entry "uid=daemon,ou=People,dc=ourscloud,dc=win"
    (略)

>$ ldapadd -x -D "cn=Manager,dc=ourscloud,dc=win" -w wSffQl00SIWbnyo3 -f /tmp/group.ldif

    adding new entry "cn=root,ou=Group,dc=ourscloud,dc=win"

    adding new entry "cn=bin,ou=Group,dc=ourscloud,dc=win"

    adding new entry "cn=daemon,ou=Group,dc=ourscloud,dc=win"
    (略)

>$ ldapsearch -x -H ldap://127.0.0.1 -b 'dc=ourscloud,dc=win'

    # extended LDIF
    #
    # LDAPv3
    # base <dc=ourscloud,dc=win> with scope subtree
    # filter: (objectclass=*)
    # requesting: ALL
    #
    
    # ourscloud.win
    dn: dc=ourscloud,dc=win
    dc: ourscloud
    objectClass: top
    objectClass: domain
    
    (略)
    
    # search result
    search: 2
    result: 0 Success
    
    # numResponses: 106
    # numEntries: 105

>$ ldapdelete -x -D "cn=Manager,dc=ourscloud,dc=win" -w wSffQl00SIWbnyo3 -r 'dc=ourscloud,dc=win'
>
>$ ldapsearch -x -H ldap://127.0.0.1 -b 'dc=ourscloud,dc=win'

    # extended LDIF
    #
    # LDAPv3
    # base <dc=ourscloud,dc=win> with scope subtree
    # filter: (objectclass=*)
    # requesting: ALL
    #
    
    # search result
    search: 2
    result: 32 No such object
    
    # numResponses: 1

>$ useradd ldapuser1</br>
>$ echo 'user1' | passwd --stdin ldapuser1</br>
>$ useradd ldapuser2</br>
>$ echo 'user2' | passwd --stdin ldapuser2
>
>$ egrep '^ldapuser' /etc/group > /tmp/group
>
>$ egrep '^ldapuser' /etc/passwd > /tmp/passwd
>
>$ ldapsearch -x -b 'dc=ourscloud,dc=win' -LLL

    No such object (32)

>$ ./migrate_passwd.pl /tmp/passwd > /tmp/passwd.ldif
>
>$ ./migrate_group.pl /tmp/group > /tmp/group.ldif
>
>$ ldapadd -x -D "cn=Manager,dc=ourscloud,dc=win" -w wSffQl00SIWbnyo3 -f /tmp/base.ldif
>
>$ ldapadd -x -D "cn=Manager,dc=ourscloud,dc=win" -w wSffQl00SIWbnyo3 -f /tmp/passwd.ldif

    adding new entry "uid=ldapuser1,ou=People,dc=ourscloud,dc=win"

    adding new entry "uid=ldapuser2,ou=People,dc=ourscloud,dc=win"

>$ ldapadd -x -D "cn=Manager,dc=ourscloud,dc=win" -w wSffQl00SIWbnyo3 -f /tmp/group.ldif

    adding new entry "cn=ldapuser1,ou=Group,dc=ourscloud,dc=win"

    adding new entry "cn=ldapuser2,ou=Group,dc=ourscloud,dc=win"

>$ ldapsearch -x -b 'dc=ourscloud,dc=win' -LLL

    dn: dc=ourscloud,dc=win
    dc: ourscloud
    objectClass: top
    objectClass: domain
    
    (略)
    
    dn: uid=ldapuser1,ou=People,dc=ourscloud,dc=win
    uid: ldapuser1
    cn: ldapuser1
    objectClass: account
    objectClass: posixAccount
    objectClass: top
    objectClass: shadowAccount
    userPassword:: e2NyeXB0fSQ2JFJ0TmpaR2xKJDAudXJsdGxEWkNyZWxkSWcyLy96bFh2RUlLRTJ
     UNW5ydUx3Zjd5clNUS3BQRU1tVE5zQlR4SEZpNHBNQjZ1dld5U296RkFLRm9mSGlHdUF6d1FLTW4x
    shadowLastChange: 17802
    shadowMin: 0
    shadowMax: 99999
    shadowWarning: 7
    loginShell: /bin/bash
    uidNumber: 500
    gidNumber: 500
    homeDirectory: /home/ldapuser1
    
    dn: uid=ldapuser2,ou=People,dc=ourscloud,dc=win
    uid: ldapuser2
    cn: ldapuser2
    objectClass: account
    objectClass: posixAccount
    objectClass: top
    objectClass: shadowAccount
    userPassword:: e2NyeXB0fSQ2JDJ3OVp2elkvJEpnWWVkQ1JXRDlCeGNHeUpVcnVuTVc3WVFpVGk
     wdy5Ra1A2ZmlBT3hkTjFDLkRvV0RHaFVkbjVQb2hpZHkzTGtmb2FEQnVENjFMZUVqQS5hL3dUSEow
    shadowLastChange: 17802
    shadowMin: 0
    shadowMax: 99999
    shadowWarning: 7
    loginShell: /bin/bash
    uidNumber: 501
    gidNumber: 501
    homeDirectory: /home/ldapuser2
    
    dn: cn=ldapuser1,ou=Group,dc=ourscloud,dc=win
    objectClass: posixGroup
    objectClass: top
    cn: ldapuser1
    userPassword:: e2NyeXB0fXg=
    gidNumber: 500
    
    dn: cn=ldapuser2,ou=Group,dc=ourscloud,dc=win
    objectClass: posixGroup
    objectClass: top
    cn: ldapuser2
    userPassword:: e2NyeXB0fXg=
    gidNumber: 501

>$ yum -y install nginx php-fpm phpldapadmin
>
>$ mv /etc/nginx/conf.d/default.conf{,_$(date +%F)}
>
>$ vim /etc/nginx/conf.d/phpldapadmin.conf

    server {
        listen       80;
        server_name  192.168.3.120;
    
        #charset koi8-r;
        error_log  /var/log/nginx/192.168.3.120.error.log;
        access_log  /var/log/nginx/192.168.3.120.access.log  main;
    
        location / {
            root   /usr/share/phpldapadmin/htdocs;
            index  index.php login.php;
        }
    
        error_page  404              /404.html;
    
        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/share/nginx/html;
        }
    
        location ~ \.php$ {
            root           /usr/share/phpldapadmin/htdocs;
            fastcgi_pass   127.0.0.1:9000;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            include        fastcgi_params;
        }
    }

>$ service nginx start</br>
>$ chkconfig --level 3 nginx on
>
>$ service php-fpm start</br>
>$ chkconfig --level 3 php-fpm on
>
>$ \cp -arp /etc/phpldapadmin/config.php{,_$(date +%F)}
>
>$ vim /etc/phpldapadmin/config.php

    <?php
    ……
    $servers->newServer('ldap_pla');
    $servers->setValue('server','name','LDAP Server');
    $servers->setValue('server','host','192.168.3.120');
    $servers->setValue('server','port',389);
    $servers->setValue('server','base',array('dc=ourscloud,dc=win'));
    $servers->setValue('login','auth_type','cookie');
    $servers->setValue('login','bind_id','cn=Manager,dc=ourscloud,dc=win');
    $servers->setValue('login','bind_pass','wSffQl00SIWbnyo3');
    $servers->setValue('server','tls',false);
    ?>

>$ cd /usr/share/phpldapadmin/
>
>$ chown -R nobody:nobody ./htdocs/
>
>$ chmod -R 777 ./htdocs/

#### 5.登录php LDAP admin
>登录地址：http://192.168.3.120/</br>
>帐号：ldapuser1</br>
>密码：user1

---

# Client

#### 1.安装OpenLDAP Client
>$ yum -y install nss-pam-ldapd openldap-clients pam_ldap

#### 2.修改配置文件
>$ \cp -arp /etc/sysconfig/authconfig{,_$(date +%F)}

    执行以下长语句：
    sed -i 's/^USEMKHOMEDIR=.*/USEMKHOMEDIR=yes/g; s/^PASSWDALGORITHM=.*/PASSWDALGORITHM=yes/g; s/^USELDAPAUTH=.*/USELDAPAUTH=yes/g; s/^USELDAP=.*/USELDAP=yes/g; s/^USESYSNETAUTH=.*/USESYSNETAUTH=yes/g' /etc/sysconfig/authconfig

>$ diff /etc/sysconfig/authconfig{,_$(date +%F)}

    2c2
    < USEMKHOMEDIR=yes
    ---
    > USEMKHOMEDIR=no
    12,13c12,13
    < PASSWDALGORITHM=yes
    < USELDAPAUTH=yes
    ---
    > PASSWDALGORITHM=sha512
    > USELDAPAUTH=no
    21c21
    < USELDAP=yes
    ---
    > USELDAP=no
    24c24
    < USESYSNETAUTH=yes
    ---
    > USESYSNETAUTH=no

>$ \cp -arp /etc/openldap/ldap.conf{,_$(date +%F)}

    执行以下长语句：
    sed -i 's@^#BASE.*@BASE   dc=ourscloud,dc=win@g; s@^#URI.*@URI    ldap://192.168.3.120@g' /etc/openldap/ldap.conf

>$ diff /etc/openldap/ldap.conf{,_$(date +%F)}

    8,9c8,9
    < BASE   dc=ourscloud,dc=win
    < URI    ldap://192.168.3.120
    ---
    > #BASE   dc=example,dc=com
    > #URI    ldap://ldap.example.com ldap://ldap-master.example.com:666

>$ ldapsearch -x -b 'dc=ourscloud,dc=win'

    # extended LDIF
    #
    # LDAPv3
    # base <dc=ourscloud,dc=win> with scope subtree
    # filter: (objectclass=*)
    # requesting: ALL
    #
    
    # ourscloud.win
    dn: dc=ourscloud,dc=win
    dc: ourscloud
    objectClass: top
    objectClass: domain
    
    (略)
    
    # ldapuser1, People, ourscloud.win
    dn: uid=ldapuser1,ou=People,dc=ourscloud,dc=win
    uid: ldapuser1
    cn: ldapuser1
    objectClass: account
    objectClass: posixAccount
    objectClass: top
    objectClass: shadowAccount
    userPassword:: e2NyeXB0fSQ2JFJ0TmpaR2xKJDAudXJsdGxEWkNyZWxkSWcyLy96bFh2RUlLRTJ
     UNW5ydUx3Zjd5clNUS3BQRU1tVE5zQlR4SEZpNHBNQjZ1dld5U296RkFLRm9mSGlHdUF6d1FLTW4x
    shadowLastChange: 17802
    shadowMin: 0
    shadowMax: 99999
    shadowWarning: 7
    loginShell: /bin/bash
    uidNumber: 500
    gidNumber: 500
    homeDirectory: /home/ldapuser1
    
    # ldapuser2, People, ourscloud.win
    dn: uid=ldapuser2,ou=People,dc=ourscloud,dc=win
    uid: ldapuser2
    cn: ldapuser2
    objectClass: account
    objectClass: posixAccount
    objectClass: top
    objectClass: shadowAccount
    userPassword:: e2NyeXB0fSQ2JDJ3OVp2elkvJEpnWWVkQ1JXRDlCeGNHeUpVcnVuTVc3WVFpVGk
     wdy5Ra1A2ZmlBT3hkTjFDLkRvV0RHaFVkbjVQb2hpZHkzTGtmb2FEQnVENjFMZUVqQS5hL3dUSEow
    shadowLastChange: 17802
    shadowMin: 0
    shadowMax: 99999
    shadowWarning: 7
    loginShell: /bin/bash
    uidNumber: 501
    gidNumber: 501
    homeDirectory: /home/ldapuser2
    
    # ldapuser1, Group, ourscloud.win
    dn: cn=ldapuser1,ou=Group,dc=ourscloud,dc=win
    objectClass: posixGroup
    objectClass: top
    cn: ldapuser1
    userPassword:: e2NyeXB0fXg=
    gidNumber: 500
    
    # ldapuser2, Group, ourscloud.win
    dn: cn=ldapuser2,ou=Group,dc=ourscloud,dc=win
    objectClass: posixGroup
    objectClass: top
    cn: ldapuser2
    userPassword:: e2NyeXB0fXg=
    gidNumber: 501
    
    # search result
    search: 2
    result: 0 Success
    
    # numResponses: 18
    # numEntries: 17

>$ authconfig --enableldap --enableldapauth --ldapserver=192.168.3.120 --ldapbasedn="dc=ourscloud,dc=win" --enablemkhomedir --update

    执行以下语句块：
    \cp -arp /etc/pam.d/system-auth-ac{,_$(date +%F)}
    sed -i 's/sss/ldap/g' /etc/pam.d/system-auth-ac
    echo 'session     optional      pam_oddjob_mkhomedir.so skel=/etc/skel/  umask=0077' >> /etc/pam.d/system-auth-ac
    echo 'session     required      pam_mkhomedir.so  skel=/etc/skel/  umask=0077' >> /etc/pam.d/system-auth-ac

    \cp -arp /etc/pam.d/password-auth-ac{,_$(date +%F)}
    sed -i 's/sss/ldap/g' /etc/pam.d/password-auth-ac
    echo 'session     optional      pam_oddjob_mkhomedir.so skel=/etc/skel/  umask=0077' >> /etc/pam.d/password-auth-ac
    echo 'session     required      pam_mkhomedir.so  skel=/etc/skel/  umask=0077' >> /etc/pam.d/password-auth-ac
    
> $ service oddjobd start
>
>$ chkconfig --level 3 oddjobd on

#### 3.登录Linux
>登录方式：ssh ldapuser1@192.168.3.121</br>
>密码：user1

</font>