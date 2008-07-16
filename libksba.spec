Name: libksba
Version: 1.0.1
Release: 1ev
Summary: Provides an API to create and parse X.509 and CMS related objects
URL: http://www.gnupg.org/related_software/libksba/
Group: System Environment/Libraries
License: GPL
Vendor: MSP Slackware
Source: ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, libgpg-error
Requires: libgpg-error
Provides: libtool(%{_libdir}/libksba.la)

%description
Libksba is a library to make the tasks of working with X.509 certificates, CMS
data and related objects more easy. It provides a highlevel interface to the
implemented protocols and presents the data in a consistent way. There is no
more need to worry about all the nasty details of the protocols. The API gives
the C programmer an easy way of interacting with the data. It copes with the
version details X.509 protocols tend to have as well as with the many
different versions and dialects. Applications must usually cope with all of
this and it has to be coded over and over again. Libksba hides this by
providing just one API which does the Right Thing. Support for new features
will be added as needed.


%prep
%setup -q


%build
%configure
make


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"


[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig
/sbin/install-info --info-dir=%{_infodir} %{_infodir}/ksba.info*

%postun
/sbin/ldconfig
/sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/ksba.info*


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README* THANKS TODO VERSION
%{_bindir}/ksba-config
%{_libdir}/libksba.*
%{_includedir}/ksba.h
%{_infodir}/ksba.info*
%{_datadir}/aclocal/ksba.m4
