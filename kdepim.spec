Name: kdepim
Version: 3.5.9
Release: 1ev
Summary: Personal Information Management suite for KDE
URL: http://kdepim.kde.org/
Group: Applications/Productivity
License: BSD, GPL-2, LGPL-2
Vendor: GNyU-Linux
Source: http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.bz2
Patch0: kdepim-3.5.6-cleartext_passwords.patch
Patch1: kdepim-kpilot_piolot-link_headers.patch
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-g++, make >= 3.79.1, perl, qt3 >= 3.3.2, fontconfig
BuildRequires: ghostscript, zlib >= 1.1, libxml2 >= 2.4.8, libxslt >= 1.0.7
BuildRequires: libmal >= 0.20, openldap-libs, pilot-link >= 0.12.0, gnokii
BuildRequires: openssl >= 0.9.6, gnupg >= 1.2.5, freetype >= 2.0.0,
BuildRequires: cyrus-sasl, gpgme, gnupg2

%description
KDE PIM is sub project of KDE. Its goal is to provide an application suite to
manage personal information. This includes mail, time, people and more. The
main result is KDE Kontact, KDE's personal information manager.


%prep
%setup -q


%build
%configure \
	--disable-debug \
    --disable-warnings \
	--enable-newdistrlists \
	--with-sasl 
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


# Search for files and directories in /usr/share.
# Files are simply added (no config stuff here), directories only if no other
# package contains them.

#find "${RPM_BUILD_ROOT}/%{_datadir}" -not -type d -print \
#	| sed "s,^$RPM_BUILD_ROOT,," >> kdepimfiles.list

#for dir in $(find "${RPM_BUILD_ROOT}/%{_datadir}" -type -d -print)
#do
#	dir=$(echo $dir | sed "s,^$RPM_BUILD_ROOT,,")
#	provides=$(rpm -q --whatprovides)
#	ret=$?
#	lc=$(echo "$provides" | grep -v kdepim | wc -l)
#	if [ "$ret" -ne 0 -o "$lc" -eq 0 ]
#	then
#		echo "%%dir $dir" >> kdepimfiles.list
#	fi
#done


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
#rm -f kdepimfiles.list


%files 
%defattr(-, root, root)
%doc MAINTAINERS README*
%doc %{_datadir}/doc/HTML/en/akregator/
%doc %{_datadir}/doc/HTML/en/kleopatra/
%doc %{_datadir}/doc/HTML/en/kwatchgnupg/
%doc %{_datadir}/doc/HTML/en/karm/
%doc %{_datadir}/doc/HTML/en/kmail/
%doc %{_datadir}/doc/HTML/en/knode/
%doc %{_datadir}/doc/HTML/en/kpilot/
%doc %{_datadir}/doc/HTML/en/kontact/
%doc %{_datadir}/doc/HTML/en/knotes/
%doc %{_datadir}/doc/HTML/en/kandy/
%doc %{_datadir}/doc/HTML/en/kalarm/
%doc %{_datadir}/doc/HTML/en/ktnef/
%doc %{_datadir}/doc/HTML/en/korn/
%doc %{_datadir}/doc/HTML/en/korganizer/
%doc %{_datadir}/doc/HTML/en/kaddressbook/
%doc %{_datadir}/doc/HTML/en/konsolekalendar/
%doc %{_datadir}/doc/HTML/en/kdepim-apidocs/
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*.h
%{_includedir}/calendar/
%{_includedir}/index/
%{_includedir}/libemailfunctions/
%{_includedir}/gpgme++/
%{_includedir}/qgpgme/
%{_includedir}/mimelib/
%{_includedir}/kgantt/
%{_includedir}/ktnef/
%{_includedir}/ksieve/
%{_includedir}/libkcal/
%{_includedir}/kleo/
%{_includedir}/kdepim/
%{_includedir}/akregator/
%{_includedir}/kmail/
%{_includedir}/korganizer/
%{_includedir}/kaddressbook/
%{_includedir}/kabc/
%{_includedir}/kontact/
%{_includedir}/kpilot/
%{_datadir}/apps/karmpart/
%{_datadir}/apps/kgantt/
%{_datadir}/apps/kmailcvt/
%{_datadir}/apps/ktnef/
%{_datadir}/apps/libkholidays/
%{_datadir}/apps/kmail/
%{_datadir}/apps/knode/
%{_datadir}/apps/libical/
%{_datadir}/apps/libkleopatra/
%{_datadir}/apps/kdepimwidgets/
%{_datadir}/apps/kwatchgnupg/
%{_datadir}/apps/kleopatra/
%{_datadir}/apps/knotes/
%{_datadir}/apps/kpilot/
%{_datadir}/apps/libkdepim/
%{_datadir}/apps/kandy/
%{_datadir}/apps/kalarm/
%{_datadir}/apps/akregator/
%{_datadir}/apps/korganizer/
%{_datadir}/apps/korgac/
%{_datadir}/apps/kaddressbook/
%{_datadir}/apps/karm/
%{_datadir}/apps/kontactsummary/
%{_datadir}/apps/kontact/
%{_datadir}/apps/kdepim/
%{_datadir}/apps/kconf_update/*
%{_datadir}/services/kresources/*.*
%{_datadir}/services/kresources/kcal/
%{_datadir}/services/kresources/kabc/
%{_datadir}/services/kresources/knotes/
%{_datadir}/services/korganizer/
%{_datadir}/services/kaddressbook/
%{_datadir}/services/kontact/
%{_datadir}/services/kded/*.*
%{_datadir}/applnk/Applications/
%{_datadir}/applnk/Utilities/*.desktop
%{_datadir}/applnk/.hidden/*
%{_datadir}/mimelnk/application/*
%{_datadir}/config*/*
%{_datadir}/autostart/*.desktop
%{_datadir}/icons/locolor/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/servicetypes/*.desktop
%{_datadir}/services/*.*
%{_datadir}/applications/kde/*.desktop
