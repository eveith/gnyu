Name: bogofilter
Version: 1.1.5
Release: 1ev
Summary: A Bayesian spam filter
URL: http://bogofilter.sourceforge.net/
Group: Applications/Internet
License: GPL
Vendor: MSP Slackware
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, flex, db, opensp
Requires: db

%description
Bogofilter is a Bayesian spam filter. In its normal mode of operation, it
takes an email message or other text on standard input, does a statistical
check against lists of "good" and "bad" words, and returns a status code
indicating whether or not the message is spam. Bogofilter is designed with
fast algorithms (including Berkeley DB system), coded directly in C, and tuned
for speed, so it can be used for production by sites that process a lot of
mail.


%prep
%setup -q


%build
%configure \
	--with-included-gsl
make %{_smp_mflags} 


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

mv "$RPM_BUILD_ROOT"/etc/bogofilter.cf.example \
	"$RPM_BUILD_ROOT"/etc/bogofilter.cf


[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS COPYING GETTING.STARTED NEWS* README* RELEASE.NOTES TODO doc/
%config(noreplace) /etc/bogofilter.cf
%{_bindir}/bf_*
%{_bindir}/bogo*
%{_mandir}/man1/*.1*
