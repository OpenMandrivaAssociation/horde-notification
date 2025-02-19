%define prj    Horde_Notification

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-notification
Version:       0.0.2
Release:       5
Summary:       Horde Notification System
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-pear
Requires:      php-pear-channel-horde
Requires:      php-gettext
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
The Notification:: class provides a subject-observer pattern for raising and
showing messages of different types and to different listeners.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

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



%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-4mdv2011.0
+ Revision: 564078
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2010.1
+ Revision: 524800
- incread release version to 3

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 523067
- increased release version to 2
- add spec with correct name
- wrong name
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear

* Sun Feb 28 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 512813
- chnaged %%__mv ../package*.xml to %%__mv ../package.xml
- added BuildRequires: php-pear-channel-horde
- removed BuiildRequires: horde-framework
- replaced PreReq with Requires(pre)
- import horde-notification


