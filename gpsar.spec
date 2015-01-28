# This is a RPM spec file for gpsar (Gnuplot Sar)

# _version and _release should be defined on the rpmbuild command:
#     --define "_version 1.0" --define "_release 1"

%define debug_package   %{nil}

%define name            gpsar
%define release         %{_release}%{?dist}
%define version         %{_version}
%define app_version     %{_app_version}

%define summary         Generate a HTML SAR report using Gnuplot

%define platform_bin_dir   %{_sbindir}
%define platform_doc_dir   %{_defaultdocdir}/gpsar

Summary:        %{summary}
Vendor:         Cloudian Inc.
URL:            http://www.cloudian.com
License:        GPLv3
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
Group:          Applications/System

Requires:       bash
Requires:       coreutils
Requires:       gawk
Requires:       grep
Requires:       sysstat
Requires:       gnuplot
Requires:       asciidoc
Requires:       liberation-fonts-common
Requires:       liberation-sans-fonts

%description
gpsar processes sysstat's SAR data files using sadf and plots the
system information to a series of PNG graphics which it then 
combines into a HTML report.

%prep
# Unpack the source tar file
%setup -q -c -n gpsar

%build
# build the source
make version

%install
# install the build to the buildroot
%__rm -rf %{buildroot}

%define buildroot_bin         %{buildroot}/%{platform_bin_dir}
%define buildroot_docs        %{buildroot}/%{platform_doc_dir}
%define buildroot_man         %{buildroot}/%{_mandir}

%__install -d %{buildroot_bin}
%__install -d %{buildroot_docs}
%__install -d %{buildroot_man}/man1

%__install -m 0755 bin/gpsar     %{buildroot_bin}
%__install -m 0644 README        %{buildroot_docs}
%__install -m 0644 COPYING       %{buildroot_docs}

gzip man/man1/*
%__install -m 0644 man/man1/*    %{buildroot_man}/man1

%files
# List of files in the RPM
%defattr(-,root,root,-)
%{platform_bin_dir}/gpsar

%doc %{platform_doc_dir}/*
%{_mandir}/man1/*

%clean
# clean the buildroot
%__rm -rf %{buildroot}

%pre
# RPM pre-install script
exit 0

%post
# RPM post-install script
exit 0

%preun
# RPM pre-uninstall script
exit 0

%postun
# RPM post-uninstall script
exit 0

%changelog
* Wed Jan 28 2015 Cloudian Inc <support@cloudian.com> - 0.6-1
- Add optional undocumented pidstat memory utilization graphing
* Mon Jan 26 2015 Cloudian Inc <support@cloudian.com> - 0.5-1
- Fix OS restart problem and add font dependency.
* Thu Mar 14 2014 Cloudian Inc <support@cloudian.com> - 0.4-1
- Added Basic System Info.
* Thu Mar 13 2014 Cloudian Inc <support@cloudian.com> - 0.3-1
- Check sadf timeformats as they vary.
* Thu Mar 13 2014 Cloudian Inc <support@cloudian.com> - 0.2-1
- Various Fixes for CentOS 6.
* Thu Mar 13 2014 Cloudian Inc <support@cloudian.com> - 0.1-1
- Initial RPM Release
