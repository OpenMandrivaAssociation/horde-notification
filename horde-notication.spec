%define prj    Horde_Notification

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-notification
Version:       0.0.2
Release:       %mkrel 1
Summary:       Horde Notification System
License:       LGPL
Group:         Productivity/Networking/Web/Servers
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
PreReq:        %{_bindir}/pear
Requires:      php-pear
Requires:      php-pear-channel-horde
Requires:      php-gettext
BuildRequires: horde-framework
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The Notification:: class provides a subject-observer pattern for raising and
showing messages of different types and to different listeners.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package*.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Notification
%dir %{peardir}/Horde/Notification/Listener
%{peardir}/Horde/Notification.php
%{peardir}/Horde/Notification/Event.php
%{peardir}/Horde/Notification/Listener.php
%{peardir}/Horde/Notification/Listener/audio.php
%{peardir}/Horde/Notification/Listener/javascript.php
%{peardir}/Horde/Notification/Listener/mobile.php
%{peardir}/Horde/Notification/Listener/status.php

