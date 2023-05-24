Name:      c2-ec2-netutils
Summary:   A set of network tools for managing and auto configuration ENIs
Version:   1.1
Release:   1%{?dist}
License:   MIT
Source0:   53-c2-network-interfaces.rules.systemd
Source1:   53-c2-network-interfaces.rules.upstart
Source2:   75-persistent-net-generator.rules
Source3:   ec2net-functions
Source4:   c2-net.hotplug
Source5:   ec2ifup
Source6:   ec2ifdown
Source7:   ec2ifup.8
Source8:   ec2ifscan
Source9:   ec2ifscan.8
Source10:  elastic-network-interfaces.conf
Source11:  ec2net-scan.service
Source12:  c2_write_net_rules
Source13:  c2_rule_generator.functions
Source14:  ec2net-ifup@.service

URL:       https://github.com/C2Devel/c2-ec2-netutils
BuildArch: noarch
Requires:  wicked
Requires:  curl
Requires:  sed
Requires:  iproute

Provides: c2-ec2-netutils
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
c2-ec2-netutils contains a set of utilities for managing elastic network interfaces.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/network/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/network/scripts/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8/

install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/
install -m644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/network/scripts/
install -m755 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/network/scripts/
install -d -m755 $RPM_BUILD_ROOT%{_sbindir}
install -m755 %{SOURCE5} $RPM_BUILD_ROOT%{_sbindir}/
install -m755 %{SOURCE6} $RPM_BUILD_ROOT%{_sbindir}/
install -m755 %{SOURCE8} $RPM_BUILD_ROOT%{_sbindir}/
install -m644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/53-c2-network-interfaces.rules
install -d -m755 $RPM_BUILD_ROOT%{_unitdir}
install -m644 %{SOURCE11} $RPM_BUILD_ROOT%{_unitdir}/ec2net-scan.service
install -m644 %{SOURCE14} $RPM_BUILD_ROOT%{_unitdir}/ec2net-ifup@.service
install -d -m755 $RPM_BUILD_ROOT/usr/lib/udev
install -m644 %{SOURCE12} $RPM_BUILD_ROOT/usr/lib/udev
install -m644 %{SOURCE13} $RPM_BUILD_ROOT/usr/lib/udev
install -m644 %{SOURCE7} $RPM_BUILD_ROOT%{_mandir}/man8/ec2ifup.8
ln -s ./ec2ifup.8.gz $RPM_BUILD_ROOT%{_mandir}/man8/ec2ifdown.8.gz
install -m644 %{SOURCE9} $RPM_BUILD_ROOT%{_mandir}/man8/ec2ifscan.8

%clean
rm -rf $RPM_BUILD_ROOT

%post
ln -s -f %{_unitdir}/ec2net-scan.service %{_sysconfdir}/systemd/system/multi-user.target.wants/ec2net-scan.service

%postun
%{__rm} -f %{_sysconfdir}/systemd/system/multi-user.target.wants/ec2net-scan.service

%files
%{_sysconfdir}/udev/rules.d/53-c2-network-interfaces.rules
%{_sysconfdir}/udev/rules.d/75-persistent-net-generator.rules
%{_sysconfdir}/sysconfig/network/scripts/ec2net-functions
%{_sysconfdir}/sysconfig/network/scripts/c2-net.hotplug
%{_sbindir}/ec2ifup
%{_sbindir}/ec2ifdown
%{_sbindir}/ec2ifscan
%attr(0644,root,root) %{_unitdir}/ec2net-scan.service
%attr(0644,root,root) %{_unitdir}/ec2net-ifup@.service
%attr(755, -, -) %{_prefix}/lib/udev/c2_write_net_rules
%{_prefix}/lib/udev/c2_rule_generator.functions
%doc %{_mandir}/man8/ec2ifup.8.gz
%doc %{_mandir}/man8/ec2ifdown.8.gz
%doc %{_mandir}/man8/ec2ifscan.8.gz

%changelog
* Wed May 24 2023 Georgy Melnikov <gmelnikov@croc.ru> 1.1
- Create c2-ec2-netutils for SUSE-like distros

