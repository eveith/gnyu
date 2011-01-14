Name: libksba
Version: 1.0.3
Release: 2ev
Summary: Provides an API to create and parse X.509 and CMS related objects
URL: http://www.gnupg.org/related_software/libksba/
Group: System Environment/Libraries
License: GPL-3
Vendor: GNyU-Linux
Source: ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires(prep,build,install): coreutils
BuildRequires(build,install): make
BuildRequires(build): gcc, libgpg-error

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
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig
update-info-dir

%postun
/sbin/ldconfig
update-info-dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README* THANKS TODO VERSION
%{_bindir}/ksba-config
%{_libdir}/libksba.*
%{_includedir}/ksba.h
%doc %{_infodir}/ksba.info*
%{_datadir}/aclocal/ksba.m4
